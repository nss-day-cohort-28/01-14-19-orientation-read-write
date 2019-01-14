# w=write, r=read, a=append, r+ = read and write
with open("./data/test.txt", 'w') as testfile:
  testfile.write("Hello, C28. Hope you're having a great day.\n")

with open("./data/test.txt", 'a') as testfile:
  testfile.write("Hello, C28. Hope you're awake.\n")

# ==========
nickset = {"The Mooch", "Knuckles", "Burninator", "Kneecap", "Ole Red", "Bubba",
           "OG", "KitKat", "Spanky", "Monkeybutt", "L`il Devil", "Bird Person", "Fancy Slacks"}

nameset = {"Bob Smith", "Charise Anderson", "Jissie David", "Henry Goldberg", "Greg Korte", "Steve Brownlee", "Kimmy Bird", "Joe Shepherd", "Emily Lemmon", "Brenda Long", "Harold Brown", "Megan Ducharme", "Darth Vader"}

with open("data/nicknames.txt", "w") as nicknames:
  for nick in nickset:
    nicknames.write(nick + '\n')

with open("data/names.txt", "w") as names:
  for name in nameset:
    names.write(name + '\n')

# Later, in some other part of the app
with open('data/names.txt', "r") as names:
  namelist = names.readlines()

with open('data/nicknames.txt', "r") as nicks:
  nicklist = nicks.readlines()

# strip() method returns a copy of the string with both leading and trailing characters removed
# split() method splits a string into a list where each word is a list item
# slashes are escaping the double quotes. All Mob nicknames gotta have quotes around 'em!
# enumerate() method allows us to loop over something and have an automatic counter. So we can get an "i" like good old JS, and use that to access each item in nicknames
mob_names = [f"{name.strip().split(' ')[0]} \"{nicklist[i].strip()}\" {name.strip().split(' ')[1]}" for i, name in enumerate(namelist)]

print(mob_names)
