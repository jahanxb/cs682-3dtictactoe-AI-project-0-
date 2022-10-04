#!/usr/bin/python3

import numpy as np
import argparse

class TicTacToe:
	def __init__(self, board=None, player=1) -> None:
		if board is None:
			self.board = self.init_board()
		else:
			self.board = board
		self.player = player

	def init_board(self):
		return np.array([[0,0,0],[0,0,0],[0,0,0]])

	def print_board(self):
		print (self.board)

	def eval_win(self):
		# TODO: Implement how to evaluate a win
		return 1

	def play_game(self):
		# some while loop 
		return self.board, self.eval_win()

def load_board( filename ):
	return np.loadtxt( filename)

# def save_board( self, filename ):
# 	np.savetxt( filename, self.board, fmt='%d')

def main():
	parser = argparse.ArgumentParser(description='Play tic tac toe')
	parser.add_argument('-f', '--file', default=None, type=str ,help='load board from file')
	parser.add_argument('-p', '--player', default=1, type=int, choices=[1,-1] ,help='player that playes first, 1 or -1')
	args = parser.parse_args()

	board = load_board(args.file) if args.file else None
	testcase = np.array([[ 0,0,0],
                             [-1,1,0],
                             [-1,0,0]])
	ttt = TicTacToe(testcase, args.player)
	# ttt.print_board()
	b,p = ttt.play_game()
	print("final board: \n{}".format(b))
	print("winner: player {}".format(p))

if __name__ == '__main__':
	main()