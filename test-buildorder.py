from dataclasses import dataclass
from typing import List, Tuple, Dict

@dataclass
class Unit:
    name: str
    metal_cost: float
    energy_cost: float
    build_time: float       # in seconds
    metal_rate: float       # m/s once built
    energy_rate: float      # e/s once built
    energy_upkeep: float    # e/s upkeep (negative if consuming)
    build_power: float      # BP zur Beschleunigung von Bauprojekten
    prerequisites: List[str]  # Einheitencodes, die vorab gebaut sein müssen

# Definition der Einheiten
unit_stats: Dict[str, Unit] = {
    'armmex':   Unit('Metal Extractor',          50,    500,   18.0,   0.0,   0.0, -3.0,   0.0, []),
    'armsolar': Unit('Solar Collector',         155,      0,   26.0,   0.0,  20.0,  0.0,   0.0, []),
    'armmoho':  Unit('Advanced Metal Extractor',640,   8100,  141.0,   0.0,   0.0,  0.0,   0.0, ['armmex']),
    'armmex2':  Unit('Advanced Metal Extractor MK2',2000,12000,200.0,   4.0,   0.0, -3.0,   0.0, ['armmoho']),
    'armgant':  Unit('Experimental Gantry',    8400,  62000,  673.0,   0.0,   0.0,  0.0,   0.0, []),
    'armfus':   Unit('Fusion Reactor',         4500,  26000,  754.0,   0.0,1100.0,  0.0,   0.0, ['armgant']),
    'armbotfac':Unit('Bot Factory',            3000,  1500,  120.0,   0.0,   0.0,  0.0,   0.0, ['armgant']),
    'armcon':   Unit('Construction Bot',         20,      0,   12.0,   0.0,   0.0,  0.0,  10.0, ['armbotfac']),
    'armadvbot':Unit('Advanced Construction Bot',500,   150,   20.0,   0.0,   0.0,  0.0,  40.0, ['armcon']),
}

def simulate_build_order(
    build_order: List[Tuple[str, int]],
    metal_spot_rates: List[float],
    initial_metal: float,
    initial_energy: float,
    initial_build_power: float = 1.0
) -> None:
    """
    Simuliert den zeitlichen Ablauf und Ressourcen‑Verlauf einer Build‑Order.
    """
    t = 0.0
    metal = initial_metal
    energy = initial_energy
    build_power = initial_build_power
    completed_builds: List[str] = []
    active_units: List[Unit] = []
    
    # Trennlinie vorbereiten
    line_length = 60
    
    print(f"{'Zeit (s)':>8} | {'Baut':<25} | {'Metal':>8} | {'Energie':>8} | {'BP':>5}")
    print("-" * line_length)
    
    for code, count in build_order:
        unit = unit_stats[code]
        for _ in range(count):
            # Prerequisite-Check
            for prereq in unit.prerequisites:
                if prereq not in completed_builds:
                    raise ValueError(f"Prerequisite {prereq} muss gebaut sein, bevor {code} gebaut wird.")
            # Ressourcen sofort abziehen
            metal -= unit.metal_cost
            energy -= unit.energy_cost
            
            # Simuliere Bauzeit basierend auf Build-Power
            dt = unit.build_time / build_power
            # laufende Einkommen/Verbrauch während des Bauens
            m_rate = sum(u.metal_rate for u in active_units)
            e_rate = sum(u.energy_rate + u.energy_upkeep for u in active_units)
            metal += m_rate * dt
            energy += e_rate * dt
            
            t += dt
            # Einheit wird als gebaut markiert und aktiviert
            completed_builds.append(code)
            if code == 'armmex' and len([u for u in active_units if u.name=='Metal Extractor']) < len(metal_spot_rates):
                idx = len([u for u in active_units if u.name=='Metal Extractor'])
                mr = metal_spot_rates[idx]
                active_units.append(Unit(unit.name, 0.0, 0.0, 0.0, mr, 0.0, -3.0, unit.build_power, unit.prerequisites))
            else:
                active_units.append(unit)
            # Update der Build-Power
            build_power += unit.build_power
            
            print(f"{t:8.1f} | {unit.name:<25} | {metal:8.1f} | {energy:8.1f} | {build_power:5.1f}")
    
    print("-" * line_length)
    final_m_rate = sum(u.metal_rate for u in active_units)
    final_e_rate = sum(u.energy_rate + u.energy_upkeep for u in active_units)
    print(f"Aktive Einkommen: Metal {final_m_rate:.1f} m/s, Energie {final_e_rate:.1f} e/s, Build-Power {build_power:.1f} BP")

# Beispielaufruf:
if __name__ == "__main__":
    build_order = [
        ('armmex', 3),
        ('armsolar', 3),
        ('armfus', 1),
        ('armgant', 1),
    ]
    metal_spots = [1.8, 1.8, 1.8]
    simulate_build_order(build_order, metal_spots, initial_metal=1000.0, initial_energy=1000.0, initial_build_power=1.0)
