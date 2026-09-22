class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add a song
    def add_song(self, title, artist):
        new_song = SongNode(title, artist)

        if self.head is None:
            self.head = self.tail = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song

        print("Song added successfully!")

    # Display playlist
    def display_playlist(self):
        current = self.head
        count = 1

        print("\n----- MUSIC PLAYLIST -----")

        while current:
            print(
                count, ".",
                current.title,
                "-",
                current.artist
            )

            current = current.next
            count += 1


# Create playlist
playlist = Playlist()

# Add songs
playlist.add_song("Believer", "Imagine Dragons")
playlist.add_song("Perfect", "Ed Sheeran")
playlist.add_song("Faded", "Alan Walker")

# Display playlist
playlist.display_playlist()