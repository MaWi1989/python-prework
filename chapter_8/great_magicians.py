magicians = ['copperfield', 'hudini', 'shin lin']

def show_magicians(names):
    """Show list of magicans' names."""
    for name in names:
        name = name.title()
        print(name)

show_magicians(magicians)

print("\n")
def make_great(names):
    """add 'the Great' to each magician's name."""
    for name in names:
        name = name.title() + " the Great"
        print(name)

make_great(magicians)

print("\n")

great = make_great(magicians[:])

show_magicians(magicians)

show_magicians(great)


