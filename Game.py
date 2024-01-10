from Move import Move
from Board import Board
from Score import Score
import random

class Game:
    def __init__(self):
        self.__board = Board()
        self.__options = (0,1,2,3,4,5,6,7)
        self.__code = self.get_code()

        self.score_list = []
        self.move_list = []
        self.curr_move = -1


    def get_code(self):
        code = random.sample(self.__options ,4)
        return code


    def make_move(self, input):
        m = Move()
        m.make(input)
        self.move_list.append(m)
        self.curr_move += 1

    def update_score(self):
        s = Score()
        s.calculate(self.__code, self.move_list[self.curr_move])
        self.score_list.append(s)
        return

    def show_code(self):
        print('the real code is__',self.__code)

    def get_user_choice(self):
        user_input = input('enter your choise now: ')
        move = list(user_input)
        for i in range(len(move)):
            move[i] = int(move[i])
        return move

    def show_board(self):
        print('round _____ move ________ score')
        for i in range(self.curr_move +1):
            print(' ',i+1,'___',self.move_list[i],'__',self.score_list[i])

    def single_round(self):
        move = self.get_user_choice()
        self.make_move(move)
        self.update_score()
        self.show_board()


    def run(self):
        self.single_round()
        while self.score_list[self.curr_move] != [2,2,2,2]:
            self.single_round()

        print('correct!!!')
        self.show_code()



if __name__ == "__main__":
    g = Game()
    g.run()
