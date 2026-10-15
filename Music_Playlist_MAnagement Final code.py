import tkinter as tk
from tkinter import messagebox

# ---------------- DOUBLY LINKED LIST ----------------

head = None
tail = None
current = None
song_id = 1


def add_song(title, artist):
    global head, tail, song_id, current

    title = title.strip()
    artist = artist.strip()

    if not title or not artist:
        messagebox.showwarning(
            "Missing Information",
            "Please enter both song title and artist."
        )
        return

    new_song = {
        "id": song_id,
        "title": title,
        "artist": artist,
        "prev": None,
        "next": None
    }

    if head is None:
        head = tail = new_song
        current = new_song
    else:
        new_song["prev"] = tail
        tail["next"] = new_song
        tail = new_song

    song_id += 1

    title_entry.delete(0, tk.END)
    artist_entry.delete(0, tk.END)

    refresh_playlist()
    show_current_song()


def delete_song(sid):
    global head, tail, current

    temp = head

    while temp:
        if temp["id"] == sid:

            if temp["prev"]:
                temp["prev"]["next"] = temp["next"]
            else:
                head = temp["next"]

            if temp["next"]:
                temp["next"]["prev"] = temp["prev"]
            else:
                tail = temp["prev"]

            if current is temp:
                current = temp["next"] or temp["prev"]

            refresh_playlist()
            show_current_song()
            return

        temp = temp["next"]


def search_song():
    query = search_entry.get().strip().lower()

    if not query:
        messagebox.showinfo("Search", "Enter a song title.")
        return

    temp = head

    while temp:
        if query in temp["title"].lower():
            messagebox.showinfo(
                "Song Found",
                f"Title: {temp['title']}\nArtist: {temp['artist']}"
            )
            return

        temp = temp["next"]

    messagebox.showinfo("Search", "No matching song found.")


def next_song():
    global current

    if current and current["next"]:
        current = current["next"]
        show_current_song()
        select_current_in_list()
    else:
        messagebox.showinfo("Playlist", "No next song available.")


def previous_song():
    global current

    if current and current["prev"]:
        current = current["prev"]
        show_current_song()
        select_current_in_list()
    else:
        messagebox.showinfo(
            "Playlist",
            "No previous song available."
        )


def show_current_song():
    if current:
        now_title.config(text=current["title"])
        now_artist.config(text="by " + current["artist"])
    else:
        now_title.config(text="No song selected")
        now_artist.config(text="Add songs to get started")


def refresh_playlist():
    playlist_box.delete(0, tk.END)

    temp = head
    count = 0

    while temp:
        playlist_box.insert(
            tk.END,
            f"  {temp['title']}  —  {temp['artist']}"
        )
        count += 1
        temp = temp["next"]

    total_label.config(text=f"TOTAL SONGS: {count}")


def select_current_in_list():
    if not current:
        return

    index = 0
    temp = head

    while temp:
        if temp["id"] == current["id"]:
            playlist_box.selection_clear(0, tk.END)
            playlist_box.selection_set(index)
            playlist_box.see(index)
            break

        index += 1
        temp = temp["next"]


def play_selected_song(event=None):
    global current

    selection = playlist_box.curselection()

    if not selection:
        return

    index = selection[0]
    temp = head

    for _ in range(index):
        if temp:
            temp = temp["next"]

    if temp:
        current = temp
        show_current_song()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("MelodyFlow | Music Playlist")
root.geometry("850x650")
root.minsize(750, 600)
root.configure(bg="#10121C")


# ---------------- HEADER ----------------

header = tk.Frame(root, bg="#191C2B", pady=18)
header.pack(fill="x")

logo = tk.Label(
    header,
    text="♫  MELODYFLOW",
    font=("Arial", 23, "bold"),
    fg="#A78BFA",
    bg="#191C2B"
)
logo.pack()

subtitle = tk.Label(
    header,
    text="YOUR MUSIC. YOUR MOOD.",
    font=("Arial", 9, "bold"),
    fg="#B0B5CC",
    bg="#191C2B"
)
subtitle.pack(pady=(4, 0))


# ---------------- CURRENT SONG ----------------

player = tk.Frame(root, bg="#22263A", padx=20, pady=18)
player.pack(fill="x", padx=25, pady=18)

tk.Label(
    player,
    text="NOW SELECTED",
    font=("Arial", 9, "bold"),
    fg="#A78BFA",
    bg="#22263A"
).pack()

now_title = tk.Label(
    player,
    text="No song selected",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#22263A"
)
now_title.pack(pady=(8, 2))

now_artist = tk.Label(
    player,
    text="Add songs to get started",
    font=("Arial", 11),
    fg="#B0B5CC",
    bg="#22263A"
)
now_artist.pack()


# ---------------- PLAYER BUTTONS ----------------

controls = tk.Frame(player, bg="#22263A")
controls.pack(pady=12)


def make_button(parent, text, command, color="#7C3AED"):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg=color,
        fg="white",
        activebackground="#5B21B6",
        activeforeground="white",
        relief="flat",
        padx=16,
        pady=8,
        cursor="hand2"
    )


make_button(
    controls, "⏮ Previous", previous_song, "#343951"
).pack(side="left", padx=7)

make_button(
    controls, "Next ⏭", next_song, "#7C3AED"
).pack(side="left", padx=7)


# ---------------- ADD SONG SECTION ----------------

content = tk.Frame(root, bg="#10121C")
content.pack(fill="both", expand=True, padx=25)

left_panel = tk.Frame(
    content, bg="#191C2B", padx=18, pady=15
)
left_panel.pack(side="left", fill="y", padx=(0, 12))

tk.Label(
    left_panel,
    text="ADD A SONG",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="#191C2B"
).pack(anchor="w", pady=(0, 15))


tk.Label(
    left_panel,
    text="Song Title",
    fg="#B0B5CC",
    bg="#191C2B"
).pack(anchor="w")

title_entry = tk.Entry(
    left_panel,
    font=("Arial", 11),
    width=24,
    bg="#292D42",
    fg="white",
    insertbackground="white",
    relief="flat"
)
title_entry.pack(pady=(5, 12), ipady=7)


tk.Label(
    left_panel,
    text="Artist Name",
    fg="#B0B5CC",
    bg="#191C2B"
).pack(anchor="w")

artist_entry = tk.Entry(
    left_panel,
    font=("Arial", 11),
    width=24,
    bg="#292D42",
    fg="white",
    insertbackground="white",
    relief="flat"
)
artist_entry.pack(pady=(5, 14), ipady=7)


make_button(
    left_panel, "+ Add Song",
    lambda: add_song(
        title_entry.get(),
        artist_entry.get()
    )
).pack(fill="x", pady=5)


tk.Label(
    left_panel,
    text="SEARCH SONG",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#191C2B"
).pack(anchor="w", pady=(25, 10))


search_entry = tk.Entry(
    left_panel,
    font=("Arial", 11),
    width=24,
    bg="#292D42",
    fg="white",
    insertbackground="white",
    relief="flat"
)
search_entry.pack(pady=(0, 10), ipady=7)


make_button(
    left_panel, "⌕ Search",
    search_song, "#343951"
).pack(fill="x")


# ---------------- PLAYLIST SECTION ----------------

right_panel = tk.Frame(
    content, bg="#191C2B", padx=15, pady=15
)
right_panel.pack(side="left", fill="both", expand=True)

playlist_header = tk.Frame(right_panel, bg="#191C2B")
playlist_header.pack(fill="x", pady=(0, 10))

tk.Label(
    playlist_header,
    text="YOUR PLAYLIST",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="#191C2B"
).pack(side="left")

total_label = tk.Label(
    playlist_header,
    text="TOTAL SONGS: 0",
    font=("Arial", 8, "bold"),
    fg="#A78BFA",
    bg="#191C2B"
)
total_label.pack(side="right")


list_frame = tk.Frame(right_panel, bg="#191C2B")
list_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

playlist_box = tk.Listbox(
    list_frame,
    font=("Arial", 10),
    bg="#22263A",
    fg="white",
    selectbackground="#7C3AED",
    selectforeground="white",
    relief="flat",
    activestyle="none",
    yscrollcommand=scrollbar.set
)
playlist_box.pack(side="left", fill="both", expand=True)

scrollbar.config(command=playlist_box.yview)

playlist_box.bind("<<ListboxSelect>>", play_selected_song)


def delete_selected_song():
    selection = playlist_box.curselection()

    if not selection:
        messagebox.showwarning(
            "Delete Song",
            "Select a song from the playlist first."
        )
        return

    index = selection[0]
    temp = head

    for _ in range(index):
        if temp:
            temp = temp["next"]

    if temp:
        delete_song(temp["id"])


make_button(
    right_panel, "🗑 Delete Selected Song",
    delete_selected_song, "#B83250"
).pack(fill="x", pady=(12, 0))


# ---------------- FOOTER ----------------

footer = tk.Label(
    root,
    text="Built with Python  |  Doubly Linked List",
    font=("Arial", 9),
    fg="#777F9D",
    bg="#10121C",
    pady=12
)
footer.pack(fill="x")


# ---------------- RUN APPLICATION ----------------

root.mainloop()