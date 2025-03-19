##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def TEST_binary_node(class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: BinaryNode class{W}\n")

    test_node1 = class_ref.BinaryNode(1)
    test_node2 = class_ref.BinaryNode(2)

    test = type(test_node1) == class_ref.BinaryNode
    print(f"New BinaryNode object was created: {result(test)}")

    test = test_node1._BinaryNode__parent == test_node1._BinaryNode__left == test_node1._BinaryNode__right == None
    print(f"BinaryNode parent, left, & right pointers initialize to None: {result(test)}")

    print(f"\n{P}Inequality Magic Methods{W}")

    print(f"\n{test_node1} < {test_node2}")
    test = test_node1 < test_node2 and not (test_node2 < test_node1)
    print(f"Less than produces correct result: {result(test)}")

    try:
        test_node1 < 2
        print(f"Less than raises an exception when comparing node and non-node: {result(False)}")
    except:
        print(f"Less than raises an exception when comparing node and non-node: {result(True)}")

    print(f"\n{test_node1} > {test_node2}")
    test = not (test_node1 > test_node2) and test_node2 > test_node1
    print(f"Greater than produces correct result: {result(test)}")

    try:
        test_node1 > 2
        print(f"Greater than raises an exception when comparing node and non-node: {result(False)}")
    except:
        print(f"Greater than raises an exception when comparing node and non-node: {result(True)}")

    print(f"\n{test_node1} == {test_node2}")
    test = not (test_node1 == test_node2)
    print(f"Equal to produces correct result: {result(test)}")

    try:
        test_node1 == 2
        print(f"Equal to raises an exception when comparing node and non-node: {result(False)}")
    except:
        print(f"Equal to raises an exception when comparing node and non-node: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_insert(BST):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Inserting Values{W}\n")

    print(f"{P} ~ Root Insertion ~{W}")

    print(f"{B}First node, 19, will be added{W}")

    BST.insert(19)
    print(f"Current BST: {B}{BST}{W}\n")

    test = type(BST._BinarySearchTree__root) == BST.BinaryNode
    print(f"Element added to tree as BinaryNode: {result(test)}")

    test = BST._BinarySearchTree__root._BinaryNode__value == 19
    print(f"First value is added as root: {result(test)}")

    test = len(BST) == 1
    print(f"Tree size increased to 1: {result(test)}\n")

    try:
        BST.insert('X')
        BST.insert(True)
        BST.insert(3.14)
        print(f"Can only insert integers into BST: {result(False)}")
    except:
        print(f"Can only insert integers into BST: {result(True)}")

    try:
        BST.insert(19)
        print(f"Cannot insert duplicate values into BST: {result(False)}")
    except:
        print(f"Cannot insert duplicate values into BST: {result(True)}")

    ############
    root = BST._BinarySearchTree__root
    ############

    print(f"\n\n{P} ~ Simple Left Insertion (no recursion) ~{W}")
    print(f"{B}Second node, 7, will be added{W}")
    BST.insert(7)
    print(f"Current BST: {B}{BST}{W}\n")

    test = root._BinaryNode__left._BinaryNode__value == 7
    print(f"New node was inserted at the correct location: {result(test)}")

    test = root._BinaryNode__left._BinaryNode__parent is root
    print(f"New node is connected to its parent: {result(test)}")

    test = len(BST) == 2
    print(f"Tree size increased to 2: {result(test)}")

    test = BST.inorder_traversal() == [7, 19]
    print(f"\nInorder traversal produces sorted list: {result(test)}")

    ############

    print(f"\n\n{P} ~ Simple Right Insertion (no recursion) ~{W}")
    print(f"{B}Third node, 25, will be added{W}")
    BST.insert(25)
    print(f"Current BST: {B}{BST}{W}\n")

    test = root._BinaryNode__right._BinaryNode__value == 25
    print(f"New node was inserted at the correct location: {result(test)}")

    test = root._BinaryNode__right._BinaryNode__parent is root
    print(f"New node is connected to its parent: {result(test)}")

    test = len(BST) == 3
    print(f"Tree size increased to 3: {result(test)}")

    test = BST.inorder_traversal() == [7, 19, 25]
    print(f"\nInorder traversal produces sorted list: {result(test)}")

    ############

    print(f"\n\n{P} ~ Recursive Insertion ~{W}")
    print(f"{B}Fourth node, 10, will be added{W}")
    BST.insert(10)
    print(f"Current BST: {B}{BST}{W}\n")

    test = root._BinaryNode__left._BinaryNode__right._BinaryNode__value == 10
    print(f"New node was inserted at the correct location: {result(test)}")

    test = root._BinaryNode__left._BinaryNode__right._BinaryNode__parent is root._BinaryNode__left
    print(f"New node is connected to its parent: {result(test)}")

    test = len(BST) == 4
    print(f"Tree size increased to 4: {result(test)}")

    test = BST.inorder_traversal() == [7, 10, 19, 25]
    print(f"\nInorder traversal produces sorted list: {result(test)}")

    print(f"\n\n{B}Fifth node, 20, will be added{W}")
    BST.insert(20)
    print(f"Current BST: {B}{BST}{W}\n")

    test = root._BinaryNode__right._BinaryNode__left._BinaryNode__value == 20
    print(f"New node was inserted at the correct location: {result(test)}")

    test = root._BinaryNode__right._BinaryNode__left._BinaryNode__parent is root._BinaryNode__right
    print(f"New node is connected to its parent: {result(test)}")

    test = len(BST) == 5
    print(f"Tree size increased to 5: {result(test)}")

    test = BST.inorder_traversal() == [7, 10, 19, 20, 25]
    print(f"\nInorder traversal produces sorted list: {result(test)}")

    ############

    print(f"\n\n{P} ~ Bulk Insertion ~{W}")
    for element in [2, 3, 24, 15]:
        BST.insert(element)

    print(f"Four new elements were inserted: {B}{BST}{W}\n")

    test = len(BST) == 9
    print(f"Tree size increased to 9: {result(test)}")

    test = BST.inorder_traversal() == [2, 3, 7, 10, 15, 19, 20, 24, 25]
    print(f"\nInorder traversal produces sorted list: {result(test)}")

    ############

    print(f"\n\n{P} ~ Duplication Exception ~{W}")

    test = True
    for element in [2, 3, 7, 10, 15, 19, 20, 24, 25]:
        try:
            BST.insert(element)
            test = test and False
        except:
            test = test and True

    print(f"BST prevents any duplicates from being added: {result(test)}")

    print("~" * 50, "\n\n")


def VIEW_tree():
    print("~" * 50)
    print(f"{P}This is what your tree will look\nlike for the next round of tests. {W}\n")

    print("""
              (19)
            /     \\
          (7)      (25)
          / \\     /
        (2) (10) (20)
          \\    \\     \\
          (3)  (15)  (24)

    """)
    print("~" * 50, "\n\n")


def TEST_min_max(BST):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: get_min & get_max{W}\n")

    print(f"{P} ~ get_min() ~{W}")
    print(f"Current BST: {B}{BST}{W}")

    exp = 2
    res = BST.get_min()._BinaryNode__value
    test = exp == res
    print(f"The min in this tree is {exp}: {result(test)}")

    BST.insert(1)
    print(f"\nA new min was added to the tree: {B}{BST}{W}")

    exp = 1
    res = BST.get_min()._BinaryNode__value
    test = exp == res
    print(f"The min in this tree is {exp}: {result(test)}")

    print(f"\n\n{P} ~ get_max() ~{W}")
    print(f"Current BST: {B}{BST}{W}")

    exp = 25
    res = BST.get_max()._BinaryNode__value
    test = exp == res
    print(f"The max in this tree is {exp}: {result(test)}")

    BST.insert(30)
    print(f"\nA new max was added to the tree: {B}{BST}{W}")

    exp = 30
    res = BST.get_max()._BinaryNode__value
    test = exp == res
    print(f"The max in this tree is {exp}: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(BST, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = BST.insert.__doc__
    if doc != None:
        print(f"{B}insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}insert() Documentation Missing{W}\n")

    doc = BST.get_min.__doc__
    if doc != None:
        print(f"{B}get_min() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_min() Documentation Missing{W}\n")

    doc = BST.get_max.__doc__
    if doc != None:
        print(f"{B}get_max() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_max() Documentation Missing{W}\n")

    doc = BST.inorder_traversal.__doc__
    if doc != None:
        print(f"{B}inorder_traversal() Documentation:{W} {doc}\n")
    else:
        print(f"{R}inorder_traversal() Documentation Missing{W}\n")

    doc = class_ref.__str__.__doc__
    if doc != None:
        print(f"{B}__str__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__str__() Documentation Missing{W}\n")

    doc = class_ref.__len__.__doc__
    if doc != None:
        print(f"{B}__len__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__len__() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")