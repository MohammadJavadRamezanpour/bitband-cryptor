from utils.constants import PDF_ICON_PATH, VIDEO_ICON_PATH, DEFAULT_ICON_PATH, LOCK_ICON_PATH
from utils.helpers.get_file_extension import get_file_extension
from utils.helpers.is_locked import is_locked

def get_file_icon_path(file_path:str) -> str:
    if is_locked(file_path):
        return LOCK_ICON_PATH

    match get_file_extension(file_path):
        case "jpg" | "jpeg" | "png":
            return file_path
        case "pdf":
            return PDF_ICON_PATH
        case "mp4" | "mkv" | "avi":
            return VIDEO_ICON_PATH
        case _:
            return DEFAULT_ICON_PATH
        