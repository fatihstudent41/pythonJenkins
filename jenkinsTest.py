class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age}, {self.id})"

people = []
for i in range(10):
    person = Person(f"Person {i}", i+20, i+1000)
    people.append(person)

for person in people:
    print(person)
    print(repr(person))
print("it is a jenkins & python test file")