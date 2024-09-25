# Task: Last4
# Hide the credit card number, display only last 4 digits

# Example Input:
# 1234123456789989
# Example Output:
# ************9989

# Example Input:
# 789989
# Example Output:
# **9989


CREDIT_CARD_LENGTH = 16
SHOWN_WILDCARD = 4


def last4_challenge(s: str | list[str]) -> str:
    if len(s) < CREDIT_CARD_LENGTH:
        raise ValueError("Credit card length is incorrect")

    masked = '*' * (len(s) - SHOWN_WILDCARD)
    shown = s[len(s) - SHOWN_WILDCARD:]
    return masked + shown


print(last4_challenge("1234123456789989"))
print(last4_challenge("1234123456789989".split()))

