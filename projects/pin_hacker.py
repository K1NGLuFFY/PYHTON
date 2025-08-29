#!/usr/bin/env python3
"""
PIN Hacker - Advanced PIN Maker and Breaker System
A sophisticated tool for creating secure PINs and breaking them with style
"""

import os
import sys
import time
import random
import itertools
import threading
from datetime import datetime
from typing import List, Dict, Any, Optional
import json

class Colors:
    """ANSI color codes for hacker-style output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BLINK = '\033[5m'

class PinMaker:
    """Advanced PIN generation with security analysis"""
    
    def __init__(self):
        self.security_levels = {
            'WEAK': {'length': 4, 'patterns': True, 'repeats': True},
            'MEDIUM': {'length': 6, 'patterns': False, 'repeats': False},
            'STRONG': {'length': 8, 'patterns': False, 'repeats': False},
            'PARANOID': {'length': 12, 'patterns': False, 'repeats': False}
        }
    
    def generate_pin(self, security_level: str = 'MEDIUM', custom_length: int = None) -> Dict[str, Any]:
        """Generate a secure PIN based on security level"""
        config = self.security_levels.get(security_level, self.security_levels['MEDIUM'])
        length = custom_length or config['length']
        
        # Generate PIN
        if security_level == 'PARANOID':
            # Use cryptographic random for paranoid level
            pin = ''.join([str(random.SystemRandom().randint(0, 9)) for _ in range(length)])
        else:
            pin = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        
        # Analyze security
        security_analysis = self.analyze_pin_security(pin)
        
        return {
            'pin': pin,
            'security_level': security_level,
            'analysis': security_analysis,
            'generated_at': datetime.now().isoformat()
        }
    
    def analyze_pin_security(self, pin: str) -> Dict[str, Any]:
        """Analyze PIN security characteristics"""
        analysis = {
            'length_score': min(len(pin) / 8, 1.0),
            'pattern_score': self.check_patterns(pin),
            'repetition_score': self.check_repetitions(pin),
            'sequence_score': self.check_sequences(pin),
            'overall_score': 0
        }
        
        # Calculate overall score
        weights = [0.3, 0.25, 0.25, 0.2]
        scores = [
            analysis['length_score'],
            analysis['pattern_score'],
            analysis['repetition_score'],
            analysis['sequence_score']
        ]
        analysis['overall_score'] = sum(w * s for w, s in zip(weights, scores))
        
        return analysis
    
    def check_patterns(self, pin: str) -> float:
        """Check for common patterns (lower is better)"""
        patterns = ['1234', '4321', '0000', '1111', '1212', '1122', '2580']
        pin_str = str(pin)
        for pattern in patterns:
            if pattern in pin_str:
                return 0.1
        return 1.0
    
    def check_repetitions(self, pin: str) -> float:
        """Check for character repetitions (lower is better)"""
        unique_chars = len(set(pin))
        return unique_chars / len(pin)
    
    def check_sequences(self, pin: str) -> float:
        """Check for sequential numbers (lower is better)"""
        pin_str = str(pin)
        for i in range(len(pin_str) - 2):
            if ord(pin_str[i+1]) == ord(pin_str[i]) + 1 and ord(pin_str[i+2]) == ord(pin_str[i]) + 2:
                return 0.1
        return 1.0

class PinBreaker:
    """Advanced PIN breaking with multiple attack vectors"""
    
    def __init__(self, target_pin: str):
        self.target_pin = str(target_pin)
        self.pin_length = len(target_pin)
        self.attempts = 0
        self.start_time = None
        self.attack_log = []
        
    def log_attack(self, method: str, attempt: str, success: bool = False):
        """Log attack attempts for analysis"""
        self.attack_log.append({
            'timestamp': datetime.now().isoformat(),
            'method': method,
            'attempt': attempt,
            'attempt_number': self.attempts,
            'success': success
        })
    
    def brute_force_attack(self, show_progress: bool = True) -> Dict[str, Any]:
        """Pure brute force attack - try every combination"""
        self.start_time = time.time()
        self.attempts = 0
        
        if show_progress:
            self.display_hacker_banner("BRUTE FORCE ATTACK INITIATED")
        
        possible_digits = '0123456789'
        total_combinations = 10 ** self.pin_length
        
        for combination in itertools.product(possible_digits, repeat=self.pin_length):
            self.attempts += 1
            guess = ''.join(combination)
            
            if show_progress and self.attempts % 1000 == 0:
                progress = (self.attempts / total_combinations) * 100
                self.display_progress(progress, guess)
            
            self.log_attack('brute_force', guess, guess == self.target_pin)
            
            if guess == self.target_pin:
                return self.create_success_result('brute_force', guess)
        
        return self.create_failure_result('brute_force')
    
    def dictionary_attack(self, custom_list: List[str] = None) -> Dict[str, Any]:
        """Dictionary attack using common PINs"""
        self.start_time = time.time()
        self.attempts = 0
        
        self.display_hacker_banner("DICTIONARY ATTACK INITIATED")
        
        common_pins = custom_list or [
            '0000', '1111', '1234', '1212', '7777', '1004', '2000', '4444',
            '2222', '6969', '9999', '3333', '5555', '6666', '1122', '1313',
            '8888', '4321', '1010', '2580', '5683', '0852', '123456', '654321',
            '111111', '000000', '123123', '456456', '789789', '147258', '369369'
        ]
        
        for guess in common_pins:
            if len(guess) == self.pin_length:
                self.attempts += 1
                self.log_attack('dictionary', guess, guess == self.target_pin)
                
                if guess == self.target_pin:
                    return self.create_success_result('dictionary', guess)
        
        return self.create_failure_result('dictionary')
    
    def smart_attack(self) -> Dict[str, Any]:
        """Intelligent attack combining multiple strategies"""
        self.start_time = time.time()
        self.attempts = 0
        
        self.display_hacker_banner("SMART ATTACK INITIATED")
        
        # Phase 1: Dictionary attack
        result = self.dictionary_attack()
        if result['success']:
            return result
        
        # Phase 2: Pattern-based attack
        result = self.pattern_attack()
        if result['success']:
            return result
        
        # Phase 3: Brute force fallback
        return self.brute_force_attack(show_progress=False)
    
    def pattern_attack(self) -> Dict[str, Any]:
        """Attack based on common patterns"""
        self.start_time = time.time()
        self.attempts = 0
        
        patterns = [
            # Repeated digits
            [str(i) * self.pin_length for i in range(10)],
            # Sequential
            [''.join(map(str, range(i, i + self.pin_length))) for i in range(10 - self.pin_length + 1)],
            [''.join(map(str, range(i, i - self.pin_length, -1))) for i in range(9, self.pin_length - 1, -1)],
            # Mirror patterns
            ['1212', '3434', '5656', '7878', '9090'] if self.pin_length == 4 else [],
            # Date patterns
            [f"{year:02d}{month:02d}" for year in range(1, 32) for month in range(1, 13) if len(f"{year:02d}{month:02d}") == self.pin_length]
        ]
        
        for pattern_group in patterns:
            for guess in pattern_group:
                self.attempts += 1
                self.log_attack('pattern', guess, guess == self.target_pin)
                
                if guess == self.target_pin:
                    return self.create_success_result('pattern', guess)
        
        return self.create_failure_result('pattern')
    
    def create_success_result(self, method: str, pin: str) -> Dict[str, Any]:
        """Create success result dictionary"""
        end_time = time.time()
        return {
            'success': True,
            'method': method,
            'pin_found': pin,
            'attempts': self.attempts,
            'time_taken': round(end_time - self.start_time, 4),
            'attack_log': self.attack_log[-10:]  # Last 10 attempts
        }
    
    def create_failure_result(self, method: str) -> Dict[str, Any]:
        """Create failure result dictionary"""
        return {
            'success': False,
            'method': method,
            'attempts': self.attempts,
            'message': f'{method} attack failed to find PIN'
        }
    
    def display_hacker_banner(self, attack_type: str):
        """Display hacker-style banner"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.GREEN}{Colors.BOLD}")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    PIN BREAKER v2.0                        ║")
        print("║              Advanced Penetration System                    ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        print(f"{Colors.RED}ATTACK TYPE: {attack_type}{Colors.RESET}")
        print(f"{Colors.YELLOW}TARGET: {'*' * self.pin_length}{Colors.RESET}")
        print("-" * 60)
    
    def display_progress(self, progress: float, current_guess: str):
        """Display attack progress"""
        bar_length = 40
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        print(f"\r{Colors.CYAN}Progress: [{bar}] {progress:.1f}% | Current: {current_guess}{Colors.RESET}", end='')

class HackerInterface:
    """Main hacker-style interface"""
    
    def __init__(self):
        self.pin_maker = PinMaker()
        self.current_session = None
    
    def display_banner(self):
        """Display main banner"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.GREEN}{Colors.BOLD}")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║   ██████╗ ██╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗   ║")
        print("║   ██╔══██╗██║████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔════╝   ║")
        print("║   ██████╔╝██║██╔██╗ ██║██║  ███╗██████╔╝██████╔╝█████╗     ║")
        print("║   ██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██╗██╔══╝     ║")
        print("║   ██║     ██║██║ ╚████║╚██████╔╝██║  ██║██║  ██║███████╗   ║")
        print("║   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ║")
        print("║                                                              ║")
        print("║              ADVANCED PIN MAKER & BREAKER                   ║")
        print("║                  Zero Day Security Suite                    ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def display_menu(self):
        """Display main menu"""
        print(f"\n{Colors.CYAN}┌─────────────────────────────┐")
        print("│        MAIN MENU            │")
        print("├─────────────────────────────┤")
        print("│ 1. PIN Maker (Generate)     │")
        print("│ 2. PIN Breaker (Attack)    │")
        print("│ 3. Security Analysis       │")
        print("│ 4. Attack Simulator      │")
        print("│ 5. Exit                  │")
        print("└─────────────────────────────┘{Colors.RESET}")
    
    def pin_maker_mode(self):
        """PIN generation mode"""
        self.display_banner()
        print(f"\n{Colors.GREEN}[PIN MAKER MODE ACTIVATED]{Colors.RESET}")
        
        print("\nSecurity Levels:")
        print("1. WEAK (4 digits, patterns allowed)")
        print("2. MEDIUM (6 digits, secure)")
        print("3. STRONG (8 digits, very secure)")
        print("4. PARANOID (12 digits, maximum security)")
        print("5. Custom length")
        
        choice = input(f"\n{Colors.YELLOW}Select security level (1-5): {Colors.RESET}").strip()
        
        security_map = {
            '1': 'WEAK',
            '2': 'MEDIUM',
            '3': 'STRONG',
            '4': 'PARANOID'
        }
        
        if choice in security_map:
            result = self.pin_maker.generate_pin(security_map[choice])
        elif choice == '5':
            length = int(input("Enter custom PIN length: "))
            result = self.pin_maker.generate_pin('CUSTOM', length)
        else:
            result = self.pin_maker.generate_pin('MEDIUM')
        
        self.display_pin_result(result)
    
    def display_pin_result(self, result: Dict[str, Any]):
        """Display PIN generation results"""
        print(f"\n{Colors.GREEN}[PIN GENERATED SUCCESSFULLY]{Colors.RESET}")
        print(f"PIN: {Colors.RED}{Colors.BOLD}{result['pin']}{Colors.RESET}")
        print(f"Security Level: {result['security_level']}")
        print(f"Overall Security Score: {result['analysis']['overall_score']:.2f}")
        
        print(f"\n{Colors.CYAN}Security Analysis:{Colors.RESET}")
        print(f"  Length Score: {result['analysis']['length_score']:.2f}")
        print(f"  Pattern Score: {result['analysis']['pattern_score']:.2f}")
        print(f"  Repetition Score: {result['analysis']['repetition_score']:.2f}")
        print(f"  Sequence Score: {result['analysis']['sequence_score']:.2f}")
    
    def pin_breaker_mode(self):
        """PIN breaking mode"""
        self.display_banner()
        print(f"\n{Colors.RED}[PIN BREAKER MODE ACTIVATED]{Colors.RESET}")
        
        target_pin = input(f"\n{Colors.YELLOW}Enter target PIN to break: {Colors.RESET}").strip()
        
        if not target_pin.isdigit():
            print(f"{Colors.RED}Invalid PIN format!{Colors.RESET}")
            return
        
        breaker = PinBreaker(target_pin)
        
        print("\nAttack Methods:")
        print("1. Dictionary Attack (fast)")
        print("2. Brute Force (comprehensive)")
        print("3. Pattern Attack (smart)")
        print("4. Smart Attack (all methods)")
        
        method_choice = input(f"\n{Colors.YELLOW}Select attack method (1-4): {Colors.RESET}").strip()
        
        methods = {
            '1': breaker.dictionary_attack,
            '2': lambda: breaker.brute_force_attack(show_progress=True),
            '3': breaker.pattern_attack,
            '4': breaker.smart_attack
        }
        
        if method_choice in methods:
            print(f"\n{Colors.RED}⚠️  ATTACK IN PROGRESS...{Colors.RESET}")
            result = methods[method_choice]()
            self.display_attack_result(result)
        else:
            result = breaker.smart_attack()
            self.display_attack_result(result)
    
    def display_attack_result(self, result: Dict[str, Any]):
        """Display attack results"""
        if result['success']:
            print(f"\n{Colors.GREEN}[ATTACK SUCCESSFUL]{Colors.RESET}")
            print(f"PIN Cracked: {Colors.RED}{Colors.BOLD}{result['pin_found']}{Colors.RESET}")
            print(f"Method Used: {result['method']}")
            print(f"Attempts: {Colors.YELLOW}{result['attempts']}{Colors.RESET}")
            print(f"Time: {Colors.CYAN}{result['time_taken']}s{Colors.RESET}")
            
            if 'attack_log' in result:
                print(f"\n{Colors.PURPLE}Last attempts:{Colors.RESET}")
                for log in result['attack_log'][-5:]:
                    print(f"  Attempt #{log['attempt_number']}: {log['attempt']}")
        else:
            print(f"\n{Colors.RED}[ATTACK FAILED]{Colors.RESET}")
            print(result['message'])
    
    def security_analysis_mode(self):
        """Analyze PIN security"""
        self.display_banner()
        print(f"\n{Colors.BLUE}[SECURITY ANALYSIS MODE]{Colors.RESET}")
        
        pin = input(f"\n{Colors.YELLOW}Enter PIN to analyze: {Colors.RESET}").strip()
        
        analysis = self.pin_maker.analyze_pin_security(pin)
        
        print(f"\n{Colors.CYAN}Security Report for PIN: {Colors.RED}{pin}{Colors.RESET}")
        print(f"Overall Security Score: {analysis['overall_score']:.2f}/1.0")
        
        if analysis['overall_score'] > 0.8:
            print(f"{Colors.GREEN}✅ STRONG PIN{Colors.RESET}")
        elif analysis['overall_score'] > 0.5:
            print(f"{Colors.YELLOW}⚠️  MEDIUM SECURITY{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ WEAK PIN - Consider changing{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_banner()
            self.display_menu()
            
            choice = input(f"\n{Colors.YELLOW}Enter choice (1-5): {Colors.RESET}").strip()
            
            if choice == '1':
                self.pin_maker_mode()
            elif choice == '2':
                self.pin_breaker_mode()
            elif choice == '3':
                self.security_analysis_mode()
            elif choice == '4':
                self.attack_simulator()
            elif choice == '5':
                print(f"\n{Colors.GREEN}[SESSION TERMINATED]{Colors.RESET}")
                break
            else:
                print(f"\n{Colors.RED}Invalid choice!{Colors.RESET}")
            
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
    
    def attack_simulator(self):
        """Simulate various attack scenarios"""
        self.display_banner()
        print(f"\n{Colors.PURPLE}[ATTACK SIMULATOR]{Colors.RESET}")
        
        test_pins = ['1234', '0000', '2580', '5847', '9876']
        
        for pin in test_pins:
            print(f"\n{Colors.YELLOW}Testing PIN: {pin}{Colors.RESET}")
            breaker = PinBreaker(pin)
            result = breaker.smart_attack()
            
            if result['success']:
                print(f"  ✅ Cracked in {result['attempts']} attempts")
            else:
                print(f"  ❌ Failed to crack")

def main():
    """Main entry point"""
    try:
        interface = HackerInterface()
        interface.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[SESSION INTERRUPTED]{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[ERROR] {str(e)}{Colors.RESET}")

if __name__ == "__main__":
    main()
