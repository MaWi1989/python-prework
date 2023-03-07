favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language is " + language.title() + ".")
    
for name in favorite_languages.keys():
    print(name.title())
print("\n")
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + 
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")
print("\n")
#to print names in order:
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("\n")

#to avoid repetition:
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")
people = ['mary','john','sarah','tom','phil']
for person in people:
    if person in favorite_languages.keys():
        print("Thank you for taking the survey, " + person.title() + "!")
    else:
        print(person.title() + ", please take our survey!")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else: 
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())

        