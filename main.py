# Dylan Stitt
# Unit 6 Lab 5
# Binary Search Tree

# Implementation & testing of the Binary Search Tree

# Import file
from TEST_CODE import *
import os
from BinarySearchTree import BinarySearchTree

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    # TEST 1 - Test BinaryNode nested class
    # BEFORE TESTING: implement BinaryNode actions & attributes
    TEST_binary_node(BinarySearchTree)

    BST = BinarySearchTree()

    # TEST 2 - Test insert
    # BEFORE TESTING: implement insert, inorder_traversal,
    #                           __str__, __len__
    TEST_insert(BST)

    # Tree Review!
    # This is not a test and has nothing to do with your code
    VIEW_tree()

    # TEST 3 - Test min & max
    # BEFORE TESTING: implement get_min, get_max
    TEST_min_max(BST)

    # TEST 4 - Test docstrings
    # BEFORE TESTING: implement docstrings
    TEST_docs(BST, BinarySearchTree)

if __name__ == "__main__":
    os.system("cls")
    main()
