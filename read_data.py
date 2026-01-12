from pathlib import Path

with open(Path("./the-verdict.txt"), "r", encoding="utf_8") as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))
print(raw_text[:99])
