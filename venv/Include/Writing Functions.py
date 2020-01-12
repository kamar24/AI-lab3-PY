def speak_excitedly(message, exclamations=1, capitalize=False):
    message += '!' * exclamations
    if capitalize:
        return message.upper()
    return message

message = "I love Python"
message1 = "Keyword arguments are great"
message2 = "I guess Java is okay..."
message3 = "Let's go Stanford"

print(speak_excitedly(message=message, exclamations=1, capitalize=False))
print(speak_excitedly(message=message1, exclamations=4, capitalize=False))
print(speak_excitedly(message=message2, exclamations=0, capitalize=False))
print(speak_excitedly(message=message3, exclamations=2, capitalize=True))
#Exclamations= wykrzyniki
#Capitalize= capslock

print("\n")

