# Format der Datei `unit_data.json`

Die Datei `unit_data.json` enthält eine JSON-Struktur mit Objekt-Einträgen für jede Unit. Der Schlüssel ist der `unit_code` (z. B. `legmex`). Jeder Eintrag ist ein Objekt mit folgenden Feldern:

- **name**: Menschlich lesbarer Name der Einheit (String)
- **metal_cost**: Metall-Kosten zum Bau (Float)
- **energy_cost**: Energie-Kosten zum Bau (Float)
- **build_time**: Basis-Bauzeit in Sekunden (Float)
- **metal_rate**: Metall-Produktion m/s nach Fertigstellung (Float)
- **energy_rate**: Energie-Produktion e/s nach Fertigstellung (Float)
- **energy_upkeep**: Netto-Energie-Verbrauch e/s nach Fertigstellung (Float, negativ = Verbrauch)
- **build_power**: Build-Power BP, die nach Fertigstellung zum Verkürzen zukünftiger Bauzeiten beiträgt (Float)
- **prerequisites**: Liste von `unit_code`s (Strings), die vor diesem Bau fertiggestellt sein müssen

```json
{
  "legmex": {
    "name": "Metal Extractor",
    "metal_cost": 50.0,
    "energy_cost": 500.0,
    "build_time": 18.0,
    "metal_rate": 0.0,
    "energy_rate": 0.0,
    "energy_upkeep": -3.0,
    "build_power": 0.0,
    "prerequisites": []
  },
  ...
}
```
