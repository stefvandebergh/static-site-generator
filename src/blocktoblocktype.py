from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def block_to_block_type(block:str) -> BlockType:
    if block.startswith("# "):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith("> ") or block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1:3] == ". ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH