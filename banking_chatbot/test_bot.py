#!/usr/bin/env python3
"""
Test script for Banking Customer Service Bot
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from banking_chatbot import BankingCustomerServiceBot, initialize_nltk

def test_basic_functionality():
    """Test basic bot functionality"""
    print("🧪 Testing Banking Customer Service Bot...")
    
    # Initialize NLTK
    initialize_nltk()
    
    # Create bot instance
    bot = BankingCustomerServiceBot()
    
    # Test cases
    test_queries = [
        "What's my account balance?",
        "Show my recent transactions",
        "Am I eligible for a personal loan?",
        "Calculate interest on 10000 at 5% for 2 years",
        "Where is the nearest branch?",
        "What credit cards do you offer?",
        "How do I open a business account?",
        "Thank you",
        "Goodbye"
    ]
    
    print("\n✅ Testing individual queries:")
    for query in test_queries:
        print(f"\n📝 Query: {query}")
        response = bot.get_response(query)
        print(f"🤖 Response: {response}")
    
    print("\n✅ All tests completed successfully!")
    return True

if __name__ == "__main__":
    try:
        test_basic_functionality()
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        sys.exit(1)
