name = "Jane"
name = "Jess"
print(name)

# string formatting 

greeting = f"Hello, {name}!"
print(greeting)


greeting2 = "Hello, {}"
name = "Madam Jessica"
with_name = greeting2.format(name)
with_name_two = greeting2.format("Dan")
print(with_name_two)

longer_phrase = "Hello, {} this string demonstrates using multiple placeholders. Today is {} ."

formatted_phrase = longer_phrase.format("Jess", "Monday")
print(formatted_phrase)