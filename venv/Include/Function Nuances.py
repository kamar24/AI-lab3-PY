def say_hello():
    print("Hello!")

print(say_hello())
def echo(arg=None):
    print("arg:", arg)
    return arg
print(echo())  # => arg: None None
print(echo(5)) # => arg: 5 5
print(echo("Hello")) # => arg: Hello Hello



def drive(has_car):
    if not has_car:
        return
    return 100  # miles


print(drive(False))  # => None
print(drive(True))   # => 100