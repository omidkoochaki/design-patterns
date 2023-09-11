from src.memento.document_state import DocumentState


class Document:
    _font_name: str = None
    _font_size: str = None
    _content: str = None

    def create_state(self) -> DocumentState:
        state = DocumentState(self.content, self.font_size, self.font_name)
        return state

    def restore(self, state: DocumentState):
        self.content = state.content
        self.font_size = state.font_size
        self.font_name = state.font_name

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
