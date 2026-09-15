"""Text normalization helpers for LLM output comparison."""

_CURLY_REPLACEMENTS = {
    "\u2019": "'",   # right single quote
    "\u2018": "'",   # left single quote
    "\u201c": '"',   # left double quote
    "\u201d": '"',   # right double quote
    "\u2013": "-",   # en dash
    "\u2014": "-",   # em dash
    "\u00a0": " ",   # non-breaking space
}


def normalize(text: str) -> str:
    """Normalize LLM output for reliable comparison.

    LLMs often emit curly quotes and typographic dashes. Convert them
    to ASCII equivalents, lowercase, and strip surrounding whitespace.
    """
    for curly, straight in _CURLY_REPLACEMENTS.items():
        text = text.replace(curly, straight)
    return text.lower().strip()