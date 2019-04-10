class Song(object):
    """docstring for Song."""

    def __init__(self, lyrics):
        super(Song, self).__init__()
        self.lyrics = lyrics

    def singMeASong(self):
        for line in self.lyrics:
            print(line)

happyBday = Song([
"Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"
])

bullsonParade = Song([
"They rally around the family",
"With pockets full of shells"
])

happyBday.singMeASong()

bullsonParade.singMeASong()
