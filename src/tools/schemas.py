from typing import List, Optional

from pydantic import BaseModel, Field


class FetchEmailsInput(BaseModel):
    """
    Input schema for the fetch_emails_tool.
    """

    email_address: str = Field(description="Email address to fetch emails for")
    minutes_since: int = Field(
        default=30, description="Only retrieve emails newer than this many minutes"
    )


class SendEmailInput(BaseModel):
    """
    Input schema for the send_email_tool.
    """

    email_id: str = Field(
        description="Gmail message ID to reply to. This must be a valid Gmail message ID obtained from the fetch_emails_tool. If you're creating a new email (not replying), you can use any string like 'NEW_EMAIL'."
    )
    response_text: str = Field(description="Content of the reply")
    email_address: str = Field(description="Current user's email address")
    additional_recipients: Optional[List[str]] = Field(
        default=None, description="Optional additional recipients to include"
    )


class CheckCalendarInput(BaseModel):
    """
    Input schema for the check_calendar_tool.
    """

    dates: List[str] = Field(description="List of dates to check in DD-MM-YYYY format")


class ScheduleMeetingInput(BaseModel):
    """
    Input schema for the schedule_meeting_tool.
    """

    attendees: List[str] = Field(description="Email addresses of meeting attendees")
    title: str = Field(description="Meeting title/subject")
    start_time: str = Field(
        description="Meeting start time in ISO format (YYYY-MM-DDTHH:MM:SS)"
    )
    end_time: str = Field(
        description="Meeting end time in ISO format (YYYY-MM-DDTHH:MM:SS)"
    )
    organizer_email: str = Field(description="Email address of the meeting organizer")
    timezone: str = Field(
        default="Europe/Prague", description="Timezone for the meeting"
    )
