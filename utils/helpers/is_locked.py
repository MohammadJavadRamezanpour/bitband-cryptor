from utils.constants import SIGNATURE

def is_locked(file_name):
    with open(file_name, "rb") as file:
        content = file.read()
        return content.endswith(SIGNATURE.encode())