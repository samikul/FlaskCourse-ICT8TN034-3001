"Animal classes to demonstrate OOP"

class Animal():
	name = "Generic animal"

	def sound(self):
		return f"Generic sounds by {self.name}"

	def __repr__(self):
		return f"<Animal {self.name}>"

class Lion(Animal):
	def sound(self):
		return "Roaar!"

class Cat(Animal):
	def sound(self):
		return "Meow!"

def main():
	lion = Lion()
	print(lion.sound())
	cat = Cat()
	print(cat.sound())
	ani = Animal()
	print(ani.sound())

if __name__ == "__main__":
	main()
