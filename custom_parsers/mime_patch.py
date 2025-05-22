from paperless.consumer import consumers

# Backup original
_original_supported = consumers.Consumer._is_supported_mimetype

# Patch it
def _patched_supported_mimetype(cls, mimetype):
    # You can whitelist only specific types, or allow all
    allowed = [
        "video/mp4",
        "video/mkv",
        "application/zip",
        "application/octet-stream",
        # Add more types if needed
    ]
    return True if mimetype in allowed else _original_supported(cls, mimetype)

# Apply patch
consumers.Consumer._is_supported_mimetype = classmethod(_patched_supported_mimetype)
