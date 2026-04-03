import re


# This function takes raw markdown text and returns
# a list of tuples. Each tuple contains the alt text
# and URL of any  markdown images found in the text.
def extract_markdown_images(markdown_text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown_text)
    return matches

# This function does the same as the above function, 
# but for markdown links instead of images.
def extract_markdown_links(markdown_text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", markdown_text)
    return matches
