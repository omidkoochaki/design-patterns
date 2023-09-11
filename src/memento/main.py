from memento.document import Document
from memento.history import History

hist = History()

doc = Document()
doc.content = 'c1'
doc.font_size = 'fs1'
doc.font_name = 'fn1'
hist.push(doc.create_state())

doc.content = 'c2'
doc.font_size = 'fs2'
doc.font_name = 'fn2'
hist.push(doc.create_state())

doc.content = 'c3'
doc.font_size = 'fs3'
doc.font_name = 'fn3'

print('Before Restore: ', doc.content, doc.font_name, doc.font_size)
doc.restore(hist.pop())
print('After Restore: ', doc.content, doc.font_name, doc.font_size)
