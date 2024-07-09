import os
from pprint import pprint

from dotenv import load_dotenv
from notion_client import Client


load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])

page = notion.pages.create(
    parent={"database_id": os.environ["DATABASE_ID"]},
    properties={
        "Name": {"title": [{"text": {"content": "Alice"}}]},
    },
    children=[
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "Hello"}}]
            },
        }
    ],
)

pprint(page)
