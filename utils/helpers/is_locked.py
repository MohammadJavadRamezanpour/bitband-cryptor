from utils.constants import SIGNATURE

def is_locked(file_path):
    with open(file_path, "rb") as file:
        return file.read().endswith(SIGNATURE.encode())
