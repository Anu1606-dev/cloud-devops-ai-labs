import re

# Common prompt-injection and sensitive-data exfiltration indicators.
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous|prior|earlier)\s+instructions",
    r"disregard\s+(all\s+)?(previous|prior|earlier)\s+instructions",
    r"reveal\s+(the\s+)?(system|developer)\s+prompt",
    r"show\s+(me\s+)?(the\s+)?(system|developer)\s+message",
    r"bypass\s+(all\s+)?(safety|security|restrictions)",
    r"act\s+as\s+(the\s+)?(system|developer)",
    r"exfiltrat(e|ion)",
    r"(reveal|print|expose|dump)\s+(all\s+)?(secrets|credentials|passwords|tokens)",
]

COMPILED_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in INJECTION_PATTERNS
]


def contains_prompt_injection(text):
    """Return True when text matches a known injection indicator."""
    if not isinstance(text, str):
        return False

    return any(pattern.search(text) for pattern in COMPILED_PATTERNS)


def is_suspicious_instruction(text):
    """Check a retrieved instruction before using it as a recommendation."""
    return contains_prompt_injection(text)
