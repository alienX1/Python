class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validTriangle(self):
        if (self.a + self.b >= self.c) and (self.b + self.b >= self.a) and (self.a + self.c >= self.b):
            return True
        else:
            return False

    def perimeter(self):
        P = self.a + self.b + self.c
        return P


side1 = int(input())
side2 = int(input())
side3 = int(input())

t1 = Triangle(side1, side2, side3)
if t1.validTriangle():
    print(f'Valid Triangle, with perimeter = {t1.perimeter()}')

else:
    print('Not a valid triangle')


# from functools import reduce
# words = ['mary', 'had', 'a', 'little', 'lamb']
# biggest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
# print(biggest_word)
