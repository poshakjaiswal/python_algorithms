from mailmerge import MailMerge
from datetime import date

# Define the templates - assumes they are in the same directory as the code
template_1 = "input.docx"

# Show a simple example
document_1 = MailMerge(template_1)

print("Fields included in {}: {}".format(template_1, document_1.get_merge_fields()))

document_1.merge(
    namee='Gold')

# Save the document as example 1
document_1.write('example1.docx')