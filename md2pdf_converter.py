import os
import sys
import markdown
import pdfkit

dir_name = "/mnt/temp/"

list_of_files = sorted([os.path.join(dir_name, file) for file in os.listdir(dir_name)
                        if os.path.isfile(os.path.join(dir_name, file)) and file.endswith(".md")])

print(f"Reading MD files: {list_of_files}.")
full_md = "\n".join([open(file_name, "r").read() for file_name in list_of_files])

print("Converting content to HTML.")
html = f'<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>{markdown.markdown(full_md)}<body></html>'

output_name = sys.argv[1]
output_file = os.path.join(dir_name, output_name)

if os.path.exists(output_file):
    print(f"Removing old output file [{output_name}].")
    os.remove(output_file)

print(f"Convering HTML to PDF.")
pdfkit.from_string(html, output_file)
