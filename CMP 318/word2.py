from docx import Document

# Open an existing Word document
doc = Document('example.docx')

# Read and print the content
for paragraph in doc.paragraphs:
    print(paragraph.text)
