import os.path
import sys
import markdown
import pdfkit
import yaml

content_dir = "/mnt/content/"
default_dir = "/mnt/default/"

COVER_FILE = "cover.html"
TOC_FILE = "toc.xsl"
HEADER_FILE = "header.html"
FOOTER_FILE = "footer.html"
CONF_FILE = "conf.yaml"

allowed_extensions = (".md", ".html", ".xsl", ".yaml")

files = sorted([os.path.join(content_dir, file)
                for file in os.listdir(content_dir)
                if os.path.isfile(os.path.join(content_dir, file)) and (file.endswith(allowed_extensions))])

default_files = sorted([os.path.join(default_dir, file)
                        for file in os.listdir(default_dir)
                        if os.path.isfile(os.path.join(default_dir, file)) and (file.endswith(allowed_extensions))])


def get_reserved_file(reserved_file):
    file = os.path.join(content_dir, reserved_file)
    if file not in files:
        file = os.path.join(default_dir, reserved_file)
        if file not in default_files:
            return None
    else:
        files.remove(file)

    print(f"Found \"{reserved_file}\"")
    return file


cover = get_reserved_file(COVER_FILE)
toc = get_reserved_file(TOC_FILE)
header = get_reserved_file(HEADER_FILE)
footer = get_reserved_file(FOOTER_FILE)
conf_file = get_reserved_file(CONF_FILE)

if not conf_file:
    conf_file = os.path.join("./", CONF_FILE)

if not toc:
    toc = os.path.join("./", TOC_FILE)

full_md = ""
for file_name in files:
    print(f"Reading file \"{file_name}\"")
    full_md += open(file_name, "r").read()
    full_md += "\n"

print(f"\nLoading configs from \"{conf_file}\"")
conf = {}
with open(conf_file, 'r') as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

options = conf['options']

if 'header-html' not in options and header:
    print("\nAdding \"header-html\" to options")
    options['header-html'] = header

if 'footer-html' not in options and footer:
    print("\nAdding \"footer-html\" to options")
    options['footer-html'] = footer

toc_dict = conf['toc']

if 'xsl-style-sheet' not in toc_dict and toc:
    print("\nAdding \"xsl-style-sheet\" to toc")
    toc_dict['xsl-style-sheet'] = toc

print("\nConverting content to HTML\n")
html = markdown.markdown(full_md)


print("Converting HTML to PDF.\n")

output_name = sys.argv[1]
output_file = os.path.join(content_dir, output_name)
if os.path.exists(output_file):
    print(f"Removing old output file \"{output_name}\"\n")
    os.remove(output_file)

if not cover:
    pdfkit.from_string(html, output_file, options, verbose=True, toc=toc_dict)
else:
    pdfkit.from_string(html, output_file, options, verbose=True, cover_first=True, cover=cover, toc=toc_dict)

print("HTML converted to PDF.")
