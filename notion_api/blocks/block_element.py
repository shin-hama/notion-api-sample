from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class BlockElement(ABC):
    type: str

    @abstractmethod
    def toDict(self):
        result: dict[str, object] = {"type": self.type, "object": "block"}
        return result


@dataclass
class BlockElementWithChildren(BlockElement):
    children: list[BlockElement] = field(default_factory=list)

    def AddChild(self, child: BlockElement):
        self.children.append(child)

    @abstractmethod
    def toDict(self):
        result = super().toDict()
        result[self.type] = {"children": [child.toDict() for child in self.children]}
        return result
