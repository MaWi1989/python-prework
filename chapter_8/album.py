def make_album(album_title, artist_name, tracks = ''):
    """Return a dictionary of information about an album."""
    album = {'Album':album_title.title(), 'Artist':artist_name.title()}

    if tracks:
        album['Tracks'] = tracks

    return album

album_made = make_album('midnights', 'taylor swift')
print(album_made)

album_made = make_album('sour', 'olivia rodrigo')
print(album_made)

album_made = make_album('meteora', 'linkin park')
print(album_made)

album_made = make_album('nevermind', 'nirvana', tracks = 10)
print(album_made)