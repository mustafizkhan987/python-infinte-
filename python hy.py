import time
import random

# Utility functions
def slow_print(text, delay=0.03):
    """Print text one character at a time."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def separator():
    print("=" * 60)

# Game classes
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.health -= damage
        slow_print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

class Enemy(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []

    def heal(self):
        if "Potion" in self.inventory:
            self.health += 20
            self.inventory.remove("Potion")
            slow_print(f"{self.name} uses a Potion and recovers 20 health!")
        else:
            slow_print("You don't have any Potions!")

# Game functions
def intro():
    separator()
    slow_print("Welcome to the Adventure Game!")
    slow_print("Your goal is to navigate through the forest, defeat enemies, and escape alive.")
    separator()


def encounter_enemy(player):
    enemy = Enemy("Goblin", 30, 5)
    slow_print(f"A wild {enemy.name} appears!")

    while enemy.is_alive() and player.is_alive():
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Heal")
        print("3. Run")
        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(player)
        elif choice == "2":
            player.heal()
            if enemy.is_alive():
                enemy.attack(player)
        elif choice == "3":
            slow_print("You run away from the battle.")
            return False
        else:
            slow_print("Invalid choice. The enemy attacks!")
            enemy.attack(player)

    if player.is_alive():
        slow_print(f"You defeated the {enemy.name}!")
        player.inventory.append("Potion")
        slow_print("You found a Potion in the enemy's bag.")
        return True
    else:
        slow_print("You were defeated by the enemy...")
        return False


def explore(player):
    separator()
    slow_print("You venture deeper into the forest.")
    event = random.choice(["enemy", "item", "nothing"])

    if event == "enemy":
        return encounter_enemy(player)
    elif event == "item":
        slow_print("You found a Potion on the ground!")
        player.inventory.append("Potion")
    else:
        slow_print("You find nothing of interest.")
    return True

def final_battle(player):
    separator()
    slow_print("You reach the heart of the forest. A towering ogre blocks your path!")
    boss = Enemy("Ogre", 80, 15)

    while boss.is_alive() and player.is_alive():
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Heal")
        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(boss)
            if boss.is_alive():
                boss.attack(player)
        elif choice == "2":
            player.heal()
            if boss.is_alive():
                boss.attack(player)
        else:
            slow_print("Invalid choice. The ogre attacks!")
            boss.attack(player)

    if player.is_alive():
        slow_print("You defeated the ogre and escaped the forest!")
        return True
    else:
        slow_print("You were slain by the ogre...")
        return False

# Main game loop
def main():
    intro()
    name = input("Enter your name: ")
    player = Player(name)

    game_running = True

    while game_running:
        separator()
        print("\nWhat would you like to do?")
        print("1. Explore the forest")
        print("2. Check inventory")
        print("3. Quit game")
        choice = input("Choose an option: ")

        if choice == "1":
            if not explore(player):
                break
        elif choice == "2":
            separator()
            slow_print(f"Health: {player.health}")
            slow_print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")
        elif choice == "3":
            slow_print("Thanks for playing!")
            game_running = False
        else:
            slow_print("Invalid choice.")

        if player.health <= 0:
            slow_print("You have perished in the forest. Game Over.")
            game_running = False

    if player.is_alive():
        final_battle(player)

if __name__ == "__main__":
    main()
