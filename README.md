# LangGraph ChatBot

A simple conversational chatbot built using [LangGraph](https://langchain-ai.github.io/langgraph/) and [LangChain OpenAI](https://python.langchain.com/docs/integrations/chat/openai/). This bot maintains conversation history using a memory saver and runs in a terminal loop.

## Features

- **State Management**: Uses `StateGraph` to manage the chat state.
- **Memory**: Implements `MemorySaver` to persist conversation context within a session.
- **OpenAI Integration**: Utilizes `ChatOpenAI` for generating responses.
- **Interactive Loop**: Simple command-line interface for chatting.

## Prerequisites

- Python 3.8+
- OpenAI API Key

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository-url>
   cd Chatbot_LangGraph
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install langgraph langchain-openai langchain-core python-dotenv
   ```

4. **Set up Environment Variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot script:

```bash
python ChatBot.py
```

Type your message and press Enter. To exit the chat, type `exit`, `quit`, or `bye`.

## Visual Flow

```mermaid
graph TD
    Init[Initialize App] --> LoadEnv[Load .env & Setup LLM]
    LoadEnv --> BuildGraph[Build StateGraph]
    BuildGraph --> Compile[Compile with MemorySaver]
    Compile --> InputLoop{User Input Loop}
    InputLoop -->|'exit', 'quit'| Stop[Terminate]
    InputLoop -->|Message| Invoke[Invoke Workflow]
    
    subgraph LangGraph Execution
        Start((START)) --> ChatNode[Chat Node\n(Call OpenAI)]
        ChatNode --> End((END))
    end
    
    Invoke --> Start
    End --> Print[Print Bot Response]
    Print --> InputLoop
```

## Code Structure

- `ChatBot.py`: Main script containing the graph definition, node logic, and execution loop.
