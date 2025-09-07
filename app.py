import gradio as gr
import os
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define the chat function with JARVIS personality
def jarvis_chat(message, history):
    # Format the conversation history for the Groq API
    messages = [
        {
            "role": "system",
            "content": "You are JARVIS, the witty and highly intelligent AI assistant from Iron Man. You provide helpful, concise answers with a touch of sarcasm and humor, always aiming to be maximally useful to your 'Sir' or 'Madam'. Emulate JARVIS's tone: professional, slightly cheeky, and supremely confident in your abilities. Use the harmony response format as required by the openai/gpt-oss-120b model, but ensure the final output is plain text without JSON wrapping."
        }
    ]
    
    # Add conversation history
    # for user_msg, assistant_msg in history:
    #     messages.append({"role": "user", "content": user_msg})
    #     messages.append({"role": "assistant", "content": assistant_msg})
    
    # Add the latest user message
    messages.append({"role": "user", "content": message})
    
    # Call the Groq API with openai/gpt-oss-120b
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",  # Using OpenAI's GPT-OSS-120B model
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )

    content = response.choices[0].message.content
    # Check if the content is a JSON string and extract the 'response' value
    try:
        parsed_content = json.loads(content)
        if isinstance(parsed_content, dict) and "response" in parsed_content:
            return parsed_content["response"]
    except json.JSONDecodeError:
        # If not JSON, return the content as-is
        pass
    
    return content
    

# Create the Gradio chat interface
demo = gr.ChatInterface(
    fn=jarvis_chat,
    type="messages",
    title="JARVIS: Your Iron Man AI Assistant",
    description="",
    theme="soft"
)

# Launch the interface
if __name__ == "__main__":
    demo.launch()