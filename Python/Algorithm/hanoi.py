class Plate:
    def __init__(self, size):
        self.size = size


class Pole:
    def __init__(self, name, n):
        self.name = name
        self.plates = [Plate(i) for i in range(n, 0, -1)]


class Hanoi:
    def __init__(self, n):
        self.start = Pole('start', n)
        self.end = Pole('end', 0)
        self.temp = Pole('temp', 0)

    def move(self, start, end):
        plate = start.plates.pop()
        end.plates.append(plate)
        print('move {} from {} to {}'.format(plate.size, start.name, end.name))

    def move_n(self, start, end, temp, n):
        if n == 0:
            return
        self.move_n(start, temp, end, n - 1)
        self.move(start, end)
        self.move_n(temp, end, start, n - 1)


n = 64
hanoi = Hanoi(n)
hanoi.move_n(hanoi.start, hanoi.end, hanoi.temp, n)
