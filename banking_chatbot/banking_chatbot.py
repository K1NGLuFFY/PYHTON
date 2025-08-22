import json
import random
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from datetime import datetime
import requests
from typing import Dict, List, Optional

class BankingCustomerServiceBot:
    def __init__(self):
        self.intents = self.load_intents()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.conversation_context = []
        self.account_balance = 5000.00  # Mock account data
        self.transaction_history = []
        self.loan_eligibility = {"personal": True, "home": True, "car": True}
        self.credit_score = 750
        
    def load_intents(self):
        """Load banking-specific intents from JSON file"""
        try:
            with open('banking_intents.json', 'r') as file:
                data = json.load(file)
                return data['intents']
        except FileNotFoundError:
            print("Error: banking_intents.json file not found")
            return []
    
    def preprocess_text(self, text):
        """Clean and preprocess user input"""
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) 
                 for token in tokens 
                 if token not in self.stop_words]
        return tokens
    
    def calculate_similarity(self, user_tokens, pattern_tokens):
        """Calculate similarity between user input and pattern"""
        if not user_tokens or not pattern_tokens:
            return 0
        
        user_set = set(user_tokens)
        pattern_set = set(pattern_tokens)
        
        intersection = len(user_set.intersection(pattern_set))
        union = len(user_set.union(pattern_set))
        
        return intersection / union if union > 0 else 0
    
    def format_currency(self, amount):
        """Format amount as currency"""
        return f"${amount:,.2f}"
    
    def get_account_balance(self):
        """Return current account balance"""
        return f"Your current account balance is {self.format_currency(self.account_balance)}"
    
    def get_transaction_history(self, limit=5):
        """Return recent transaction history"""
        if not self.transaction_history:
            return "No recent transactions found."
        
        history = self.transaction_history[-limit:]
        formatted_history = []
        for transaction in history:
            formatted_history.append(
                f"{transaction['date']}: {transaction['description']} - "
                f"{self.format_currency(transaction['amount'])} "
                f"({transaction['type']})"
            )
        return "Recent transactions:\n" + "\n".join(formatted_history)
    
    def check_loan_eligibility(self, loan_type):
        """Check loan eligibility based on type"""
        if loan_type.lower() in ["personal", "home", "car"]:
            eligible = self.loan_eligibility[loan_type.lower()]
            if eligible:
                return f"Good news! You are eligible for a {loan_type} loan with your credit score of {self.credit_score}."
            else:
                return f"Based on your current profile, you may not be eligible for a {loan_type} loan at this time."
        return "Please specify the loan type (personal, home, or car) for eligibility check."
    
    def calculate_interest(self, principal, rate, time):
        """Calculate simple interest"""
        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        return interest, total_amount
    
    def process_banking_query(self, intent, entities=None):
        """Process banking-specific queries"""
        if intent == "check_balance":
            return self.get_account_balance()
        
        elif intent == "transaction_history":
            return self.get_transaction_history()
        
        elif intent == "loan_eligibility":
            loan_type = entities.get('loan_type', 'personal') if entities else 'personal'
            return self.check_loan_eligibility(loan_type)
        
        elif intent == "interest_calculation":
            if entities and 'principal' in entities and 'rate' in entities and 'time' in entities:
                principal = float(entities['principal'])
                rate = float(entities['rate'])
                time = float(entities['time'])
                interest, total = self.calculate_interest(principal, rate, time)
                return (f"For ${principal} at {rate}% for {time} years:\n"
                       f"Interest: {self.format_currency(interest)}\n"
                       f"Total amount: {self.format_currency(total)}")
            return "Please provide principal amount, interest rate, and time period for calculation."
        
        elif intent == "transfer_money":
            return "To transfer money, please log into your online banking or visit our nearest branch. For security reasons, I cannot process transfers through this chat."
        
        elif intent == "credit_card_info":
            return ("We offer various credit cards with different benefits:\n"
                   "- Rewards Card: Earn points on every purchase\n"
                   "- Cashback Card: Get cash back on eligible purchases\n"
                   "- Travel Card: Earn miles and travel benefits\n"
                   "Visit our website or branch to apply.")
        
        elif intent == "branch_locator":
            return ("Our branches are located at:\n"
                   "1. Downtown Branch: 123 Main Street\n"
                   "2. Uptown Branch: 456 Oak Avenue\n"
                   "3. Westside Branch: 789 Pine Road\n"
                   "Hours: Monday-Friday 9AM-5PM, Saturday 9AM-1PM")
        
        return None
    
    def get_response(self, user_input):
        """Generate banking-specific response"""
        if not user_input.strip():
            return "I didn't catch that. Could you please rephrase your banking question?"
        
        user_tokens = self.preprocess_text(user_input)
        
        best_intent = None
        best_score = 0
        entities = {}
        
        # Find best matching intent
        for intent in self.intents:
            for pattern in intent['patterns']:
                pattern_tokens = self.preprocess_text(pattern.lower())
                similarity = self.calculate_similarity(user_tokens, pattern_tokens)
                
                if similarity > best_score:
                    best_score = similarity
                    best_intent = intent
        
        # Process banking-specific queries
        if best_score > 0.3 and best_intent:
            banking_response = self.process_banking_query(
                best_intent['tag'], 
                self.extract_entities(user_input)
            )
            
            if banking_response:
                response = banking_response
            else:
                response = random.choice(best_intent['responses'])
            
            self.conversation_context.append({
                'user': user_input,
                'bot': response,
                'intent': best_intent['tag'],
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            return response
        
        # Default responses for unmatched queries
        default_responses = [
            "I'm not sure I understand your banking question. Could you rephrase it?",
            "I can help with account balance, transactions, loans, and other banking services. What would you like to know?",
            "Let me help you with your banking needs. Could you clarify your question?",
            "I specialize in banking and financial services. How can I assist you today?"
        ]
        
        return random.choice(default_responses)
    
    def extract_entities(self, user_input):
        """Extract entities like amounts, dates, etc. from user input"""
        entities = {}
        
        # Extract dollar amounts
        amount_pattern = r'\$?(\d+(?:\.\d{2})?)'
        amounts = re.findall(amount_pattern, user_input)
        if amounts:
            entities['amount'] = amounts[0]
        
        # Extract loan types
        loan_types = ['personal', 'home', 'car', 'business']
        for loan_type in loan_types:
            if loan_type in user_input.lower():
                entities['loan_type'] = loan_type
        
        # Extract numbers for interest calculation
        numbers = re.findall(r'\d+(?:\.\d+)?', user_input)
        if len(numbers) >= 3:
            entities['principal'] = numbers[0]
            entities['rate'] = numbers[1]
            entities['time'] = numbers[2]
        
        return entities
    
    def get_conversation_history(self):
        """Return conversation history"""
        return self.conversation_context
    
    def clear_context(self):
        """Clear conversation context"""
        self.conversation_context = []

def initialize_nltk():
    """Download required NLTK data"""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        print("Downloading required NLTK data...")
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        print("NLTK data downloaded successfully!")
