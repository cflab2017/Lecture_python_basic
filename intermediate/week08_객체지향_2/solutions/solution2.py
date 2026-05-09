class Playlist:
    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def remove(self, song):
        self._songs.remove(song)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, idx):
        return self._songs[idx]

    def __contains__(self, song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

    def __repr__(self):
        return f"Playlist({len(self._songs)} songs)"

p = Playlist()
p.add("Bohemian Rhapsody")
p.add("Imagine")
p.add("Hotel California")
print(len(p))
print(p[0])
print("Imagine" in p)
for song in p:
    print("-", song)
print(p)
