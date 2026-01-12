from pathlib import Path

import httpx

url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"

resp = httpx.get(url)

with open(Path("./the-verdict.txt"), "w", encoding="utf_8") as f:
    f.write(resp.text)
