import os
from mdtohtmlnode import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown document")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    htmlstring = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Content }}", htmlstring)
    template = template.replace("{{ Title }}", title)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w") as f:
        f.write(template)

def generate_page_r(dir_path_content, template_path, dir_path_dest, basepath):
    print(f"Generating pages in {dir_path_content} using {template_path}")
    for item in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dir_path_dest, item)
        if content_path.endswith(".md") and os.path.isfile(content_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(content_path, template_path, dest_path, basepath)
        else:
            os.mkdir(dest_path)
            generate_page_r(content_path, template_path, dest_path, basepath)