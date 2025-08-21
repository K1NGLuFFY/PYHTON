#!/usr/bin/env python3
"""
Aptech Direction Guide
A simple Python program to guide users from either Abakpa or Emene to Aptech institution
"""

import sys

class AptechDirectionGuide:
    def __init__(self):
        self.locations = {
            "abakpa": {
                "name": "Abakpa",
                "directions": [
                    "From Abakpa Market, head west on Abakpa Road",
                    "Continue straight for about 2.5km",
                    "Turn right at the T-junction (Aptech signboard visible)",
                    "Drive 500m, Aptech will be on your left",
                    "Landmark: Look for the blue Aptech building with computer graphics"
                ]
            },
            "emene": {
                "name": "Emene",
                "directions": [
                    "From Emene Junction, take the Enugu-Abakaliki Expressway",
                    "Drive east for approximately 3.2km",
                    "Turn left at the first major intersection after the fuel station",
                    "Continue for 800m, Aptech will be on your right",
                    "Landmark: Opposite the Total filling station"
                ]
            }
        }
        
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("=" * 50)
        print("    APTECH DIRECTION GUIDE")
        print("=" * 50)
        print("Welcome! This guide will help you reach Aptech")
        print("institution from either Abakpa or Emene.")
        print()
        
    def get_user_location(self):
        """Get user's starting location"""
        while True:
            print("\nWhere are you coming from?")
            print("1. Abakpa")
            print("2. Emene")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                return "abakpa"
            elif choice == '2':
                return "emene"
            elif choice == '3':
                print("Thank you for using Aptech Direction Guide!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
    def display_directions(self, location_key):
        """Display directions for the selected location"""
        location = self.locations[location_key]
        
        print(f"\n{'='*50}")
        print(f"DIRECTIONS FROM {location['name'].upper()} TO APTECH")
        print(f"{'='*50}")
        
        for i, direction in enumerate(location['directions'], 1):
            print(f"{i}. {direction}")
            
        print(f"\n{'='*50}")
        print("Additional Tips:")
        print("- Journey time: ~15-20 minutes depending on traffic")
        print("- Alternative route: Use Google Maps for real-time updates")
        print("- Contact: 0803-123-4567 for further assistance")
        print(f"{'='*50}")
        
    def run(self):
        """Main program loop"""
        self.display_welcome()
        
        while True:
            location = self.get_user_location()
            self.display_directions(location)
            
            print("\nWould you like to:")
            print("1. Get directions from another location")
            print("2. Exit")
            
            choice = input("Enter your choice (1-2): ").strip()
            
            if choice == '2':
                print("Thank you for using Aptech Direction Guide!")
                break
            elif choice != '1':
                print("Invalid choice. Exiting...")
                break

def main():
    """Main function to run the program"""
    guide = AptechDirectionGuide()
    guide.run()

if __name__ == "__main__":
    main()
