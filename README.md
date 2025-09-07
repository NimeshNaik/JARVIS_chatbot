# JARVIS Chatbot

A conversational AI assistant inspired by JARVIS from Iron Man, built with Gradio and powered by Groq's API using the OpenAI GPT-OSS-120B model.

## Features

- **JARVIS Personality**: Witty, intelligent, and slightly sarcastic responses in the style of Tony Stark's AI assistant
- **Interactive Web Interface**: Clean and modern chat interface built with Gradio
- **High-Performance AI**: Powered by Groq's fast inference with OpenAI's GPT-OSS-120B model
- **Conversation Memory**: Maintains context throughout the conversation
- **Professional Tone**: Balances helpfulness with JARVIS's characteristic confidence and humor

## Prerequisites

- Python 3.7 or higher
- Groq API key (sign up at [console.groq.com](https://console.groq.com))

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Groq API key as an environment variable:
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   ```
   
   Or on Windows:
   ```cmd
   set GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://127.0.0.1:7860`)

3. Start chatting with JARVIS! Try asking questions like:
   - "What's the weather like today?"
   - "Help me write a Python function"
   - "Tell me a joke"
   - "What's your opinion on AI?"

## Project Structure

```
JARVIS_chatbot/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Configuration

The chatbot can be customized by modifying the system prompt in `app.py`:

```python
"content": "You are JARVIS, the witty and highly intelligent AI assistant from Iron Man..."
```

You can adjust:
- **Temperature** (line 31): Controls response creativity (0.0-1.0)
- **Max tokens** (line 30): Maximum response length
- **Model** (line 28): Currently using `openai/gpt-oss-120b`

## Dependencies

- **gradio**: Web interface framework
- **groq**: Python client for Groq API
- **httpx**: HTTP client library

## API Usage

This application uses the Groq API, which provides:
- Fast inference speeds
- Access to various open-source models
- Competitive pricing
- High reliability

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `GROQ_API_KEY` environment variable is set correctly
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: If port 7860 is busy, Gradio will automatically use the next available port

### Getting Help

- Check the [Groq documentation](https://console.groq.com/docs) for API-related issues
- Visit the [Gradio documentation](https://gradio.app/docs/) for interface customization
- Ensure your Python version is 3.7 or higher

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the JARVIS chatbot!

---

*"Sometimes you gotta run before you can walk."* - Tony Stark

Enjoy chatting with your very own JARVIS assistant! 🤖✨
