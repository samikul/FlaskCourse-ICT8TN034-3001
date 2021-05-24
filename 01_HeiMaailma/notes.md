

- Hei maailma
- Skriptin teko
- Paketinhallinta ja ohjelmien asentaminen
- Hei Flask!
  - päivitä paketit
  - python3-flask
  - "hello flask"

### Pythonkertausta
Luennon esimerkit (Tero Karvinen, 24.5.2021):

#### yourname.py
```python
#!/usr/bin/python3

import sys

if len(sys.argv)<2:
    sys.exit("Please tell me your name")

name = sys.argv[1]
print(f"Hello, { name }")
```
#### loop.py
```python
for planet in ["merkurius", "venus", "maa", "mars"]:
    print(planet)

for i in range(0,10):
    print(i)
```
#### functiones.py
```python
def square(x):
    return x*x

if __name__ == "__main__":
    print(square(2))
```
#### importing.py
```python
from functiones import square

print(square(25))
class Animal():
    name = "Generic animal"

    def sound(self):
        return "Generic cute animal sounds"

animal = Animal()
animal.name
 = "Generissimus"
thingy = Animal()
thingy.name
 = "Thingimus"

print(animal.name)
print(animal.sound())
print(f"Thingimuses name: {thingy.name}")
```
#### classy.py
```python
class Animal():
    name = "Generic animal"

    def sound(self):
        return "Generic cute animal sounds"

class Lion(Animal):
    def sound(self):
        return "Rooaar!"

def main():
    lion = Lion()
    print(lion.sound())

if __name__ == "__main__":
    main()
```
#### scoping.py
Näkyvyyssäännöt
```python
def square(x):
    return x*x

def cube(x):
    return x*x*x

def main():
    print(square(2))
    print(cube(2))
    print(x)

main()
```
```python
def greet(name="Anomuumi", greeting="Hyvää päivää"):
    return f"{ greeting }, { name }"

print(greet(greeting="Heeeelloooo, "))
print(greet("Tero"))
def greet(name="Anomuumi"):
    return f"Hei, { name }"

name = "Tero"
print(greet(name=name))
```
