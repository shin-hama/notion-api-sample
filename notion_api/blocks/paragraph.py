from dataclasses import dataclass
from notion_api.blocks.block_element import BlockElement


@dataclass
class Paragraph(BlockElement):
    type: str = "paragraph"
    text: str = ""

    def toDict(self):
        result = super().toDict()
        result[self.type] = {
            "rich_text": [{"type": "text", "text": {"content": self.text}}],
        }
        return result
