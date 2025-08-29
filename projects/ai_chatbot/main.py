#!/usr/bin/env python3
"""
AI Chatbot - Main Application
A simple AI chatbot that can have conversations and answer questions
"""

import sys
import os
from chatbot import AIChatbot, initialize_nltk

def print_welcome():
    """Print welcome message"""
    print("\n" + "="*50)
    print("    🤖 AI CHATBOT")
    print("="*50)
    print("Hello! I'm your AI assistant.")
    print("Type 'help' for available commands")
    print("Type 'quit' or 'exit' to leave")
    print("="*50 + "\n")

def print_help():
    """Print help information"""
    print("\n" + "-"*30)
    print("AVAILABLE COMMANDS:")
    print("  help     - Show this help message")
    print("  history  - Show recent conversation")
    print("  clear    - Clear conversation history")
    print("  quit/exit- Exit the chatbot")
    print("-"*30 + "\n")

def main():
    """Main chatbot loop"""
    # Initialize NLTK
    initialize_nltk()
    
    # Create chatbot instance
    chatbot = AIChatbot()
    
    # Print welcome message
    print_welcome()
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Handle empty input
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("Bot: Goodbye! Have a great day! 👋")
                break
            
            elif user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'history':
                history = chatbot.get_conversation_history()
                if history:
                    print("\n" + "-"*30)
                    print("RECENT CONVERSATION:")
                    for i, entry in enumerate(history, 1):
                        print(f"  {i}. You: {entry['user']}")
                        print(f"     Bot: {entry['bot']}")
                    print("-"*30 + "\n")
                else:
                    print("Bot: No conversation history yet.\n")
                continue
            
            elif user_input.lower() == 'clear':
                chatbot.clear_context()
                print("Bot: Conversation history cleared!\n")
                continue
            
            # Get response from chatbot
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! Have a great day! 👋")
            break
        except Exception as e:
            print(f"Bot: Sorry, I encountered an error: {str(e)}\n")

if __name__ == "__main__":
    main()
