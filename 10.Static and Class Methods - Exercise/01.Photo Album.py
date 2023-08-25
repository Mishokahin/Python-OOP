from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count/4))

    def add_photo(self, label: str):
        for p in range(self.pages):
            if len(self.photos[p]) < 4:
                self.photos[p].append(label)
                return f"{label} photo added successfully on page {p + 1} slot {len(self.photos[p])}"

        return "No more free slots"

    def display(self):
        result = f"{'-' * 11}"
        for i in range(self.pages):
            result += f"\n{' '.join('[]' for _ in range(len(self.photos[i])))}" + f"\n{'-' * 11}"

        return result


album = PhotoAlbum(1)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())