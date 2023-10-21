import base64

def fit_key(key:str) -> bytes:
    if len(key) != 32:
        remaing_length = 32 - len(key)
        if remaing_length > 0:
            key += b'a' * remaing_length
        else:
            key = key[:32]
    return base64.urlsafe_b64encode(key)