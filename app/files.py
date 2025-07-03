import csv
from pathlib import Path

rows = [
    ("Name", "Score"),
    ("Ali", "95"),
    ("Ahmed", "40"),
]

# with open("data/exm.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)


home_dir = Path.home()/ "/workspaces/Python-Avengers/data/note.txt"
text = home_dir.write_text("hello", encoding="utf-8")

