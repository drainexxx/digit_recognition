class Point:

    # Функция для выбора проверяемго столбца в матрице 3x3 на вертикальную линию
    @staticmethod
    def select_a_column(mas):
        ves_mat = mas
        ves_mat_id = (int(input("Введите по какому столбцу будет проверка(отчет идет с 0):")))

        if ves_mat_id == 0:
            for i in range(3):
                ves_mat[i][0] = 1
                ves_mat[i][1] = -0.1
                ves_mat[i][2] = -1

        elif ves_mat_id == 1:

            for i in range(3):
                ves_mat[i][0] = -0.2
                ves_mat[i][1] = 1
                ves_mat[i][2] = -0.2

        elif ves_mat_id == 2:

            for i in range(3):
                ves_mat[i][0] = -1
                ves_mat[i][1] = -0.1
                ves_mat[i][2] = 1

        return ves_mat

    # Функция для перемножения матрицы весов на матрицу значений матрицы 3x3
    @staticmethod
    def matrix_multiplication_3x3(A, mat_ves):

        matrix_fin = ([0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0])

        for i in range(3):
            for j in range(3):
                matrix_fin[i][j] = A[i][j] * mat_ves[i][j]

        return matrix_fin

    # Функция для суммирования получившихся значений, а затем применения функции активации
    @staticmethod
    def apply_activation_function(fin_mat):
        S = 0
        for i in fin_mat:
            S = sum(i) + S

        act = 1 / (1 + (3 - S) * 2 + 2.718 ** (-S))
        if 0.6 <= act <= 1:
            print(f'Вероятность: {act}')
            print('True')
            return act
        else:
            print(f'Вероятность: {act}')
            print('False')
            return act

A = ([1, 1, 0],
     [1, 1, 0],
     [1, 0, 0])

B = ([1, 1, 0],
     [1, 1, 0],
     [1, 0, 0])

ves_mat = Point.select_a_column(A) # Определяем веса

fin_mat = Point.matrix_multiplication_3x3(B, ves_mat) # умножение матрицы значений на матрицу весов

result = Point.apply_activation_function(fin_mat) # сумирование и применение функции активации

print(result)