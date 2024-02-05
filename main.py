from tkinter import *

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


# Класс для работы с интерфейсом
class Entering_values:

    @staticmethod
    def window_output(con_res='d'):

        def calculating_probability():
            matr_zn = ([int(btn0_0['text']),int(btn0_1['text']), int(btn0_2['text']),int(btn0_3['text'])],
                       [int(btn1_0['text']),int(btn1_1['text']), int(btn1_2['text']),int(btn1_3['text'])],
                       [int(btn2_0['text']),int(btn2_1['text']), int(btn2_2['text']),int(btn2_3['text'])],
                       [int(btn3_0['text']),int(btn3_1['text']), int(btn3_2['text']),int(btn3_3['text'])],
                       [int(btn4_0['text']),int(btn4_1['text']), int(btn4_2['text']),int(btn4_3['text'])],
                       [int(btn5_0['text']),int(btn5_1['text']), int(btn5_2['text']),int(btn5_3['text'])])

            print(matr_zn)

            ves_0 =([-10, 3, 3, -10],
                    [3, -30, -30, 3],
                    [3, -30, -30, 3],
                    [3, -30, -30, 3],
                    [3, -30, -30, 3],
                    [-10, 3, 3, -10])
            ves_1 = ([-25, -20, -2, 4],
                    [-10, -1, 4, 2],
                    [-2, 2, -1, 2],
                    [2, -5, -1, 2],
                    [-10, -20, 0, 2],
                    [-5, -5, -2, 5])
            ves_2 =([-5, 4, 5, -5],
                    [3, -20, -15, 4],
                    [3, -20, -3, 3],
                    [-20, -3, 3, -20],
                    [-3, 3, -12, -15],
                    [3, 3, 4, 4])
            ves_3 =([-2, 3, 3, 0],
                    [0, -20, -20, 5],
                    [-30, 0, 3, -1],
                    [-30, -8, -2, 5],
                    [3, -5, -6, 3],
                    [-5, 3, 3, 3])
            ves_4 =([3, 0, -5, 3],
                    [3, 0, -5, 3],
                    [3, 3, 3, 3],
                    [-20, -20, -5, 3],
                    [-20, -20, -5, 3],
                    [-20, -20, -5, 3])
            ves_5 =([2, 2, 2, 2],
                    [2, -6, -20, -15],
                    [2, 2, 2, -6],
                    [-20, -10, -4, 2],
                    [-9, -20, -15, 2],
                    [2, 2, 2, -8])
            ves_6 =([-10, 3, 3, -5],
                    [3, -10, -20, 3],
                    [3, -10, -25, -30],
                    [12, 3, 3, -20],
                    [3, -25, -9, 3],
                    [-10, 3, 3, -10])
            ves_7 =([3, 3, 3, 5],
                    [-10, -20, -5, 6],
                    [-20, -5, 3, -5],
                    [-20, -5, 3, -5],
                    [-5, 3, -9, -5],
                    [-15, 3, -15, -5])
            ves_8 =([-8, 2, 2, -8],
                    [3, -20, -20, 2],
                    [-6, 2, 2, -6],
                    [3, -20, -20, 2],
                    [3, -20, -20, 2],
                    [-6, 3, 3, -6])
            ves_9 =([-3, 3, 3, 0],
                    [4, -20, -20, 3],
                    [4, -10, -9, 5],
                    [-15, 4, 4, 4],
                    [-20, -20, -15, 4],
                    [-6, 3, 3, -6])

            def vx_zn_zn(matr_zn, ves_matr):
                vx_zn = ([0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0])
                for i in range(6):
                    for j in range(4):
                        vx_zn[i][j] = matr_zn[i][j]*ves_matr[i][j]

                S = 0
                for i in vx_zn:
                    S = sum(i) + S

                act = 1 / (1 + 2.718 ** (-S/10))
                if 0.6 <= act <= 1:
                    print(f'Вероятность: {act}')
                    print('True')
                    return act
                else:
                    print(f'Вероятность: {act}')
                    print('False')
                    return act

            itog_0 = vx_zn_zn(matr_zn, ves_0)
            itog_1 = vx_zn_zn(matr_zn, ves_1)
            itog_2 = vx_zn_zn(matr_zn, ves_2)
            itog_3 = vx_zn_zn(matr_zn, ves_3)
            itog_4 = vx_zn_zn(matr_zn, ves_4)
            itog_5 = vx_zn_zn(matr_zn, ves_5)
            itog_6 = vx_zn_zn(matr_zn, ves_6)
            itog_7 = vx_zn_zn(matr_zn, ves_7)
            itog_8 = vx_zn_zn(matr_zn, ves_8)
            itog_9 = vx_zn_zn(matr_zn, ves_9)

            for i in (itog_0, itog_1, itog_2, itog_3, itog_4, itog_5, itog_6, itog_7, itog_8, itog_9):
                try:
                    if i > i_max:
                        i_max = i
                except:
                    i_max = i

            num = 'пока ничему'
            if i_max == itog_0:
                num = '0'
            elif i_max == itog_1:
                num = '1'
            elif i_max == itog_2:
                num = '2'
            elif i_max == itog_3:
                num = '3'
            elif i_max == itog_4:
                num = '4'
            elif i_max == itog_5:
                num = '5'
            elif i_max == itog_6:
                num = '6'
            elif i_max == itog_7:
                num = '7'
            elif i_max == itog_8:
                num = '8'
            elif i_max == itog_9:
                num = '9'

            if i_max < 0.15:
                num = "Наверное, это каракули"

            res = f'вероятность того, что цифра 0: {itog_0*100}%\n\n' \
                  f'вероятность того, что цифра 1: {itog_1*100}%\n\n' \
                  f'вероятность того, что цифра 2: {itog_2*100}%\n\n' \
                  f'вероятность того, что цифра 3: {itog_3*100}%\n\n' \
                  f'вероятность того, что цифра 4: {itog_4*100}%\n\n' \
                  f'вероятность того, что цифра 5: {itog_5*100}%\n\n' \
                  f'вероятность того, что цифра 6: {itog_6*100}%\n\n' \
                  f'вероятность того, что цифра 7: {itog_7*100}%\n\n' \
                  f'вероятность того, что цифра 8: {itog_8*100}%\n\n' \
                  f'вероятность того, что цифра 9: {itog_9*100}%\n\n' \
                  f'Наиболее вероятно, что это цифра: {num}\n\n'
            btn_con['text'] = res

        def clicked_0_0():
            if (btn0_0["text"] == "0"):
                btn0_0["text"] = "1"
                btn0_0['fg'] = "#007FFF"
                btn0_0['bg'] = "#007FFF"
            else:
                btn0_0["text"] = "0"
                btn0_0['fg'] = "#7FFF00"
                btn0_0['bg'] = "#7FFF00"

        def clicked_0_1():
            if (btn0_1["text"] == "0"):
                btn0_1["text"] = "1"
                btn0_1['fg'] = "#007FFF"
                btn0_1['bg'] = "#007FFF"
            else:
                btn0_1["text"] = "0"
                btn0_1['fg'] = "#7FFF00"
                btn0_1['bg'] = "#7FFF00"

        def clicked_0_2():
            if (btn0_2["text"] == "0"):
                btn0_2["text"] = "1"
                btn0_2['fg'] = "#007FFF"
                btn0_2['bg'] = "#007FFF"
            else:
                btn0_2["text"] = "0"
                btn0_2['fg'] = "#7FFF00"
                btn0_2['bg'] = "#7FFF00"

        def clicked_0_3():
            if (btn0_3["text"] == "0"):
                btn0_3["text"] = "1"
                btn0_3['fg'] = "#007FFF"
                btn0_3['bg'] = "#007FFF"
            else:
                btn0_3["text"] = "0"
                btn0_3['fg'] = "#7FFF00"
                btn0_3['bg'] = "#7FFF00"

        def clicked_1_0():
            if (btn1_0["text"] == "0"):
                btn1_0["text"] = "1"
                btn1_0['fg'] = "#007FFF"
                btn1_0['bg'] = "#007FFF"
            else:
                btn1_0["text"] = "0"
                btn1_0['fg'] = "#7FFF00"
                btn1_0['bg'] = "#7FFF00"

        def clicked_1_1():
            if (btn1_1["text"] == "0"):
                btn1_1["text"] = "1"
                btn1_1['fg'] = "#007FFF"
                btn1_1['bg'] = "#007FFF"
            else:
                btn1_1["text"] = "0"
                btn1_1['fg'] = "#7FFF00"
                btn1_1['bg'] = "#7FFF00"

        def clicked_1_2():
            if (btn1_2["text"] == "0"):
                btn1_2["text"] = "1"
                btn1_2['fg'] = "#007FFF"
                btn1_2['bg'] = "#007FFF"
            else:
                btn1_2["text"] = "0"
                btn1_2['fg'] = "#7FFF00"
                btn1_2['bg'] = "#7FFF00"

        def clicked_1_3():
            if (btn1_3["text"] == "0"):
                btn1_3["text"] = "1"
                btn1_3['fg'] = "#007FFF"
                btn1_3['bg'] = "#007FFF"
            else:
                btn1_3["text"] = "0"
                btn1_3['fg'] = "#7FFF00"
                btn1_3['bg'] = "#7FFF00"

        def clicked_2_0():
            if (btn2_0["text"] == "0"):
                btn2_0["text"] = "1"
                btn2_0['fg'] = "#007FFF"
                btn2_0['bg'] = "#007FFF"
            else:
                btn2_0["text"] = "0"
                btn2_0['fg'] = "#7FFF00"
                btn2_0['bg'] = "#7FFF00"

        def clicked_2_1():
            if (btn2_1["text"] == "0"):
                btn2_1["text"] = "1"
                btn2_1['fg'] = "#007FFF"
                btn2_1['bg'] = "#007FFF"
            else:
                btn2_1["text"] = "0"
                btn2_1['fg'] = "#7FFF00"
                btn2_1['bg'] = "#7FFF00"

        def clicked_2_2():
            if (btn2_2["text"] == "0"):
                btn2_2["text"] = "1"
                btn2_2['fg'] = "#007FFF"
                btn2_2['bg'] = "#007FFF"
            else:
                btn2_2["text"] = "0"
                btn2_2['fg'] = "#7FFF00"
                btn2_2['bg'] = "#7FFF00"

        def clicked_2_3():
            if (btn2_3["text"] == "0"):
                btn2_3["text"] = "1"
                btn2_3['fg'] = "#007FFF"
                btn2_3['bg'] = "#007FFF"
            else:
                btn2_3["text"] = "0"
                btn2_3['fg'] = "#7FFF00"
                btn2_3['bg'] = "#7FFF00"

        def clicked_3_0():
            if (btn3_0["text"] == "0"):
                btn3_0["text"] = "1"
                btn3_0['fg'] = "#007FFF"
                btn3_0['bg'] = "#007FFF"
            else:
                btn3_0["text"] = "0"
                btn3_0['fg'] = "#7FFF00"
                btn3_0['bg'] = "#7FFF00"

        def clicked_3_1():
            if (btn3_1["text"] == "0"):
                btn3_1["text"] = "1"
                btn3_1['fg'] = "#007FFF"
                btn3_1['bg'] = "#007FFF"
            else:
                btn3_1["text"] = "0"
                btn3_1['fg'] = "#7FFF00"
                btn3_1['bg'] = "#7FFF00"

        def clicked_3_2():
            if (btn3_2["text"] == "0"):
                btn3_2["text"] = "1"
                btn3_2['fg'] = "#007FFF"
                btn3_2['bg'] = "#007FFF"
            else:
                btn3_2["text"] = "0"
                btn3_2['fg'] = "#7FFF00"
                btn3_2['bg'] = "#7FFF00"

        def clicked_3_3():
            if (btn3_3["text"] == "0"):
                btn3_3["text"] = "1"
                btn3_3['fg'] = "#007FFF"
                btn3_3['bg'] = "#007FFF"
            else:
                btn3_3["text"] = "0"
                btn3_3['fg'] = "#7FFF00"
                btn3_3['bg'] = "#7FFF00"

        def clicked_4_0():
            if (btn4_0["text"] == "0"):
                btn4_0["text"] = "1"
                btn4_0['fg'] = "#007FFF"
                btn4_0['bg'] = "#007FFF"
            else:
                btn4_0["text"] = "0"
                btn4_0['fg'] = "#7FFF00"
                btn4_0['bg'] = "#7FFF00"

        def clicked_4_1():
            if (btn4_1["text"] == "0"):
                btn4_1["text"] = "1"
                btn4_1['fg'] = "#007FFF"
                btn4_1['bg'] = "#007FFF"
            else:
                btn4_1["text"] = "0"
                btn4_1['fg'] = "#7FFF00"
                btn4_1['bg'] = "#7FFF00"

        def clicked_4_2():
            if (btn4_2["text"] == "0"):
                btn4_2["text"] = "1"
                btn4_2['fg'] = "#007FFF"
                btn4_2['bg'] = "#007FFF"
            else:
                btn4_2["text"] = "0"
                btn4_2['fg'] = "#7FFF00"
                btn4_2['bg'] = "#7FFF00"

        def clicked_4_3():
            if (btn4_3["text"] == "0"):
                btn4_3["text"] = "1"
                btn4_3['fg'] = "#007FFF"
                btn4_3['bg'] = "#007FFF"
            else:
                btn4_3["text"] = "0"
                btn4_3['fg'] = "#7FFF00"
                btn4_3['bg'] = "#7FFF00"

        def clicked_5_0():
            if (btn5_0["text"] == "0"):
                btn5_0["text"] = "1"
                btn5_0['fg'] = "#007FFF"
                btn5_0['bg'] = "#007FFF"
            else:
                btn5_0["text"] = "0"
                btn5_0['fg'] = "#7FFF00"
                btn5_0['bg'] = "#7FFF00"

        def clicked_5_1():
            if (btn5_1["text"] == "0"):
                btn5_1["text"] = "1"
                btn5_1['fg'] = "#007FFF"
                btn5_1['bg'] = "#007FFF"
            else:
                btn5_1["text"] = "0"
                btn5_1['fg'] = "#7FFF00"
                btn5_1['bg'] = "#7FFF00"

        def clicked_5_2():
            if (btn5_2["text"] == "0"):
                btn5_2["text"] = "1"
                btn5_2['fg'] = "#007FFF"
                btn5_2['bg'] = "#007FFF"
            else:
                btn5_2["text"] = "0"
                btn5_2['fg'] = "#7FFF00"
                btn5_2['bg'] = "#7FFF00"

        def clicked_5_3():
            if (btn5_3["text"] == "0"):
                btn5_3["text"] = "1"
                btn5_3['fg'] = "#007FFF"
                btn5_3['bg'] = "#007FFF"
            else:
                btn5_3["text"] = "0"
                btn5_3['fg'] = "#7FFF00"
                btn5_3['bg'] = "#7FFF00"

        def clicked_opr_ver():
            if (btn5_3["text"] == "0"):
                btn5_3["text"] = "1"
                btn5_3['fg'] = "#007FFF"
                btn5_3['bg'] = "#007FFF"
            else:
                btn5_3["text"] = "0"
                btn5_3['fg'] = "#7FFF00"
                btn5_3['bg'] = "#7FFF00"

        window = Tk()
        window.title("Приложение для распознования цифры")
        window.geometry('740x660')

        lbl = Label(window, text="Введите пожалуйста цифру:", font=("Arial Bold", 16))
        lbl.grid(column=0, row=0, columnspan=4)


        btn0_0 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_0_0, height=1, width=3, font=("Arial Bold", 40))
        btn0_1 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_0_1, height=1, width=3, font=("Arial Bold", 40))
        btn0_2 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_0_2, height=1, width=3, font=("Arial Bold", 40))
        btn0_3= Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_0_3, height=1, width=3, font=("Arial Bold", 40))

        btn1_0 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_1_0, height=1, width=3, font=("Arial Bold", 40))
        btn1_1 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_1_1, height=1, width=3, font=("Arial Bold", 40))
        btn1_2 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_1_2, height=1, width=3, font=("Arial Bold", 40))
        btn1_3 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_1_3, height=1, width=3, font=("Arial Bold", 40))

        btn2_0 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_2_0, height=1, width=3, font=("Arial Bold", 40))
        btn2_1 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_2_1, height=1, width=3, font=("Arial Bold", 40))
        btn2_2 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_2_2, height=1, width=3, font=("Arial Bold", 40))
        btn2_3 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_2_3, height=1, width=3, font=("Arial Bold", 40))

        btn3_0 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_3_0, height=1, width=3, font=("Arial Bold", 40))
        btn3_1 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_3_1, height=1, width=3, font=("Arial Bold", 40))
        btn3_2 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_3_2, height=1, width=3, font=("Arial Bold", 40))
        btn3_3 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_3_3, height=1, width=3, font=("Arial Bold", 40))

        btn4_0 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_4_0, height=1, width=3, font=("Arial Bold", 40))
        btn4_1 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_4_1, height=1, width=3, font=("Arial Bold", 40))
        btn4_2 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_4_2, height=1, width=3, font=("Arial Bold", 40))
        btn4_3 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_4_3, height=1, width=3, font=("Arial Bold", 40))

        btn5_0 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_5_0, height=1, width=3, font=("Arial Bold", 40))
        btn5_1 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_5_1, height=1, width=3, font=("Arial Bold", 40))
        btn5_2 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_5_2, height=1, width=3, font=("Arial Bold", 40))
        btn5_3 = Button(window, text="0", bg="#7FFF00", fg="#7FFF00", command=clicked_5_3, height=1, width=3, font=("Arial Bold", 40))

        btn_opr_ver = Button(window, text="Нажмите, чтобы\n увидеть результат!", bg="#458B00", fg="#F5F5DC", command=calculating_probability, height=8, width=16, font=("Arial Bold", 24))
        btn_con = Button(window, text="Пока нет значений", bg="#F5F5DC", fg="#458B00", command=clicked_opr_ver, height=22, width=50, font=("Arial Bold", 8))


        # txt = Entry(window, width=10)
        # txt.grid(column=1, row=0)
        btn0_0.grid(column=0, row=1)
        btn0_1.grid(column=1, row=1)
        btn0_2.grid(column=2, row=1)
        btn0_3.grid(column=3, row=1)

        btn1_0.grid(column=0, row=2)
        btn1_1.grid(column=1, row=2)
        btn1_2.grid(column=2, row=2)
        btn1_3.grid(column=3, row=2)

        btn2_0.grid(column=0, row=3)
        btn2_1.grid(column=1, row=3)
        btn2_2.grid(column=2, row=3)
        btn2_3.grid(column=3, row=3)

        btn3_0.grid(column=0, row=4)
        btn3_1.grid(column=1, row=4)
        btn3_2.grid(column=2, row=4)
        btn3_3.grid(column=3, row=4)

        btn4_0.grid(column=0, row=5)
        btn4_1.grid(column=1, row=5)
        btn4_2.grid(column=2, row=5)
        btn4_3.grid(column=3, row=5)

        btn5_0.grid(column=0, row=6)
        btn5_1.grid(column=1, row=6)
        btn5_2.grid(column=2, row=6)
        btn5_3.grid(column=3, row=6)

        btn_opr_ver.grid(column=4, row=1, columnspan=3, rowspan=3)
        btn_con.grid(column=4, row=4, columnspan=3, rowspan=3)

        window.mainloop()

Entering_values.window_output()



# A = ([1, 1, 0],
#      [1, 1, 0],
#      [1, 0, 0])
#
# B = ([1, 1, 0],
#      [1, 1, 0],
#      [1, 0, 0])

#ves_mat = Point.select_a_column(A) # Определяем веса

#fin_mat = Point.matrix_multiplication_3x3(B, ves_mat) # умножение матрицы значений на матрицу весов

#result = Point.apply_activation_function(fin_mat) # сумирование и применение функции активации

#print(result)