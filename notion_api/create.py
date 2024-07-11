import os
from pprint import pprint

from dotenv import load_dotenv
from notion_client import Client

from notion_api.blocks.clumn import ColumnList
from notion_api.blocks.paragraph import Paragraph


load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])

p1 = Paragraph(text="column 1")
p2 = Paragraph(text="column 2")
p3 = Paragraph(text="spanning column 1 and 2")
columns = ColumnList([p1, p2])

page = notion.pages.create(
    parent={"database_id": os.environ["DATABASE_ID"]},
    properties={
        "Name": {"title": [{"text": {"content": "Alice2"}}]},
    },
    children=[
        columns.toDict(),
        p3.toDict(),
    ],
)

pprint(page)
