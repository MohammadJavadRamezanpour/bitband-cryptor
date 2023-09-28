from utils.constants import PDF_ICON, VIDEO_ICON, DEFAULT_ICON

def get_file_extension(file_name):
    return file_name.split(".")[-1]

def get_file_icon(file_name):
    match get_file_extension(file_name):
        case "jpg" | "png" | "jpeg":
            return file_name
        case "mp4" | "avi" | "mkv":
            return VIDEO_ICON
        case "pdf":
            return PDF_ICON
        case _:
            return DEFAULT_ICON