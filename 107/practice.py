class Person:
    def __init__(self, name, age, height, favorite_player):
        self.name = name
        self.age = age
        self.height = height
        self.favorite_player = favorite_player

    def introduce(self):
        introduction = (f"Hello, my name is {self.name}. "
                        f"I am {self.age} years old, "
                        f"{self.height} feet tall and "
                        f"my favorite football player is {self.favorite_player}.")
        return introduction

# Create an instance of Person
alex = Person(name="Alex Molina", age=27, height=6, favorite_player="Ray Lewis")

# Print the introduction
print(alex.introduce())