class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i3 in self.my_list:
            for i4 in i3:
                print(f"{i4:6}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i2 in range(len(other.my_list[i])):
                self.my_list[i][i2] = self.my_list[i][i2] + other.my_list[i][i2]
        return Matrix.__str__(self)


m = Matrix([[-1, 0, 1], [-1, 1, 1], [6, 1, -1], [1, 2, -1]])
new_m = Matrix([[-2, 4, 1], [-2, 6, 2], [0, 4, -2], [2, 2, -5]])
print(m + new_m)