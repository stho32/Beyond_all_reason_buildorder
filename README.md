# Beyond_all_reason_buildorder

## 1. Zielsetzung  
- Automatische Ermittlung der zeit­optimalen Build‑Order, um eine vordefinierte Menge von Einheiten auf dem Schlachtfeld zu haben (z. B. T3‑Werft, Fusionsreaktor etc.).  
- Minimale Aggressivität, Fokus auf schnelle Skalierung bis Tech‑Level 3.  
- Berücksichtigung variabler Metall‑Spot‑Raten, Build‑Power und Tech‑Abhängigkeiten.  

## 2. Funktionale Anforderungen  
1. **Zieldefinition**  
   - Variable `target_units: List[Tuple[str, int]]` definiert am Skriptanfang die Einheitencodes und -anzahlen, die am Ende aktiv sein sollen.  
2. **Ressourcen­spots**  
   - Variable `metal_spots: List[float]` enthält Metallraten (m/s) für T1‑Extractoren in der Reihenfolge der Spots.  
3. **Einheiten­daten**  
   - `unit_stats: Dict[str, UnitSpec]` mit für jede Einheit:  
     - Code (z. B. `armmex`, `armcon`)  
     - Metall‑ und Energie‑Kosten  
     - Basis‑Bauzeit (s)  
     - Metall‑ und Energie‑Produktion bzw. -Verbrauch (m/s, e/s)  
     - Build‑Power (BP) zur Beschleunigung von Bauprojekten  
     - Prerequisites: Liste von Einheitencodes, die vorab gebaut sein müssen  
4. **Tech‑Abhängigkeiten**  
   - Vor dem Baubeginn prüft das Skript für jede Einheit, ob alle `prerequisites` im aktuellen Status erfüllt sind.  
5. **Initial­ressourcen**  
   - `initial_metal: float`, `initial_energy: float` (Default z. B. 1000)  
   - `initial_build_power: float` (Player-Basis, Default 1.0 BP)  
6. **Ressourcensimulation**  
   - Dynamische Simulation von Metall-, Energie- und Build‑Power‑Pools während des Baus.  
   - Einkommen aus aktiven Extractoren/Kraftwerken, Upkeep‑Kosten, BP‑Zuwächse durch Bots.  
7. **Optimierungs­algorithmus**  
   - Findet die Reihenfolge, die alle `target_units` am schnellsten fertigstellt.  
   - Vorschläge: Backtracking mit Greedy‑Pruning, A*‑Suche im Zustandsraum.  

## 3. Nicht‑funktionale Anforderungen  
- **Erweiterbarkeit:** Neue Einheiten-/Fabrik-Daten leicht ergänzbar.  
- **Lesbarkeit & Wartbarkeit:** Klare Trennung von Daten, Simulation und Optimierung.  
- **Performanz:** Akzeptable Laufzeit für Szenarien mit ~5–10 Ziel­einheiten.  

## 4. Eingaben  
- `target_units: List[Tuple[str, int]]`  
- `metal_spots: List[float]`  
- `initial_metal: float` (optional)  
- `initial_energy: float` (optional)  
- `initial_build_power: float` (optional)  
- `unit_stats: Dict[str, UnitSpec]` (inkl. `prerequisites`, `build_power`)  

## 5. Ausgabe  
- Abfolge von `(fertigstellungszeitpunkt, unit_code)`  
- Ressourcen‑Verlauf und Endraten für Metall, Energie, Build‑Power  
- Optional: Export als Text oder CSV  

## 6. Weiterführende Überlegungen  
- Visualisierung (Plot) von Metall/Energie/BP über Zeit  
- Szenarien­import/-export via JSON/YAML  
- Unterstützung unterschiedlicher Build‑Power‑Modi (z. B. 100 vs. 200 Base BP)  

## Projekt-Fraktion  
- Aktuelle Fraktion: Arm
