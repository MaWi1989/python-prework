def make_album(album_title, artist_name):
    """Return a dictionary of information about an album."""
    album = {'Album':album_title.title(), 'Artist':artist_name.title()}
    return album

polling_active = True

while True:
    print("What is your favorite album? ")
    print("(Enter 'q' at any time to quit.)")

    album_title = input("Favorite album: ")
    if album_title == 'q':
        break

    artist_name = input("Artist: ")
    if artist_name == 'q':
        break

    favorite_album = make_album(album_title, artist_name)
    print(favorite_album)