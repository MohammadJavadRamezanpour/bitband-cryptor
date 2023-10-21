import os

SIGNATURE = "__MJ LOCK__"

ASSETS_PATH = "assets"

ICONS_PATH = os.path.join(ASSETS_PATH, "icons")
PDF_ICON_PATH = os.path.join(ICONS_PATH, "pdf.png")
DEFAULT_ICON_PATH = os.path.join(ICONS_PATH, "default.png")
VIDEO_ICON_PATH = os.path.join(ICONS_PATH, "video1.png")
LOCK_ICON_PATH = os.path.join(ICONS_PATH, "lock.png")

TEMPLATES_ADDRESS = os.path.join(ASSETS_PATH, "templates")
CRYPTOR_TEMPLATE_ADDRESS = os.path.join(TEMPLATES_ADDRESS, "cryptor.ui")
ENCRYPT_TEMPLATE_ADDRESS = os.path.join(TEMPLATES_ADDRESS, "encrypt.ui")
DECRYPT_TEMPLATE_ADDRESS = os.path.join(TEMPLATES_ADDRESS, "decrypt.ui")

