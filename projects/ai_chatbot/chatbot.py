import json
import random
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class AIChatbot:
    def __init__(self):
        self.intents = self.load_intents()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.conversation_context = []
        
    def load_intents(self):
        """Load intents from JSON file"""
        try:
            with open('intents.json', 'r') as file:
                data = json.load(file)
                return data['intents']
        except FileNotFoundError:
            print("Error: intents.json file not found")
            return []
    
    def preprocess_text(self, text):
        """Clean and preprocess user input"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) 
                 for token in tokens 
                 if token not in self.stop_words]
        
        return tokens
    
    def calculate_similarity(self, user_tokens, pattern_tokens):
        """Calculate similarity between user input and pattern"""
        if not user_tokens or not pattern_tokens:
            return 0
        
        # Simple Jaccard similarity
        user_set = set(user_tokens)
        pattern_set = set(pattern_tokens)
        
        intersection = len(user_set.intersection(pattern_set))
        union = len(user_set.union(pattern_set))
        
        return intersection / union if union > 0 else 0
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        if not user_input.strip():
            return "I didn't catch that. Could you please say something?"
        
        # Preprocess user input
        user_tokens = self.preprocess_text(user_input)
        
        best_intent = None
        best_score = 0
        
        # Find the best matching intent
        for intent in self.intents:
            for pattern in intent['patterns']:
                pattern_tokens = self.preprocess_text(pattern.lower())
                similarity = self.calculate_similarity(user_tokens, pattern_tokens)
                
                if similarity > best_score:
                    best_score = similarity
                    best_intent = intent
        
        # Threshold for matching
        if best_score > 0.3 and best_intent:
            response = random.choice(best_intent['responses'])
            self.conversation_context.append({
                'user': user_input,
                'bot': response,
                'intent': best_intent['tag']
            })
            return response
        
        # Default response if no good match
        default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's interesting! Can you tell me more?",
            "I'm still learning. Could you explain that differently?",
            "I didn't quite catch that. What do you mean?"
        ]
        
        return random.choice(default_responses)
    
    def get_conversation_history(self):
        """Return recent conversation history"""
        return self.conversation_context[-5:] if self.conversation_context else []
    
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
