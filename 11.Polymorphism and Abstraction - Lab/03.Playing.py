def start_playing(obj):
    return obj.play()


class Children:
    @staticmethod
    def play():
        return "Children are playing"


children = Children()

print(start_playing(children))
