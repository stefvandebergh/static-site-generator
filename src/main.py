from textnode import TextNode
from copystatictopublic import copy_static_to_public
from generatepage import generate_page_r

def main():
    copy_static_to_public("static", "public")
    generate_page_r("content/", "template.html", "public/")


if __name__ == "__main__":
    main()