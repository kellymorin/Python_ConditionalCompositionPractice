# In this exercises, you're going to use a conditional statement inside a comprehension.

# Define a set that contains tuples. Each tuple should contain two strings: The name of an artist, a song by that artist
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}


# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
not_nickelback = { song for song in songs if not "Nickelback" in song[0]}
print(not_nickelback)