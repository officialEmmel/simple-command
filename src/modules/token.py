# Module: token
DESCRIPTION = "Generates a random token"
USAGE = "token"
def main():
    import secrets
    print(secrets.token_urlsafe(32))