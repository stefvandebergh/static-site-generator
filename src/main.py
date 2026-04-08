import sys
from textnode import TextNode
from copystatictopublic import copy_static_to_public
from generatepage import generate_page_r

def main():
    basepath =sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static_to_public("static", "docs")
    generate_page_r("content/", "template.html", "docs/", basepath)


if __name__ == "__main__":
    main()