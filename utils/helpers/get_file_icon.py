from utils.constants import PDF_ICON, LOCK_ICON, VIDEO_ICON, DEFAULT_ICON
from .is_locked import is_locked
from .get_file_extension import get_file_extension

def get_file_icon(file_name):
    if is_locked(file_name):
        return LOCK_ICON
    
    match get_file_extension(file_name):
        case "jpg" | "png" | "jpeg":
            return file_name
        case "mp4" | "avi" | "mkv":
            return VIDEO_ICON
        case "pdf":
            return PDF_ICON
        case _:
            return DEFAULT_ICON