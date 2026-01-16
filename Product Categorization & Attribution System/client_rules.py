import re

CLIENT_RULES = {
    "Client_A": {
        "Energy Drinks": [r"\benergy drink\b", r"\bred bull\b"],
        "Soft Drinks": [r"\bsoft drink\b", r"\bcola\b"],
        "Protein Snacks": [r"\bprotein bar\b", r"\bprotein snack\b"],
        "Tea & Coffee": [r"\btea\b"]
    },
    "Client_B": {
        "Functional Beverages": [r"\benergy drink\b"],
        "Snacks": [r"\bprotein bar\b"],
        "Hot Beverages": [r"\btea\b", r"\bcoffee\b"]
    }
}

def client_rule_tag(text, client):
    rules = CLIENT_RULES.get(client, {})
    for category, patterns in rules.items():
        for pattern in patterns:
            if re.search(pattern, text):
                return category
    return None
