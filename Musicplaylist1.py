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
        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head
        count = 1

        print("\n----- MUSIC PLAYLIST -----")

        while current:
            print(
                str(count) + ". " +
                current.title + " - " +
                current.artist
            )

            current = current.next
            count += 1

    # Search song
    def search_song(self, title):
        current = self.head

        while current:
            if current.title.lower() == title.lower():
                print("\nSong Found!")
                print("Title :", current.title)
                print("Artist:", current.artist)
                return current

            current = current.next

        print("Song not found.")
        return None

    # Delete song
    def delete_song(self, title):
        song = self.search_song(title)

        if song is None:
            return

        if song.prev:
            song.prev.next = song.next
        else:
            self.head = song.next

        if song.next:
            song.next.prev = song.prev
        else:
            self.tail = song.prev

        print("Song deleted successfully!")


# ---------------- MAIN PROGRAM ----------------

playlist = Playlist()

playlist.add_song("Believer", "Imagine Dragons")
playlist.add_song("Perfect", "Ed Sheeran")
playlist.add_song("Faded", "Alan Walker")

playlist.display_playlist()

print("\nSearching for Perfect:")
playlist.search_song("Perfect")

print("\nDeleting Faded:")
playlist.delete_song("Faded")

print("\nUpdated Playlist:")
playlist.display_playlist()