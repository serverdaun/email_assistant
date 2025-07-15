from typing import Dict, Literal, Optional

from langchain_core.tools import BaseTool, tool
from pydantic import BaseModel

from src.tools.gmail_tools import (
    check_calendar_tool,
    fetch_emails_tool,
    schedule_meeting_tool,
    send_email_tool,
)


# Base tools for agent
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


# Helper functions
def get_tools() -> list[BaseTool]:
    """
    Get the tools for the email assistant.
    """
    return [
        triage_tool,
        Done,
        Question,
        fetch_emails_tool,
        send_email_tool,
        check_calendar_tool,
        schedule_meeting_tool,
    ]


def get_tools_by_name(tools: Optional[list[BaseTool]] = None) -> Dict[str, BaseTool]:
    """
    Get the tools by name.
    """
    return {tool.name: tool for tool in tools}
