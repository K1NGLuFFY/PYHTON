#!/usr/bin/env python3
"""
Banking Customer Service Bot - Main Application
A comprehensive AI assistant for banking and business queries
"""

import os
import sys
from banking_chatbot import BankingCustomerServiceBot, initialize_nltk

def display_welcome():
    """Display welcome message and instructions"""
    print("\n" + "="*60)
    print("🏦 WELCOME TO YOUR BANKING CUSTOMER SERVICE BOT")
    print("="*60)
    print("I can help you with:")
    print("  • Check account balance")
    print("  • View transaction history")
    print("  • Loan eligibility and information")
    print("  • Credit card options")
    print("  • Branch locations")
    print("  • Interest calculations")
    print("  • Account opening")
    print("  • Business banking services")
    print("  • And much more!")
    print("="*60)
    print("Type 'help' for available commands or 'exit' to quit")
    print("="*60 + "\n")

def display_help():
    """Display available commands and examples"""
    print("\n📋 AVAILABLE COMMANDS:")
    print("-" * 30)
    print("General:")
    print("  help - Show this help message")
    print("  history - Show conversation history")
    print("  clear - Clear conversation history")
    print("  exit - Exit the chatbot")
    print("\nBanking Examples:")
    print("  'What's my account balance?'")
    print("  'Show my recent transactions'")
    print("  'Am I eligible for a personal loan?'")
    print("  'Calculate interest on $1000 at 5% for 2 years'")
    print("  'Where is the nearest branch?'")
    print("  'What credit cards do you offer?'")
    print("  'How do I open a business account?'")
    print("  'What are your mortgage rates?'")
    print("-" * 30 + "\n")

def display_farewell():
    """Display farewell message"""
    print("\n" + "="*60)
    print("Thank you for using our Banking Customer Service Bot!")
    print("Visit us at www.yourbank.com or call 1-800-BANK-HELP")
    print("Have a great day! 👋")
    print("="*60 + "\n")

def main():
    """Main application loop"""
    try:
        # Initialize NLTK data
        print("Initializing Banking Customer Service Bot...")
        initialize_nltk()
        
        # Create bot instance
        bot = BankingCustomerServiceBot()
        
        # Display welcome message
        display_welcome()
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Handle empty input
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() == 'exit':
                    display_farewell()
                    break
                
                elif user_input.lower() == 'help':
                    display_help()
                    continue
                
                elif user_input.lower() == 'history':
                    history = bot.get_conversation_history()
                    if history:
                        print("\n📜 CONVERSATION HISTORY:")
                        print("-" * 40)
                        for entry in history:
                            print(f"Time: {entry.get('timestamp', 'N/A')}")
                            print(f"You: {entry['user']}")
                            print(f"Bot: {entry['bot']}")
                            print("-" * 40)
                    else:
                        print("No conversation history yet.")
                    continue
                
                elif user_input.lower() == 'clear':
                    bot.clear_context()
                    print("✅ Conversation history cleared.")
                    continue
                
                # Get bot response
                response = bot.get_response(user_input)
                print(f"\n🏦 Bot: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nExiting...")
                display_farewell()
                break
                
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                print("Please try again or contact customer service.\n")
                
    except Exception as e:
        print(f"Failed to initialize the banking bot: {str(e)}")
        print("Please ensure all dependencies are installed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
