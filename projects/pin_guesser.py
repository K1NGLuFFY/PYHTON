import random
import time
import itertools
from typing import List, Optional

class PinGuesser:
    """A class to handle PIN guessing with multiple strategies."""
    
    def __init__(self, target_pin: str, pin_length: int = 4):
        """
        Initialize the PIN guesser.
        
        Args:
            target_pin: The PIN to guess (as string)
            pin_length: Length of the PIN (default 4)
        """
        self.target_pin = str(target_pin)
        self.pin_length = pin_length
        self.attempts = 0
        self.max_attempts = 10**pin_length  # Maximum possible combinations
        
    def brute_force_guess(self) -> dict:
        """Brute force approach - try all possible combinations."""
        start_time = time.time()
        possible_digits = '0123456789'
        
        for combination in itertools.product(possible_digits, repeat=self.pin_length):
            self.attempts += 1
            guess = ''.join(combination)
            
            if guess == self.target_pin:
                end_time = time.time()
                return {
                    'method': 'brute_force',
                    'pin_found': guess,
                    'attempts': self.attempts,
                    'time_taken': round(end_time - start_time, 4),
                    'success': True
                }
        
        return {'success': False, 'message': 'PIN not found'}
    
    def random_guess(self, max_tries: int = 10000) -> dict:
        """Random guessing approach."""
        start_time = time.time()
        tried_pins = set()
        
        while self.attempts < min(max_tries, self.max_attempts):
            self.attempts += 1
            
            # Generate random PIN
            guess = ''.join([str(random.randint(0, 9)) for _ in range(self.pin_length)])
            
            # Skip if already tried
            if guess in tried_pins:
                continue
            tried_pins.add(guess)
            
            if guess == self.target_pin:
                end_time = time.time()
                return {
                    'method': 'random',
                    'pin_found': guess,
                    'attempts': self.attempts,
                    'time_taken': round(end_time - start_time, 4),
                    'success': True
                }
        
        return {'success': False, 'message': 'PIN not found within max tries'}
    
    def dictionary_guess(self, common_pins: List[str] = None) -> dict:
        """Try common PINs first (dictionary attack)."""
        start_time = time.time()
        
        common_pins = common_pins or [
            '0000', '1111', '1234', '1212', '7777', '1004', '2000', '4444',
            '2222', '6969', '9999', '3333', '5555', '6666', '1122', '1313',
            '8888', '4321', '1010', '2580'
        ]
        
        for guess in common_pins:
            if len(guess) == self.pin_length:
                self.attempts += 1
                if guess == self.target_pin:
                    end_time = time.time()
                    return {
                        'method': 'dictionary',
                        'pin_found': guess,
                        'attempts': self.attempts,
                        'time_taken': round(end_time - start_time, 4),
                        'success': True
                    }
        
        return {'success': False, 'message': 'PIN not in common list'}
    
    def sequential_guess(self, start: int = 0) -> dict:
        """Sequential guessing from a starting point."""
        start_time = time.time()
        
        for num in range(start, 10**self.pin_length):
            self.attempts += 1
            guess = str(num).zfill(self.pin_length)
            
            if guess == self.target_pin:
                end_time = time.time()
                return {
                    'method': 'sequential',
                    'pin_found': guess,
                    'attempts': self.attempts,
                    'time_taken': round(end_time - start_time, 4),
                    'success': True
                }
        
        return {'success': False, 'message': 'PIN not found'}
    
    def smart_guess(self) -> dict:
        """Smart guessing combining dictionary and brute force."""
        # Try dictionary first
        result = self.dictionary_guess()
        if result['success']:
            return result
        
        # Fall back to brute force
        return self.brute_force_guess()

def interactive_pin_guesser():
    """Interactive version for user input."""
    print("=== PIN Guesser Program ===")
    print("Choose a mode:")
    print("1. Demo mode (predefined PIN)")
    print("2. Test mode (you provide PIN)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        target_pin = '1234'  # Predefined for demo
        print(f"Using demo PIN: {target_pin}")
    else:
        target_pin = input("Enter a 4-digit PIN to guess: ").strip()
        if not target_pin.isdigit() or len(target_pin) != 4:
            print("Invalid PIN format. Using 1234 as default.")
            target_pin = '1234'
    
    guesser = PinGuesser(target_pin)
    
    print("\nChoose guessing method:")
    print("1. Brute Force")
    print("2. Random Guess")
    print("3. Dictionary Attack")
    print("4. Sequential Guess")
    print("5. Smart Guess (Dictionary + Brute Force)")
    
    method_choice = input("Enter method (1-5): ").strip()
    
    methods = {
        '1': guesser.brute_force_guess,
        '2': lambda: guesser.random_guess(max_tries=5000),
        '3': guesser.dictionary_guess,
        '4': guesser.sequential_guess,
        '5': guesser.smart_guess
    }
    
    if method_choice in methods:
        print("\nStarting guess...\n")
        result = methods[method_choice]()
        
        if result['success']:
            print(f"✅ PIN found: {result['pin_found']}")
            print(f"Method: {result['method']}")
            print(f"Attempts: {result['attempts']}")
            print(f"Time taken: {result['time_taken']} seconds")
        else:
            print(f"❌ {result['message']}")
    else:
        print("Invalid choice. Running smart guess...")
        result = guesser.smart_guess()
        print(f"✅ PIN found: {result['pin_found']}")
        print(f"Method: {result['method']}")
        print(f"Attempts: {result['attempts']}")

def demo_all_methods():
    """Demonstrate all guessing methods with a test PIN."""
    test_pin = "5847"
    print(f"=== Demo: Guessing PIN '{test_pin}' ===\n")
    
    guesser = PinGuesser(test_pin)
    
    methods = [
        ("Dictionary Attack", guesser.dictionary_guess),
        ("Random Guess", lambda: guesser.random_guess(max_tries=10000)),
        ("Sequential Guess", guesser.sequential_guess),
        ("Brute Force", guesser.brute_force_guess),
        ("Smart Guess", guesser.smart_guess)
    ]
    
    for method_name, method_func in methods:
        # Reset attempts for each method
        guesser.attempts = 0
        result = method_func()
        
        if result['success']:
            print(f"{method_name}: Found in {result['attempts']} attempts, {result['time_taken']}s")
        else:
            print(f"{method_name}: Failed - {result['message']}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_all_methods()
    else:
        interactive_pin_guesser()
