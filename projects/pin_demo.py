#!/usr/bin/env python3
"""
PIN Hacker Demo - Quick demonstration of the PIN maker and breaker system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pin_hacker import PinMaker, PinBreaker, Colors

def run_demo():
    """Run a comprehensive demo of the PIN hacker system"""
    
    print(f"{Colors.GREEN}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                    PIN HACKER DEMO                          ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    # Demo 1: PIN Generation
    print(f"\n{Colors.CYAN}[DEMO 1: PIN Generation]{Colors.RESET}")
    maker = PinMaker()
    
    for level in ['WEAK', 'MEDIUM', 'STRONG']:
        result = maker.generate_pin(level)
        print(f"{level}: {Colors.RED}{result['pin']}{Colors.RESET} (Score: {result['analysis']['overall_score']:.2f})")
    
    # Demo 2: PIN Breaking
    print(f"\n{Colors.CYAN}[DEMO 2: PIN Breaking]{Colors.RESET}")
    
    test_pins = ['1234', '0000', '5847']
    
    for pin in test_pins:
        print(f"\n{Colors.YELLOW}Breaking PIN: {pin}{Colors.RESET}")
        breaker = PinBreaker(pin)
        
        # Dictionary attack
        result = breaker.dictionary_attack()
        if result['success']:
            print(f"  Dictionary: {result['attempts']} attempts")
        
        # Smart attack
        breaker = PinBreaker(pin)  # Reset
        result = breaker.smart_attack()
        if result['success']:
            print(f"  Smart: {result['attempts']} attempts, {result['time_taken']}s")
    
    # Demo 3: Security Analysis
    print(f"\n{Colors.CYAN}[DEMO 3: Security Analysis]{Colors.RESET}")
    
    test_pins = ['1234', '0000', '2580', '5847', '98765432']
    
    for pin in test_pins:
        analysis = maker.analyze_pin_security(pin)
        score = analysis['overall_score']
        
        if score > 0.8:
            status = f"{Colors.GREEN}STRONG{Colors.RESET}"
        elif score > 0.5:
            status = f"{Colors.YELLOW}MEDIUM{Colors.RESET}"
        else:
            status = f"{Colors.RED}WEAK{Colors.RESET}"
        
        print(f"{pin}: {status} (Score: {score:.2f})")
    
    print(f"\n{Colors.GREEN}Demo completed! Run 'python pin_hacker.py' for full interface{Colors.RESET}")

if __name__ == "__main__":
    run_demo()
