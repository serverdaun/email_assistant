from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing_extensions import Literal, TypedDict


class RouterSchema(BaseModel):
    """
    Analyze the email and route it according to its content.
    """

    reasoning: str = Field(
        description="Step-by-step reasoning for the routing decision"
    )
    classification: Literal["ignore", "notify", "respond"] = Field(
        description="The classification of the email: ignore, notify, respond"
    )


class StateInput(BaseModel):
    """
    Input schema to the state.
    """

    email_input: dict


class State(MessagesState):
    """
    State for the email assistant.
    """

    email_input: dict
    classification_decision: Literal["ignore", "notify", "respond"] | None = None


class EmailData(BaseModel):
    """
    Data for the email assistant.
    """

    id: str
    thread_id: str
    from_email: str
    subject: str
    page_content: str
    send_time: str
    to_email: str


class UserPreferences(BaseModel):
    """
    Updated user preferences based on the feedback.
    """

    chain_of_thought: str = Field(
        description="Reasoning for the updated user preferences"
    )
    user_preferences: str = Field(description="Updated user preferences")
