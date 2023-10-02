import os

SIGNATURE = "__MJ Lock__"

ASSETS_PATH = "assets"

TEMPLATES_PATH = os.path.join(ASSETS_PATH, "templates")
CRYPTOR_TEMPLATE = os.path.join(TEMPLATES_PATH, "cryptor.ui")
ENCRYPT_TEMPLATE = os.path.join(TEMPLATES_PATH, "encrypt_set_password.ui")
DECRYPT_TEMPLATE = os.path.join(TEMPLATES_PATH, "decrypt_set_password.ui")

VIDEO_ICON = os.path.join(ASSETS_PATH, "icons", "video1.png")
PDF_ICON = os.path.join(ASSETS_PATH, "icons", "pdf.png")
LOCK_ICON = os.path.join(ASSETS_PATH, "icons", "lock.png")
DEFAULT_ICON = os.path.join(ASSETS_PATH, "icons", "default.png")
