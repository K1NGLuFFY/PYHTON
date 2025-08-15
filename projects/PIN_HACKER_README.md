# PIN Hacker - Advanced PIN Maker & Breaker System

## Overview
PIN Hacker is a sophisticated Python application that combines PIN generation with security analysis and advanced breaking techniques. It features a hacker-style interface with multiple attack vectors and comprehensive security analysis.

## Features

### PIN Maker
- **Multiple Security Levels**: WEAK, MEDIUM, STRONG, PARANOID
- **Custom PIN Lengths**: Generate PINs of any length
- **Security Analysis**: Real-time security scoring
- **Pattern Detection**: Identifies weak patterns and sequences

### PIN Breaker
- **Dictionary Attack**: Uses common PIN databases
- **Brute Force Attack**: Systematic combination testing
- **Pattern Attack**: Exploits predictable patterns
- **Smart Attack**: Combines all methods intelligently

### Security Analysis
- **Real-time Scoring**: 0.0-1.0 security scale
- **Pattern Detection**: Identifies weak sequences
- **Repetition Analysis**: Checks for character repetition
- **Length Assessment**: Evaluates PIN length impact

## Usage

### Quick Demo
```bash
python pin_demo.py
```

### Full Interface
```bash
python pin_hacker.py
```

### Menu Options
1. **PIN Maker**: Generate secure PINs
2. **PIN Breaker**: Break target PINs
3. **Security Analysis**: Analyze PIN security
4. **Attack Simulator**: Run attack scenarios
5. **Exit**: Close application

## Attack Methods

### Dictionary Attack
- Uses common PIN databases
- Very fast for weak PINs
- Tests: 0000, 1234, 1111, etc.

### Brute Force Attack
- Tries every possible combination
- Comprehensive but slow
- Progress indicator included

### Pattern Attack
- Exploits predictable patterns
- Sequential numbers
- Repeated digits
- Mirror patterns

### Smart Attack
- Combines all methods
- Optimized sequence
- Best balance of speed and coverage

## Security Scoring

### Score Interpretation
- **0.8-1.0**: Strong PIN (recommended)
- **0.5-0.8**: Medium security (acceptable)
- **0.0-0.5**: Weak PIN (needs improvement)

### Factors Considered
- **Length**: Longer PINs score higher
- **Patterns**: Common patterns reduce score
- **Repetition**: Character diversity improves score
- **Sequences**: Avoid sequential numbers

## Examples

### Generate Secure PIN
```
Security Level: STRONG
Generated PIN: 73920485
Security Score: 0.92
```

### Break PIN
```
Target PIN: 1234
Method: Dictionary Attack
Attempts: 3
Time: 0.001s
```

### Security Analysis
```
PIN: 1234
Security Score: 0.15 (WEAK)
Recommendation: Use longer, more random PIN
```

## Technical Details

### Dependencies
- Python 3.6+
- Standard library only (no external dependencies)

### Files Structure
- `pin_hacker.py`: Main application
- `pin_demo.py`: Quick demonstration
- `pin_guesser.py`: Legacy system (included)

### Color Support
- ANSI color codes for enhanced display
- Works on Windows, macOS, and Linux
- Automatic terminal detection

## Security Notes

### Educational Purpose
This tool is designed for:
- Security awareness training
- Password strength education
- Penetration testing practice
- Educational demonstrations

### Ethical Use
- Only test on systems you own
- Never use for malicious purposes
- Respect privacy and security laws
- Use for learning and improvement

## Advanced Usage

### Batch Processing
```python
from pin_hacker import PinMaker, PinBreaker

# Generate multiple PINs
maker = PinMaker()
for level in ['WEAK', 'MEDIUM', 'STRONG']:
    result = maker.generate_pin(level)
    print(f"{level}: {result['pin']}")

# Test PIN strength
breaker = PinBreaker("1234")
result = breaker.smart_attack()
print(f"Cracked in {result['attempts']} attempts")
```

### Custom Attack Lists
```python
# Custom dictionary attack
breaker = PinBreaker("target_pin")
result = breaker.dictionary_attack(custom_list=['0000', '1234', '9999'])
```

## Troubleshooting

### Common Issues
- **Colors not showing**: Use Windows Terminal or enable ANSI support
- **Performance issues**: Reduce PIN length for testing
- **Import errors**: Ensure all files are in the same directory

### Performance Tips
- Use shorter PINs for demonstration
- Dictionary attack is fastest for weak PINs
- Smart attack provides best balance
- Monitor system resources for long attacks

## Version History
- v2.0: Complete rewrite with hacker interface
- v1.0: Basic PIN guessing functionality
- Legacy: Included for backward compatibility
