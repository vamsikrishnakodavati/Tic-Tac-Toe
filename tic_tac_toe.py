import random
from math import inf


class TicTacToe_Game_Game:
    def __init__(self, user_turn, computer_turn, user_first_player):
        
        self.board = self.null_board()
        self.user_turn = user_turn
        self.computer_turn = computer_turn
        self.user_first_player = user_first_player
        self.user_val = -1 
        self.computer_val = 1 

    @staticmethod
    def null_board():
        
        return [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def display_board(self):
        
        points = {
            -1: self.user_turn,
            +1: self.computer_turn,
            0: ' '
        }
        for row in self.board:
            print('\n' + '----------------')
            for item in row:
                print(f'| {points[item]} |', end='')
        print('\n' + '----------------')

    def calculate_state(self):
        
        empty_cells = []
        for x, row in enumerate(self.board):
            for y, item in enumerate(row):
                if item == 0:
                    empty_cells.append([x, y])

        return empty_cells

    @staticmethod
    def cell_no(move_no):
        
        row = (move_no - 1) // 3
        col = (move_no - 1) % 3
        return [row, col]

    def perform_move(self, cell, player_value):
        
        if cell in self.calculate_state():
            self.board[cell[0]][cell[1]] = player_value
            return True
        else:
            return False

    def user_turn(self):
          
        print(f'User turn [{self.user_turn}]')
        self.display_board()
        move = -1
        while move < 1 or move > 9:
            move = int(input('Please enter a move between 1 - 9: '))
            cell = self.cell_no(move)
            valid_move = self.perform_move(cell, self.user_val)
            if not valid_move:
                print('Please enter a valid move !!!!')
                move = -1

    def win_moves(self, player):
        
        states = []

        diag_1 = []
        diag_2 = []

        for i in range(3):
            row_temp_state = []
            col_temp_state = []

            diag_1.append(self.board[i][i])
            diag_2.append(self.board[2 - i][i])

            for j in range(3):
                row_temp_state.append(self.board[i][j])
                col_temp_state.append(self.board[j][i])

            states.append(row_temp_state)
            states.append(col_temp_state)

        states.append(diag_1)
        states.append(diag_2)

        if [player, player, player] in states:
            return True
        else:
            return False

    def get_score(self):
        
        if self.win_moves(self.user_val):
            score = -1
        elif self.win_moves(self.computer_val):
            score = 1
        else:
            score = 0

        return score

    def finding_end(self):
        
        return self.win_moves(self.computer_val) or self.win_moves(self.user_val)

    def min_max(self, player):
        
        if player == self.computer_val:
            best_score = [-1, -1, -inf]
        else:
            best_score = [-1, -1, inf]
        remaining_empty_cells = self.calculate_state()

        if len(remaining_empty_cells) == 0 or self.finding_end():
            final_score = self.get_score()
            return [-1, -1, final_score]

        for item in remaining_empty_cells:
            x, y = item[0], item[1]
            self.board[x][y] = player
            final_score = self.min_max(-player)
            self.board[x][y] = 0
            final_score[0], final_score[1] = x, y

            if player == self.computer_val:
                if final_score[2] > best_score[2]:
                    best_score = final_score
            else:
                if final_score[2] < best_score[2]:
                    best_score = final_score

        return best_score

    def ai_turn(self):
       
        print(f'AI turn [{self.computer_turn}]')
        self.display_board()

        
        if len(self.calculate_state()) == 9:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        else:
            ai_move = self.min_max(self.computer_val)
            x, y = ai_move[0], ai_move[1]

        self.perform_move([x, y], self.computer_val)

    def main(self):
       

       
        while len(self.calculate_state()) > 0 and not self.finding_end():
            if self.user_first_player.casefold() == 'N'.casefold():
                self.ai_turn()
                self.user_first_player = ''
            self.user_turn()
            self.ai_turn()

        if self.win_moves(self.user_val):
            print('\n')
            self.display_board()
            print('You just defeated AI !!!')
        elif self.win_moves(self.computer_val):
            print('\n')
            self.display_board()
            print('You SIR, lost to a computer !!!')
        else:
            print('\n')
            self.display_board()
            print('You are TOUGH.. Call it a DRAW !!!')


if __name__ == "__main__":

    u_first_player = ''
    u_choice = ''
    a_i_choice = ''

    while u_choice.casefold() != 'X'.casefold() and u_choice.casefold() != 'O'.casefold():
        u_choice = input('Would you like to play X or O: ').upper()
        a_i_choice = 'O' if u_choice.casefold() == 'X'.casefold() else 'X'

    while u_first_player.casefold() != 'Y'.casefold() and u_first_player.casefold() != 'N'.casefold():
        u_first_player = input('Would you like to play first? Y / N: ')

    t = TicTacToe_Game_Game(u_choice, a_i_choice, u_first_player)
    t.main()