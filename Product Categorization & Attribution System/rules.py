import re

RULES = {
    "Energy Drinks": [r"\benergy drink\b", r"\bred bull\b"],
    "Soft Drinks": [r"\bsoft drink\b", r"\bcola\b"],
    "Protein Snacks": [r"\bprotein bar\b", r"\bprotein snack\b", r"\bhigh protein\b"],
    "Tea & Coffee": [r"\bgreen tea\b", r"\btea bags\b", r"\btea\b"]
}

def rule_based_tag(text):
    for category, patterns in RULES.items():
        for pattern in patterns:
            if re.search(pattern, text):
                return category
    return None
