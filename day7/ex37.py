class Song(object):
    # The __init__ function is called every time an object is created from a class.
    # The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_mea_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                  "So I'll stop right there"
                   ])

happy_bday.sing_mea_a_song()
