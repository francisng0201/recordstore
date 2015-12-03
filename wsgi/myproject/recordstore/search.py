from .models import *

def LevenshteinDistance(s, t):
    # base case
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    # recursive case
    if s[-1:] == t[-1:]:
        cost = 0
    else:
        cost = 1
    delete_s = LevenshteinDistance(s[:-1], t) + 1
    delete_t = LevenshteinDistance(s, t[:-1]) + 1
    delete_both = LevenshteinDistance(s[:-1], t[:-1]) + cost 
    return min(delete_s, delete_t, delete_both)

def search_objects(search_string, class_name, start, stop, ic):
    """Will search by the .name property of your object"""
    if ic:
        search_string = search_string.lower()

    objects = class_name.objects.all()
    distances = []
    for obj in objects:
        name = obj.name
        if ic:
            name = name.lower()

        dist = LevenshteinDistance(search_string, name)
        distances.append((obj, dist))

    results = sorted(distances, key=lambda tup: tup[1])
    results = results[start:stop]
    return [ x[0] for x in results ]

def search_albums(search_string, start=0, stop=100, ic=False):
    return search_objects(search_string, Album, start, stop, ic)

def search_artists(search_string, start=0, stop=100, ic=False):
    return search_objects(search_string, Artist, start, stop, ic)
