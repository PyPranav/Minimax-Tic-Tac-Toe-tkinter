import tkinter as tk
from tkinter import messagebox
from math import inf as infinity
from tkinter import ttk

w = 16
h = 7
f = 5000


class TicTacToe:
    def __init__(self):
        self.player_dic = {"O": 'Player', 'X': 'AI'}

        self.count = 0
        self.li = [' ' for _ in range(9)]
        self.possible_moves = [z for z in range(9)]
        self.exit_flag = False
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')

        self.btn0 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(0))
        self.btn0.grid(row=0, column=0)

        self.btn1 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(1))
        self.btn1.grid(row=0, column=1)

        self.btn2 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(2))
        self.btn2.grid(row=0, column=2)

        self.btn3 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(3))
        self.btn3.grid(row=1, column=0)

        self.btn4 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(4))
        self.btn4.grid(row=1, column=1)

        self.btn5 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(5))
        self.btn5.grid(row=1, column=2)

        self.btn6 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(6))
        self.btn6.grid(row=2, column=0)

        self.btn7 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(7))
        self.btn7.grid(row=2, column=1)

        self.btn8 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(8))
        self.btn8.grid(row=2, column=2)

        self.root.mainloop()

    def change(self, num):
        if self.count % 2:
            y = 'X'
        else:
            y = 'O'
        exec('self.btn' + str(num) + '.config(text=y, state="disable")')
        self.li[num] = y
        self.possible_moves.remove(num)
        self.root.update()
        self.count += 1
        self.check()
        try:
            b = self.minimax(self.li, self.li.count(' '), 'X')
            y = 'X'
            exec('self.btn' + str(b[0]) + '.config(text=y, state="disable")')
            self.li[b[0]] = 'X'
            self.root.update()
            self.count += 1
            self.check()
        except Exception:
            pass

    def check(self):
        li = self.li
        if li[0] == li[1] == li[2] != ' ':
            self.check_part(0, 1, 2)
        elif li[0] == li[3] == li[6] != ' ':
            self.check_part(0, 3, 6)
        elif li[3] == li[4] == li[5] != ' ':
            self.check_part(3, 4, 5)
        elif li[1] == li[4] == li[7] != ' ':
            self.check_part(1, 4, 7)
        elif li[6] == li[7] == li[8] != ' ':
            self.check_part(6, 7, 8)
        elif li[2] == li[5] == li[8] != ' ':
            self.check_part(2, 5, 8)
        elif li[0] == li[4] == li[8] != ' ':
            self.check_part(0, 4, 8)
        elif li[2] == li[4] == li[6] != ' ':
            self.check_part(2, 4, 6)
        if ' ' not in li and not self.exit_flag:
            self.winner_popup('!TIEtie')
            self.root.destroy()

    def check_part(self, *num):
        li = self.li
        for z in num:
            exec('self.btn' + str(z) + '.config(bg="#90EE90")')
        self.winner_popup(self.player_dic[li[num[0]]])
        self.root.destroy()
        self.exit_flag = True

    def winner_popup(self, winner):
        if winner != '!TIEtie':
            messagebox._show('Game Over', winner.title() + ' wins the game!!')
        else:
            messagebox._show('Game Over', "It was a tie!!")

    def minimax(self, state, depth, player):
        if player == 'X':
            best = [-1, -infinity]
        else:
            best = [-1, +infinity]

        if depth == 0 or self.ai_check(state) != 0:
            score = self.ai_check(state)
            return [-1, score]

        for cell in [z for z in range(len(state)) if state[z] == ' ']:
            state[cell] = player
            score = self.minimax(state, depth - 1, 'O' if player == 'X' else 'X')
            state[cell] = ' '
            score[0] = cell

            if player == 'X':
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score

        return best

    def ai_check(self, li):
        wn = ' '
        if li[0] == li[1] == li[2] != ' ':
            wn = li[0]
        elif li[0] == li[3] == li[6] != ' ':
            wn = li[0]
        elif li[3] == li[4] == li[5] != ' ':
            wn = li[3]
        elif li[1] == li[4] == li[7] != ' ':
            wn = li[1]
        elif li[6] == li[7] == li[8] != ' ':
            wn = li[6]
        elif li[2] == li[5] == li[8] != ' ':
            wn = li[2]
        elif li[0] == li[4] == li[8] != ' ':
            wn = li[0]
        elif li[2] == li[4] == li[6] != ' ':
            wn = li[2]
        if wn == 'X':
            return 1
        elif wn == 'O':
            return -1
        else:
            return 0


TicTacToe()
is_play = False


def ye():
    global is_play
    is_play = True
    root.destroy()


while True:
    root = tk.Tk()
    root.title('Restart??')
    label = ttk.Label(root, text='Do you want to play again ?')
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
    btn_yes = ttk.Button(root, text='Yes', command=ye)
    btn_yes.grid(row=1, column=0, padx=10, pady=5)
    btn_no = ttk.Button(root, text='No', command=lambda: root.destroy())
    btn_no.grid(row=1, column=1, padx=10, pady=5)
    root.mainloop()
    if is_play:
        TicTacToe()
        is_play = False
    else:
        break
