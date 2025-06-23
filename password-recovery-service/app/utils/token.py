import secrets

def generate_token(email: str):
    return secrets.token_urlsafe(32)
