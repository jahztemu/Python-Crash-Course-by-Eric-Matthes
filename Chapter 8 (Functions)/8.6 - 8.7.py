def city_country(city, country):
    """city and country"""
    place = f'"{city}, {country}"'
    return place.title()


result = city_country('London', 'UK')
print(result)
result = city_country('New York', 'USA')
print(result)
result = city_country('Lagos', 'Nigeria')
print(result)


def make_album(artist, album, song=None):
    """Album"""
    if song:
        album = {'Artist': artist, 'Title': album, 'songs': song}
        return album
    else:
        album = {'Artist': artist, 'Title': album}
        return album


latest = make_album('Dave', 'City life')
print(latest)
latest = make_album('Cardi B', 'The Queen', 8)
print(latest)
latest= make_album('Sia', 'Injustice', 5)
print(latest)