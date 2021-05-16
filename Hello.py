class Hello:
    def __init__(self,greeting="Hello"):
        self.greeting=greeting
    def greet(self, person):
        return print("{} {}".format(self.greeting,person))


def hello(person,greeting="Hello"):

    return print ("{} {}".format(greeting,person))

hello("Text", "Hi")

new=Hello("Hi")
new.greet("Bartek")
new.greeting="Hello"
new.greet("xyz")