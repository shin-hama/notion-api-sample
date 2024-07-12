# Imports the Google Cloud client library
from dataclasses import dataclass
from typing import Iterator
from google.cloud import vision


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Block:
    vertices: list[Point]


@dataclass
class DetectionResult:
    box: Block
    text: str


def detect_document(path) -> Iterator[DetectionResult]:
    """Detects document features in an image."""
    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    client = vision.ImageAnnotatorClient()
    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            word_text = ""
            for paragraph in block.paragraphs:
                word = "".join(
                    [symbol.text for word in paragraph.words for symbol in word.symbols]
                )
                word_text += f"{word}\n"

            yield DetectionResult(
                box=Block(
                    vertices=[
                        Point(vertex.x, vertex.y)
                        for vertex in block.bounding_box.vertices
                    ]
                ),
                text=word_text,
            )
