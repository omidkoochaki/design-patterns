from src.memento.document_state import DocumentState


class History:
    _list_of_document_states: [DocumentState] = []

    def push(self, state: DocumentState):
        self._list_of_document_states.append(state)

    def pop(self):
        return self._list_of_document_states.pop()