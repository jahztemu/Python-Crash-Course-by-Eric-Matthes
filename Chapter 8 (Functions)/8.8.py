def make_album(artist, album, song=None):
    """Album"""
    if song:
        album = {'Artist': artist, 'Title': album, 'songs': song}
        return album
    else:
        album = {'Artist': artist, 'Title': album}
        return album

while True:
    repeat = input('Would you Fill in an album? (yes/no)')
    if repeat.lower() == 'no':
        break
    artists = input('Please enter artist:')
    albums = input('Please enter album:')
    songs = input('Please enter song:')
    latest = make_album(artists,albums,songs)
    print(latest)