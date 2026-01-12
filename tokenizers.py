import re
from typing import Sequence


class SimpleTokenizer:
    def __init__(self, vocab: dict[str, int]):
        self.str_to_int = vocab
        self.int_to_str = {index: item for item, index in vocab.items()}

    def encode(self, text: str) -> list[int]:
        """Splits text into tokens and carries out the string-to-integer mapping to
        produce token IDs via the vocabulary.
        """
        tokens = re.split(r"([,.:;?_!\"()']|--|\s)", text)
        tokens = [token.strip() for token in tokens if token.strip()]  # Remove whitespace
        token_ids = [self.str_to_int[token] for token in tokens]
        return token_ids

    def decode(self, ids: Sequence[int]) -> str:
        """Carries out the reverse integer-to-string mapping to convert the token IDs back into text"""
        text = " ".join(self.int_to_str[id] for id in ids)
        text = re.sub(r"\s+([,.?!\"()'])", r"\1", text)
        return text


if __name__ == "__main__":
    from pathlib import Path

    with open(Path("./the-verdict.txt"), "r", encoding="utf_8") as f:
        raw_text = f.read()
    preprocessed = re.split(r"([,.:;?_!\"()']|--|\s)", raw_text)
    preprocessed = [s.strip() for s in preprocessed if s.strip()]
    vocab = {item: index for index, item in enumerate(sorted(set(preprocessed)))}

    tokenizer = SimpleTokenizer(vocab)
    text = """"It's the last he painted, you know,"
           Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(text)
    print(len(ids))
    print(ids)
    print(tokenizer.decode(ids))
