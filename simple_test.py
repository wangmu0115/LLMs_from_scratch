import re
from pathlib import Path


def tokenizing(text: str) -> list[str]:
    result = re.split(r"([,.:;?_!\"()']|--|\s)", text)
    return [item.strip() for item in result if item.strip()]


test_sentences = [
    "Hello, world. This, is a test.",
    "Hello, world. Is this-- a test?",
]

for sentence in test_sentences:
    print(tokenizing(sentence))

with open(Path("./the-verdict.txt"), "r", encoding="utf_8") as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))
print(raw_text[:99])

preprocessed = tokenizing(raw_text)
print(len(preprocessed))
print(preprocessed[:30])


all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)
vocab = {word: index for index, word in enumerate(all_words)}
# for item, i in vocab.items():
#     print(f"{item}: {i}")
#     if i >= 50:
#         break
