import base64

def fit_key(key):
    if len(key) != 32:
        remainig_lenght = 32 - len(key)
        if remainig_lenght > 0:
            key += b"a" * remainig_lenght
        else:
            key = key[:32]
    return base64.urlsafe_b64encode(key)