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


# Sensitive-data patterns. These target common credential formats.
SENSITIVE_PATTERNS = [
    (
        re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
        "[REDACTED_AWS_ACCESS_KEY]"
    ),
    (
        re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]+", re.IGNORECASE),
        "Bearer [REDACTED]"
    ),
    (
        re.compile(
            r"\beyJ[A-Za-z0-9_-]{10,}\."
            r"[A-Za-z0-9_-]{10,}\."
            r"[A-Za-z0-9_-]{5,}\b"
        ),
        "[REDACTED_JWT]"
    ),
    (
        re.compile(
            r"\b(password|passwd|api[_-]?key|secret|access[_-]?token|"
            r"auth[_-]?token|client[_-]?secret)\b"
            r"(\s*[:=]\s*)"
            r'(?:"[^"]*"|\'[^\']*\'|[^\s,;]+)',
            re.IGNORECASE
        ),
        r"\1\2[REDACTED]"
    ),
]


def redact_sensitive_data(text):
    """Redact common credentials while preserving surrounding text."""
    if not isinstance(text, str):
        return text

    redacted = text

    for pattern, replacement in SENSITIVE_PATTERNS:
        redacted = pattern.sub(replacement, redacted)

    return redacted
