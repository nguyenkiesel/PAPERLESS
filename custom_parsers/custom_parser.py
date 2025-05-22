import custom.mime_patch  # 👈 ensures patch is applied at runtime
from paperless.parsers import DocumentParser

class AnyFileParser(DocumentParser):
    def parse(self):
        self.content = ""  # No OCR
        self.title = self.filename
        return True

    def get_thumbnail(self):
        return None  # Skip thumbnail for now
