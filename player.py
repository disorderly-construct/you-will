class Player:
    def __init__(self, name):
        self.name = name  
        self.health = 100  
        self.stamina = 100  
        self.mana = 100  
        self.target_health = 50  
        self.target_stamina = 60  
        self.target_mana = 70  

    def decrease_health(self, amount):
        self.health -= amount  # Decrease health by the specified amount
        if self.health < 0:  # Ensure health doesn't go below 0
            self.health = 0

    def decrease_stamina(self, amount):
        self.stamina -= amount  # Decrease stamina by the specified amount
        if self.stamina < 0:  # Ensure stamina doesn't go below 0
            self.stamina = 0

    def decrease_mana(self, amount):
        self.mana -= amount  # Decrease mana by the specified amount
        if self.mana < 0:  # Ensure mana doesn't go below 0
            self.mana = 0

    def display_stats(self):
        print(f"Player: {self.name}\n")  # Print the player's name
        self.display_meter("Health", self.health, self.target_health, 100)  # Display health meter
        self.display_meter("Stamina", self.stamina, self.target_stamina, 100)  # Display stamina meter
        self.display_meter("Mana", self.mana, self.target_mana, 100)  # Display mana meter
        print("\nTargets:")
        print(f"Health Target: {self.target_health}")
        print(f"Stamina Target: {self.target_stamina}") 
        print(f"Mana Target: {self.target_mana}") 

    def display_meter(self, name, value, target_value, max_value):
        meter_length = 10  # Length of the meter in circles
        filled_length = int(meter_length * value / max_value)  # Calculate the filled length of the meter, with added int function for stability. Adding value to numerator creates a correct proportional ratio.
        meter = '●' * filled_length + '○' * (meter_length - filled_length)  # Create the meter with filled and unfilled circles appearing in correct locations
        print(f"{name}: |{meter}| {value}/{target_value}")

# Example usage:
player = Player("Hero")  # Create a new player instance with the name "Hero"
player.display_stats()  # Display the initial stats of the player

# Decrease values for demonstration
player.decrease_health(40)  # Decrease health by 40
player.decrease_stamina(60)  # Decrease stamina by 60
player.decrease_mana(1)  # Decrease mana by 5
player.display_stats()  # Display the updated stats of the player
