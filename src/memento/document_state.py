class DocumentState:
    _content: str = None
    _font_name: str = None
    _font_size: str = None

    def __init__(self, content, font_size, font_name):
        self.content = content
        self.font_size = font_size
        self.font_name = font_name

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        if self._font_size is None:  # to prevent changing state accidentally
            self._font_size = value

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        if self._font_name is None:
            self._font_name = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if self._content is None:
            self._content = value
