#!/usr/bin/env python3
"""
Oregon Trail - Interactive Brainfuck & Malbolge Edition
Actually playable now
"""
import sys
import random

class InteractiveOregonTrail:
    def __init__(self):
        self.food = 500
        self.ammo = 100
        self.health = 5
        self.miles = 0
        self.day = 0
        self.party_members = 5
        self.game_over = False
        self.won = False
        
    def print_status(self):
        """Display current game state"""
        print(f"\n┌─ DAY {self.day} ─────────────────────────────────────┐")
        print(f"│ Miles: {self.miles}/2000")
        print(f"│ Food: {self.food}  |  Ammo: {self.ammo}  |  Health: {self.health}")
        print(f"│ Party Members: {self.party_members}")
        print(f"└──────────────────────────────────────────────────┘\n")
        
    def malbolge_event(self, day):
        """Generate Malbolge chaos event"""
        events = [
            ("DYSENTERY", -20, 0),
            ("SUCCESSFUL HUNT", 30, 0),
            ("RIVER CROSSING", 0, -5),
            ("FRIENDLY NATIVES", 10, 5),
            ("WAGON WHEEL BROKE", -10, 0),
            ("BUFFALO STAMPEDE", 0, -10),
            ("SNAKE BITE", -15, 0),
            ("FOUND SUPPLIES", 25, 0),
        ]
        
        # XOR chaos for event selection
        malbolge_chaos = ((day ^ self.miles) + (self.food % 256)) % len(events)
        return events[malbolge_chaos]
    
    def travel_day(self, choice):
        """Handle one day of travel"""
        self.day += 1
        
        if choice == '1':  # Travel hard
            self.miles += 30
            self.food -= 5
        elif choice == '2':  # Travel normal
            self.miles += 15
            self.food -= 3
        elif choice == '3':  # Hunt for food
            self.food += random.randint(20, 50)
            self.ammo -= 10
            self.miles += 5
        elif choice == '4':  # Rest
            self.health = min(5, self.health + 1)
            self.food -= 2
            self.miles += 2
        
        # Check for event
        if random.random() > 0.6:
            event_name, food_delta, ammo_delta = self.malbolge_event(self.day)
            print(f"[EVENT] {event_name}!")
            self.food += food_delta
            self.ammo += ammo_delta
            if food_delta < 0:
                self.health -= 1
        
        # Resource checks
        self.food = max(0, self.food)
        self.ammo = max(0, self.ammo)
        self.health = max(0, min(5, self.health))
        
        return True
    
    def check_status(self):
        """Check win/lose conditions"""
        if self.food <= 0:
            print("\n☠️  STARVATION - Your party has perished from hunger")
            return False
        
        if self.health <= 0:
            print("\n☠️  ILLNESS - Party members have succumbed")
            return False
        
        if self.miles >= 2000:
            print("\n🎉 YOU MADE IT TO OREGON!")
            print(f"   Survived {self.day} days with {self.party_members} party members")
            return True
        
        return None  # Game continues
    
    def play(self):
        """Main game loop"""
        print("╔════════════════════════════════════════════════════╗")
        print("║    OREGON TRAIL - BRAINFUCK & MALBOLGE EDITION     ║")
        print("║         An esoteric descent into madness           ║")
        print("╚════════════════════════════════════════════════════╝")
        print("\nYou've assembled a party of settlers heading west.")
        print("You have 500 food, 100 ammo, and a cursed wagon.")
        print("Reach Oregon (2000 miles) to win.\n")
        input("Press ENTER to start...")
        
        while not self.game_over:
            self.print_status()
            
            # Check win/lose
            status = self.check_status()
            if status is True:
                self.won = True
                self.game_over = True
                break
            elif status is False:
                self.game_over = True
                break
            
            # Player choices
            print("What do you do?")
            print("  [1] Push hard  (30 mi, -5 food)")
            print("  [2] Travel normal  (15 mi, -3 food)")
            print("  [3] Hunt  (+food, -ammo, +5 mi)")
            print("  [4] Rest  (+health, -2 food, +2 mi)")
            print("  [Q] Quit\n")
            
            choice = input("Choose (1-4 or Q): ").strip().upper()
            
            if choice == 'Q':
                print("\nYou abandoned the trail.")
                self.game_over = True
                break
            
            if choice in ['1', '2', '3', '4']:
                self.travel_day(choice)
            else:
                print("Invalid choice. Try again.")
                continue
        
        print("\n" + "="*50)
        print("GAME OVER")
        print("="*50)

if __name__ == "__main__":
    game = InteractiveOregonTrail()
    game.play()
