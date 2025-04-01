"""his program should store the birthdays of friends, allowing you to look them up by their name.

Requirements:

Create a Dictionary: Create a Python dictionary that stores names as keys and their corresponding birthdays as values.

Input and Output:

The program should first print a welcome message listing the names of the people whose birthdays are stored (as shown in the example interaction).
Then, it should ask the user to enter a friend's name to look up.
Finally, it should retrieve the birthday from the dictionary and print it to the console.
Example Interaction:

>>> Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:  (Welcome to the birthday dictionary. We know the birthdays of:)

Ana
Marija
Stefan
Aleksandar

>>> Koj rodenden e potrebno da se prebara? (Whose birthday do you want to find?)

Marija

>>> Rodendenot na Marija e na 17/01/1991 (Marija's birthday is on 17/01/1991)

"""

birthdays = {
    "Ana": "13/03/1999",
    "Marija": "17/01/1991",
    "Stefan": "11/08/1896",
    "Aleksandar": "25/10/1992"
}
print("Whos birthday do you want to know?")
print(', '.join(birthdays.keys()))
name=input()
birthday=birthdays[name];
print(f"The birthday of {name} is on {birthday}.")
