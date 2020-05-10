noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
if not noun.isalpha() or not verb.isalpha() or not adjective.isalpha() or not adverb.isalpha():
    print("Only Letters are allowed!")

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's Hilarious!")
