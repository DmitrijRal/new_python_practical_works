from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda row: ' '.join([str(number) for number in row]), self.matrix))

    def __add__(self, other):
        new_matrix = deepcopy(self.matrix)

        [new_matrix[key].__setitem__(inner_key, inner_value + other.matrix[key][inner_key]) for
         key, value in enumerate(self.matrix) for inner_key, inner_value in enumerate(value)]

        return Matrix(new_matrix)


print(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) +
      Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) +
      Matrix([[2, 5, 8], [3, 6, 9], [1, 4, 7]]))
