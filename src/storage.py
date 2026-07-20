import csv
from pathlib import Path

def save_csv(filename, rows):
    if not rows:
        return
    
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = rows[0].keys()

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
