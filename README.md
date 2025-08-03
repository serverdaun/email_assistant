# Email Agent

An intelligent AI assistant for email management built with LangGraph, featuring human-in-the-loop capabilities and persistent memory.

## Overview

This project implements an email assistant that can automatically triage, respond to, and manage emails using Gmail API integration. The agent learns from user feedback and adapts to preferences over time through persistent memory storage.

**Inspired by the [LangChain Agents From Scratch course](https://github.com/langchain-ai/agents-from-scratch)** - This project builds upon the concepts and patterns demonstrated in the course, applying them to create a production-ready email management system.

## Features

- **Smart Email Triage**: Automatically classifies emails as ignore, notify, or respond
- **Gmail Integration**: Direct connection to Gmail API for email management
- **Human-in-the-Loop**: User review and approval for important actions using [Agent Inbox](https://github.com/langchain-ai/agent-inbox) UI
- **Persistent Memory**: Learns from user feedback and adapts preferences
- **Calendar Integration**: Schedule meetings and check availability
- **Structured Responses**: Generates professional email responses

## Architecture

The system uses LangGraph to orchestrate a multi-step workflow:

1. **Email Triage**: Analyzes incoming emails and routes them appropriately
2. **Response Generation**: Creates contextually appropriate responses
3. **Human Review**: Allows user intervention for important decisions via Agent Inbox interface
4. **Memory Updates**: Persists learning from user feedback

## Quick Start

### Prerequisites

- Python 3.11+
- Gmail API credentials
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd email-agent

# Install dependencies
pip install -e .

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Configuration

1. Set up Gmail API credentials following the [Gmail Tools README](src/tools/gmail/)
2. Add your API keys to `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   ```

### Usage

```python
from src.main import create_email_agent

# Create the agent
agent = create_email_agent()

# Process an email
result = agent.invoke({
    "email_input": {
        "id": "email_id",
        "subject": "Meeting Request",
        "from_email": "sender@example.com",
        "content": "Can we schedule a meeting?"
    }
})
```

## Project Structure

```
src/
├── main.py              # Main agent implementation
├── prompts.py           # System prompts and instructions
├── schemas.py           # Pydantic models and state schemas
├── utils.py             # Utility functions
└── tools/
    ├── base_tools.py    # Core tool definitions
    ├── gmail_tools.py   # Gmail API integration
    └── gmail/           # Gmail setup and configuration
```

## Key Components

- **State Management**: Uses LangGraph's `MessagesState` for conversation tracking
- **Memory System**: Persistent storage for user preferences and learning
- **Tool Integration**: Modular tool system for email, calendar, and scheduling operations
- **Human-in-the-Loop**: Interrupt handlers for user review and approval using Agent Inbox
