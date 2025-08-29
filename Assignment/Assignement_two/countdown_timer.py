import time

"""
Countdown Timer Program
======================

This program creates a simple countdown timer that counts from 10 to 1.
It uses a while loop and the 'time' module for delays.
"""

print("=== COUNTDOWN TIMER ===")
print("Starting countdown from 10 to 1...\n")

# Countdown from 10 to 1
count = 10
while count > 0:
    print(f" {count}")
    time.sleep(1)  # Pause the program for 1 second
    count -= 1

print("BOOOMMM!!!")
