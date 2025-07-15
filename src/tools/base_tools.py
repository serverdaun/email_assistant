from typing import Literal
from pydantic import BaseModel
from langchain_core.tools import tool

from gmail_tools import (
    fetch_emails_tool,
    send_email_tool,
    check_calendar_tool,
    schedule_meeting_tool
)


@tool
def triage_tool(category: Literal["ignore", "notify", "respond"]) -> str:
    """
    Triage the user's request into a category.
    - ignore: The user's request is not important and can be ignored.
    - notify: The user's request is important and should be notified.
    - respond: The user's request is important and should be responded to.
    """
    return category

@tool
class Done(BaseModel):
    """
    E-mail has been sent.
    """
    done: bool

@tool
class Question(BaseModel):
    """
    Question to ask the user.
    """
    content: str


def get_tools() -> list[tool]:
    """
    Get the tools for the email assistant.
    """
    return [triage_tool, Done, Question, fetch_emails_tool, send_email_tool, check_calendar_tool, schedule_meeting_tool]
