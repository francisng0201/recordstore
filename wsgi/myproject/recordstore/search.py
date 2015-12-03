from .models import *


def count_matches(s, t):
    num_matches = 0.0
    num_transposes = 0.0
    window_size = (max(len(s), len(t)) / 2) - 1
    last_match_pos = 0

    for s_pos in range(len(s)):
        s_char = s[s_pos]
        start = max(0, s_pos - window_size)
        end =  min(len(t), s_pos + window_size + 1)
        for t_pos in range(start, end):
            if s_char == t[t_pos]:
                if t_pos < last_match_pos:
                    num_transposes += 1.0
                else:
                    num_matches += 1.0
                    last_match_pos = t_pos
                    break

    return (num_matches, num_transposes)

def distance(s, t):
    # base case
    matches, trans = count_matches(s, t)

    if matches == 0:
        return 0
    else:
        distance = 0.3 * ((matches / len(s)) + (matches/len(t)) + ((matches - trans)/ matches))
        return distance

def rank(s, t):
    p = 0.0
    for i in range(min(len(s), len(t), 4)):
        if s[i] == t[i]:
            p += 1.0

    dist = distance(s, t)
    return dist + p * 0.1 * dist

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

        dist = rank(search_string, name)
        distances.append((obj, dist))

    results = sorted(distances, key=lambda tup: tup[1], reverse=True)
    results = results[start:stop]
    return [ x[0] for x in results ]

def search_albums(search_string, start=0, stop=100, ic=False):
    return search_objects(search_string, Album, start, stop, ic)

def search_artists(search_string, start=0, stop=100, ic=False):
    return search_objects(search_string, Artist, start, stop, ic)
