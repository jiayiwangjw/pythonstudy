#Below are the two class definitions we supplied previously:
#Artist and Song.
#
#Write a function called "get_song_string". It should accept
#one argument which will be a Song object. It should return
#a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g: 
# "You Belong With Me" - Taylor Swift (2008)
#
#The quotation marks around the song title should be *part*
#of the string.
#
#Hint: You're writing a function, not a method. That means
#the function get_song_string should not be inside either
#of these classes.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist

def get_song_string(song):
    result = '\"' + song.name + '\"' + " " + "-" + " " + song.artist.name + " " + "(" + str(song.year) + ")"
    return result
        
#The code below will test your function. It isn't used for
#grading, so feel free to modify it.
newArtist = Artist("Taylor Swift", "Big Machine Records, LLC")
newSong = Song("You Belong With Me", "Fearless", 2008, newArtist)
print(get_song_string(newSong))


