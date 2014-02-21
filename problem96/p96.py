import numpy as np
import sys
import sets as set
import pdb


BOARD_SIZE = 9
VALID = set.Set(np.arange(1,10))

class SodukuBoard(object):


    def __init__(self):
        self.solution_boards = []
        self.game_number = 0
        self.board_np = np.zeros([BOARD_SIZE, BOARD_SIZE])
        #self.board = [[0] * BOARD_SIZE ] * BOARD_SIZE #This has an error according to A.
        self.ref_board = []
        self.ref_board = self.read_boards_from_txt()
        self.ref_board_np = np.array(self.ref_board)
        self.board_np = np.copy(self.ref_board_np[self.game_number,:,:])


    def __str__(self):
        return self.board_np


    def __repl__(self):
        return self.board_np


    def check_rows(self):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(self.board_np[i,:])) < BOARD_SIZE:
                return False
        return True


    def update_board(self, i, j, value):
        self.board_np[i,j] = value
        return True


    def save_solution_board(self):
        self.solution_boards.append(self.game_number)
        self.solution_boards[self.game_number] = []
        self.solution_boards[self.game_number].append(np.copy(self.board_np))
        return True


    def move_to_next_game(self):
        self.game_number += 1
        if self.game_number < len(self.ref_board_np):
            self.board_np = np.copy(self.ref_board_np[self.game_number,:,:])
            print('+++++++++++STARTING NEXT GAME+++++++++++++++++')
        else:
            print('+++++++++++All GAMES COMPLETE+++++++++++++++++')



    def read_boards_from_txt(self):

        #The idiomatic way to handle file reading
        with open('sudoku.txt', 'r') as file_handle:
            ref_board = []
            for line in file_handle:
                if line[0]=='G':
                    #New board
                    board_number = int(line.split(' ')[1]) - 1
                    ref_board.append(board_number)
                    ref_board[board_number] = []
                    print board_number
                else:
                    #print(line)
                    new_board_row = [int(c) for c in line if c in '1234567890']
                    ref_board[board_number].append(new_board_row)

        print("Data file Soduku.txt was read into data arrays")
        return ref_board


    def check_columns(self):
        for i in xrange(BOARD_SIZE):
            if len(np.unique(self.board_np[:,i])) < BOARD_SIZE:
                return False
        return True


    def check_sub_boards(self):

        for r in range(3): #rows
            for c in range(3): #columns
                col = c*3
                row = r*3
                sub_board = self.board_np[row:row+3, col:col+3]
                #print(sub_board)
                if len(np.unique(sub_board)) < BOARD_SIZE:
                    return False
        return True


    def validate_solution(self):
        if self.check_rows():
            if self.check_columns():
                if self.check_sub_boards():
                    print("This board has been solved!")
                    return True
        return False


    def get_sub_board(self, i, j):
        #this function returns the sub_board needed of the given i,j
        row = np.floor(i/3) * 3
        col = np.floor(j/3) * 3
        sub_board = self.board_np[row:row+3, col:col+3]
        return sub_board


    def determine_valid_moves(self, i, j):

        b_np = self.board_np
        if b_np[i,j]!=0:
            return([],VALID)

        current_val = b_np[i,j]
        col = set.Set(self.board_np[:,j])
        #print(col)
        row = set.Set(self.board_np[i,:])
        #print(row)
        sub_board = self.get_sub_board(i, j)
        sub_board = set.Set(sub_board.flatten())
        #print(sub_board)

        forbidden = col.union(row)
        forbidden = forbidden.union(sub_board)
        #print(forbidden)
        allowed = VALID - forbidden
        return(allowed, forbidden)

    def compute_best_move(self):
        best_r = -1
        best_c = -1
        best_allowed = [-1] * 9
        for r in xrange(BOARD_SIZE):
            for c in xrange(BOARD_SIZE):
                print (r, c)
                (allowed, forbidden) = self.determine_valid_moves(r,c)
                if (allowed!=[]):
                    print(allowed, forbidden)
                    if (len(allowed) < len(best_allowed)):
                        best_allowed = allowed
                        best_r = r
                        best_c = c
                        if len(allowed)==1:
                            return (r, c, allowed)

        return (r, c, allowed)


def main():
    mb = SodukuBoard()

    #Main execution loop!

    while True:
        (r,c,allowed) = mb.compute_best_move()
        #print (r, c, allowed)
        if len(allowed)==1:
            mb.update_board(r, c, list(allowed)[0])
        elif allowed==[]:
            if mb.validate_solution():
                mb.save_solution_board()
                mb.move_to_next_game()
                print(mb.board_np)


            else:
                print mb.game_number
                mb.move_to_next_game()
                #pdb.set_trace()
                print "super crapper, no allowed moves but the board isn't solved"
                #break
        else:
            print "crapper"
            break


    print(mb.board_np)



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


