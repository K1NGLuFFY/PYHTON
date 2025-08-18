# AI Chatbot - Python Implementation

A simple yet effective AI chatbot built with Python using natural language processing techniques.

## Features

- **Natural Language Processing**: Uses NLTK for text preprocessing and understanding
- **Intent Recognition**: Matches user input to predefined intents using similarity scoring
- **Context Awareness**: Maintains conversation history for better responses
- **Extensible**: Easy to add new intents and responses
- **Command Interface**: Built-in commands for help, history, and clearing context

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Chatbot**:
   ```bash
   python main.py
   ```

## Usage

### Starting the Chatbot
```bash
python main.py
```

### Available Commands
- `help` - Show available commands
- `history` - View recent conversation
- `clear` - Clear conversation history
- `quit`, `exit`, `bye` - Exit the chatbot

### Example Conversation
```
🤖 AI CHATBOT
================
Hello! I'm your AI assistant.
Type 'help' for available commands
Type 'quit' or 'exit' to leave
================

You: Hello
Bot: Hello! How can I help you today?

You: Tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything!

You: What's your name?
Bot: I'm an AI chatbot created to help you with various questions and tasks.

You: history
RECENT CONVERSATION:
  1. You: Hello
     Bot: Hello! How can I help you today?
  2. You: Tell me a joke
     Bot: Why don't scientists trust atoms? Because they make up everything!
  3. You: What's your name?
     Bot: I'm an AI chatbot created to help you with various questions and tasks.
```

## Project Structure

```
ai_chatbot/
├── main.py          # Entry point and CLI interface
├── chatbot.py       # Core chatbot logic
├── intents.json     # Training data and responses
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Adding New Intents

To add new intents, edit the `intents.json` file:

```json
{
  "tag": "new_intent",
  "patterns": ["pattern1", "pattern2"],
  "responses": ["response1", "response2"]
}
```

## Technical Details

- **Text Preprocessing**: Tokenization, lemmatization, stopword removal
- **Similarity Matching**: Jaccard similarity for intent recognition
- **Response Selection**: Random selection from matched intent responses
- **Context Management**: Stores last 5 conversation turns

## Future Enhancements

- Machine learning model integration
- Real-time API integration (weather, news, etc.)
- Voice input/output support
- Database for persistent conversation history
- Multi-language support
- Web interface using Flask/Django

## Troubleshooting

### NLTK Data Download Issues
If you encounter NLTK data download issues, run:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Permission Issues
On some systems, you might need to run:
```bash
python -m nltk.downloader punkt stopwords wordnet
```

## License
This project is open source and available under the MIT License.
