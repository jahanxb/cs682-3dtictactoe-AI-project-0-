#!/usr/bin/env python3
from tictac import TicTacToe
import unittest
import numpy as np


class TestTicTacToe(unittest.TestCase):
    def test_init_board(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.board.shape, (3,3))

    def test_basic_play_game_1(self):
        testcase = np.zeros((3,3))
        testcase[0,0] = 1
        testcase[1,0] = -1
        testcase[2,2] = 1
        player_first = 1
        expected = testcase.copy()
        expected[1,1] = 1
        expected_winner = 1
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        print("\nfinal board = \n{}".format(b))
        print("expected board = \n{}".format(expected))
        self.assertEqual(p, expected_winner)
        self.assertEqual(b.tolist(), expected.tolist())

    def test_basic_play_game_2(self):
        testcase = np.array([[ 1,0,1],
                             [-1,0,0],
                             [ 0,0,0]])
        player_first = 1
        
        expected = np.array([[ 1,1,1],
                             [-1,0,0],
                             [ 0,0,0]])
        expected_winner = 1
       
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        
        self.assertEqual(p, expected_winner)
        self.assertEqual(b.tolist(), expected.tolist())

    def test_basic_play_game_3(self):
        testcase = np.array([[ 0,0,1],
                             [-1,0,0],
                             [ 1,0,0]])
        player_first = 1
        
        expected = np.array([[ 0,0,1],
                             [-1,1,0],
                             [ 1,0,0]])
        expected_winner = 1
       
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        
        self.assertEqual(p, expected_winner)
        self.assertEqual(b.tolist(), expected.tolist())

    def test_basic_play_game_4(self):
        testcase = -1*np.array([[ 1,0,1],
                             [-1,0,0],
                             [ 0,0,0]])
        player_first = -1
        
        expected = -1*np.array([[ 1,1,1],
                             [-1,0,0],
                             [ 0,0,0]])
        expected_winner = -1
       
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        
        self.assertEqual(p, expected_winner)
        self.assertEqual(b.tolist(), expected.tolist())

    def test_basic_play_game_5(self):
        testcase = -1*np.array([[ 0,0,1],
                             [-1,0,0],
                             [ 1,0,0]])
        player_first = -1
        
        expected = -1*np.array([[ 0,0,1],
                             [-1,1,0],
                             [ 1,0,0]])
        expected_winner = -1
       
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        
        self.assertEqual(p, expected_winner)
        self.assertEqual(b.tolist(), expected.tolist())

    def test_basic_play_game_6(self):
        testcase = -1*np.array([[ 0,0,1],
                             [-1,0,0],
                             [ 1,0,0]])
        player_first = -1
        
        expected = -1*np.array([[ 0,0,1],
                             [-1,1,0],
                             [ 1,0,0]])
        expected_winner = -1
       
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        
        self.assertEqual(p, expected_winner)
        self.assertEqual(b.tolist(), expected.tolist())

    def test_play_game_1(self):
        testcase = np.array([[ 0,0,0],
                             [-1,1,0],
                             [-1,0,0]])
        player_first = 1
        
        expected_1 = np.array([[ 1, -1,  1],
                               [-1,  1, -1],
                               [-1,  1, -1]
                               ])
        expected_2 = np.array([[ 1, -1, -1],
                               [-1,  1,  1],
                               [-1,  1, -1]])
        expected_winner = 0 
       
        ttt = TicTacToe(testcase, player_first)
        b,p = ttt.play_game()
        print("\nfinal board = \n{}".format(b))
        correct = np.array_equal(b, expected_1) or \
                  np.array_equal(b, expected_2) 
        self.assertEqual(p, expected_winner)
        self.assertTrue(correct)


unittest.main()