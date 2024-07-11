from dataclasses import dataclass
from typing import Union
from notion_api.blocks.block_element import BlockElement, BlockElementWithChildren


@dataclass
class Column(BlockElementWithChildren):
    type: str = "column"

    def __init__(self, children: Union[list[BlockElement], BlockElement, None] = None):
        super().__init__(type=self.type)
        if children is not None:
            if isinstance(children, list):
                self.children = children
            else:
                self.children = [children]

    def toDict(self):
        result = super().toDict()
        return result


@dataclass
class ColumnList(BlockElementWithChildren):
    type: str = "column_list"

    def __init__(self, children: Union[list[BlockElement], BlockElement, None] = None):
        super().__init__(type=self.type)
        if children is not None:
            if isinstance(children, list):
                self.children = [self._wrap_in_column(item) for item in children]
            else:
                self.children = [self._wrap_in_column(children)]

    def AddChild(self, child: Union[Column, BlockElement]):
        wrapped_child = self._wrap_in_column(child)
        super().AddChild(wrapped_child)

    def _wrap_in_column(self, element: Union[Column, BlockElement]) -> Column:
        if isinstance(element, Column):
            return element
        return Column(element)

    def toDict(self):
        result = super().toDict()
        return result
