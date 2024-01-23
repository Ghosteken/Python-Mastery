from docx import Document

# Open an existing Word document
doc = Document('example.docx')

# Update the content
for paragraph in doc.paragraphs:
    if 'sample document' in paragraph.text.lower():
        paragraph.text = 'This document has been updated with python-docx.'

# Save the updated document
doc.save('updated_example.docx')
