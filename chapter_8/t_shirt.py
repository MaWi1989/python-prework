def make_shirt(size, text):
    """Make a t-shirt."""
    print("\nThis shirt is a size " + size + ".")
    print("\nThe shirt says " + "'" + text + "'.")

make_shirt('medium', 'It\'s wine o\'clock somewhere!')

make_shirt(size='large', text='meat lover')

print("\n")
def make_shirt(size='large', text='I love Python'):
    """Make a t-shirt."""
    print("\nThis shirt is a size " + size + ".")
    print("The shirt says " + "'" + text + "'.")

make_shirt()
make_shirt('medium', 'I love Python')
make_shirt(size='small', text='no thanks!')

