from _typeshed import TraceFunction


class BinaryNode:
    def __init__(self, entry):
        """A parental binary node with lots of features"""
        self._right = None
        self._left = None
        self._entry = entry
        self._dad = None
    def is_leaf(self):
        """Checks if the Binary Node is a leaf, or haw no parents"""
        if self._right== None and self._left == None: return True
        else: return False
    def get_entry(self):
        """Gets the entry"""
        return self._entry
    def branch_count(self):
        """Returns the amount of branches the node has (0-2("""
        #sets true as an int and counts from getting branch on both
        # left and right
        return int(self.has_branch("left")) + int(self.has_branch("right")) #cute cs girl forgive me
    def has_branch(self, branchDirection: str):
        """checks is the binary node either has right and left"""
        if branchDirection == "left" and self._left != None:
            return True
        if branchDirection == "right" and self._right != None:
            return True
        #neither is true and return false
        return False #else
    def get_branch(self, branchDirection: str):
        """gets the value in the binary node of the branch"""
        if branchDirection == "left": #if we;re left
            return self._left
        elif branchDirection == "right": #if we're right
            return self._right
        else:
            return None
    def set_branch(self, branchDirection: str, node):
        """Sets the value of the branch to the node"""
        if branchDirection == "left":
            self._left = node
        elif branchDirection == "right":
            self._right = node
        else:
            raise Exception(f"Branch direction \"{branchDirection}\" doesn't exist")

class BinaryTree:
    def __init__(self):
        """Makes a binary tree"""
        self._adam = None
        self.preOrder = "pre"
        self.inOrder = "in"
        self.postOrder = "post"
        self.deepest = 0
    def delete(self, value):
        """Deletes an element off of the binary tree by accessing her parent"""
        kiddieNode = self.__recursive_search(value) #get the initial value
        if kiddieNode is None:
            raise RuntimeError(f"No element with ID {value}")
        else:
            daddyNode = kiddieNode._dad
        #get the kiddieNode's branch so we can check it later
        sideOfKiddieNode = "left" if daddyNode.get_branch("left") is kiddieNode else "right"
        if kiddieNode.is_leaf():
            daddyNode.set_branch(sideOfKiddieNode, None)
        elif kiddieNode.branch_count() == 1:
            #we have at least one branch
            # but only one new kid that's getting
            # replaced with a newer baby node
            # let's check with
            child = kiddieNode.get_branch("left") or kiddieNode.get_branch("right")
            daddyNode.set_branch(sideOfKiddieNode, child)
        else: #so we have two branches and it's not as easy
           #okay imagine we have
           #       6
           #      / \
           #    10     20
           #    /\     /\
           #   11 16  21 30
           # we need to delete the node 6
           #  but we need the tree to still work
           # which means we need the smallest tree and then the next
           # larger is the next value
           # the probem is connecting the node 16 with the leftmost branch
           # up until its value matches
           successorNode: BinaryNode = kiddieNode.get_branch("left")
           #two cases: 1 is  the successor node no left branches, which means
           # it's the highest value and we just set the successor's left (next)
           # branch to the leftmost branch
           # 2 is that there's actually more than one branch and we
           # keep going deeper and deeeper into this thingamijig
           #
           highestValueInSucessorNodeTree = kiddieNode #so that we can set the right
           #branch if there's a depth of zeero
           while successorNode.has_branch("right"): #while we're not at the rightmost (highest) left value
               successorNode = successorNode.get_branch("right")
           highestValueInSucessorNodeTree = successorNode
           highestValueInSucessorNodeTree.set_branch("right", kiddieNode.get_branch("right")) #set the next right value to the kiddie node
           #this above here will preserve the hierarchy by setting the next value to the highest
           # on the branch tree and preserve order
           daddyNode.set_branch(sideOfKiddieNode, successorNode) #replace the kiddie node
           return None
    def search(self, nodeValue: int, startNode = None):
        """Searches through a binary tree and returns the element"""
        return self.__recursive_search(nodeValue, startNode).get_entry()
    def __recursive_search(self, nodeValue: int, startNode=None, found=False, returnBNode=False) -> BinaryNode:
        """Hidden function! Recursively checks through and returns the BinaryNode"""
        if startNode == None: #check if startNode is just nothing
            startNode = self._adam #set it to the start
        #this is just incase we wanna start the search somewhere else
        startNodeEntryValue = startNode.get_entry()
        if startNodeEntryValue == nodeValue: #did we find it?
            #we found it! return it
            return startNode
        elif startNodeEntryValue > nodeValue:
            #if we're at a smaller side, we're headed to the left
            if startNode.has_branch("left"):
                #so we're going to keep searching until we find that value
                return self.__recursive_search(nodeValue, startNode=startNode.get_branch("left"))
            else:
                raise IndexError(f"Value {nodeValue} doesn't exist")
        elif startNodeEntryValue < nodeValue:
            #same thing, we're at a larger side so we tend towards the right
            if startNode.has_branch("right"):
                return self.__recursive_search(nodeValue, startNode=startNode.get_branch("right"))
            else:
                raise IndexError(f"Value {nodeValue} doesn't exist")
            #todo check if we have a right branch
            #and if so go right
            #otherwise it doesn't exist
            #do the same for the left
    def add(self, entry) -> None:
        """Adds to binary tree, allows skewed"""
        userEntryNode = BinaryNode(entry)
        #is the start nothing? this will be our baseline
        # if it's not the baseline
        if self._adam == None:
            self._adam = userEntryNode
            return None
        else:
            #okay now we have to check the value of the node accessed
            #maybe you guys want me to do this recursively but i don't
            #like (n * n!) O time (especially in Python) so we're looping
            currentBNode = self._adam
            previousBNode = None
            deepestInFunction = 0
            #while the currentBNode is actually a BNode
            while hasattr(currentBNode, "_entry"):
                if deepestInFunction == self.deepest+1:
                    self.deepest += 1 #increase deepest amount
                #previous was the former current
                previousBNode = currentBNode
                #decide what direction we go into based on the size
                #we're using integers for the first lab so this works
                if currentBNode.get_entry() < userEntryNode.get_entry():
                    #right leaning >
                    currentBNode = currentBNode.get_branch("right")
                elif currentBNode.get_entry() > userEntryNode.get_entry():
                    currentBNode = currentBNode.get_branch("left") #lower value so left >
                elif currentBNode.get_entry() == userEntryNode.get_entry():
                    raise Exception("Duplicates not allowed as per the rule of Rex Noster Gibbons. Long live the king!!!")

                deepestInFunction += 1 #we've finished one layer so far
            #we've broken out of the loop!!!
            #now we know that the result of the currentNode is undefined
            #so we wanna go back and see what branch (left, right) we should
            #put the previous node                |------> None (currentNode maybe)
            # so we're here --->      previousNode|
            #                                     |-------> None (currentNode maybe)
            if previousBNode.get_entry() >= userEntryNode.get_entry(): #if it's right go right
                userEntryNode._dad = previousBNode
                previousBNode.set_branch("left", userEntryNode)
            else: #if it's left go left
                userEntryNode._dad = previousBNode
                previousBNode.set_branch("right", userEntryNode)
            return None

    def getAllNodesInTree(self, startNode, binaryNodeList: list, levelBNL: int) -> list:
        """Gets all the nodes in the tree for display"""
        if startNode == None:
            return [] #there's no left or right side return empty list
        binaryNodeList[levelBNL].append(startNode)
        #we recursively call the list to add more on each part
        if not startNode.is_leaf():
            if startNode.has_branch("left"):
                binaryNodeList = self.getAllNodesInTree(startNode.get_branch("left"), binaryNodeList, levelBNL+1)
            if startNode.has_branch("right"):
                binaryNodeList = self.getAllNodesInTree(startNode.get_branch("right"), binaryNodeList, levelBNL+1)
        return binaryNodeList
    def display(self, sortMethod):
        """Displays the node by returning a string in the method they want"""
        #make an empty list the depth length with lists in them
        leftDepth = [[] for _ in range(self.deepest+1)]
        rightDepth = [[] for _ in range(self.deepest+1)]
        leftList = self.getAllNodesInTree(self._adam.get_branch("left"), leftDepth, 0)
        rightList = self.getAllNodesInTree(self._adam.get_branch("right"), rightDepth, 0)
        listOfLeftNodes = [a for a in leftList]
        listOfRightNodes = [a for a in rightList]
        match sortMethod:
            case self.preOrder:
                print("Center: " + str(self._adam.get_entry().americanName))
                print("Left Nodes:", end="")
                for leftLevelArray in listOfLeftNodes:
                    for leftLANode in leftLevelArray:
                        print("(" + str(leftLANode.get_entry().americanName) + ")", end="")
                print("\nRight Nodes:", end="")
                for rightLevelArray in listOfRightNodes:
                    for rightLANode in rightLevelArray:
                        print("(" + str(rightLANode.get_entry().americanName) + ")", end="")
            case self.inOrder:
                print("Left Nodes:", end="")
                for leftLevelArray in listOfLeftNodes:
                    for leftLANode in leftLevelArray:
                        print("(" + str(leftLANode.get_entry().americanName) + ")", end="")
                print("Center: " + str(self._adam.get_entry().americanName))
                print("\nRight Nodes:", end="")
                for rightLevelArray in listOfRightNodes:
                    for rightLANode in rightLevelArray:
                        print("(" + str(rightLANode.get_entry().americanName) + ")", end="")

class Heap(BinaryTree):
    def __init__(self):
        super().__init__()
    def add(self, entry):
        """Adds an element to the binary tree"""
        #let's start by getting a new Binary Node
        newBinaryNode: BinaryNode = BinaryNode(entry=entry)
        if self._adam is None: #there's nothing here!
            self._adam = newBinaryNode #let's set the start to
            #our first entry
        traversalNode: BinaryNode = self._adam #now we wanna go to the right most branch
        #there's no particular order for left/right except that the parent
        # must be bigger than the child
        while traversalNode.has_branch("right"):
            traversalNode = traversalNode.get_branch("right")
        self.maxHeapAdd(newBinaryNode, traversalNode)
    def maxHeapAdd(self, newBinaryNode: BinaryNode, compareNode: BinaryNode):
        """Recursively adds a new binary node into the binary tree
        """
        if compareNode.get_entry() > newBinaryNode:
            #so we're at some point where the new BinaryNode
            #is less than the parent. so let's do two things
            #first let's make sure that the parent node doesn't
            # have kids that are greater than the new BinaryNode
            # entry and if not then we can add the binaryNode
            if compareNode.branch_count() < 2:
                #okay this means that there's at least some?
                # space for this element so we insert it and
                # return
                # we set the new dad here for easier future traversal
                newBinaryNode._dad = compareNode
                # we go right leaning here
                # and then we check to the left.
                if compareNode.has_branch("left"): compareNode.set_branch("right", newBinaryNode)
                elif compareNode.has_branch("right"): compareNode.set_branch("left", newBinaryNode)
                else: raise RuntimeError("Something absolutely terrible has happened.") #just in case :)
                return newBinaryNode
            elif compareNode.branch_count() == 2: #just making this airtight
                #this means the next two child branches exist so there's not
                # an easy "this is where you go" situation
                # therefore we need to do one of two things
                # (1): recurse and hopefully encounter a situation
                # where one of these child nodes are greater than
                # the newBinaryNode and then append the newBinaryNode
                # to that or
                # (2): we're in a situation where we're trying to add but
                # it looks like this
                # newBinaryNode : 26            (27)
                # compareNode : 27             /    \
                #                           (21)     (15)
                # where would compareNode go here?
                # the answer i will use is probably on the right branch and link 15 with 27
                # so it would become this
                #                               (27)
                #                              /    \
                #                           (21)    (26)
                #                                       \
                #                                        (15)
                # which makes sense to me because it still preserves the structure
                # but please feel free to comment
                compareNodeLeft: BinaryNode = compareNode.get_branch("left").get_entry()
                compareNodeRight: BinaryNode = compareNode.get_branch("right").get_entry()

                #SCENARIO 1: one of the child branches are greater than the compareNode
                if compareNodeRight > newBinaryNode:
                    #we start with right because we generally try to add
                    # right as much as we can, it's "right leaning"
                    return self.maxHeapAdd(newBinaryNode, compareNode.get_branch("right"))
                if compareNodeLeft > newBinaryNode:
                    #same deal with left if that's the way. this means right
                    # is bigger but left is not
                    return self.maxHeapAdd(newBinaryNode, compareNode.get_branch("left"))
                elif max(compareNodeLeft, compareNodeRight) < newBinaryNode.get_entry():
                    #okay so we have to now link the right node with this
                    # new nodes' value.
                    compareNodeRight._dad = newBinaryNode
                    newBinaryNode._dad = compareNode
                    return newBinaryNode
        elif compareNode.get_entry() < newBinaryNode.get_entry():
            # okay all that aside now
            # holy yap
            # this is when the newBinaryNode's entry is
            # greater than the current compare so it just means
            # we try and go one up (if we can)
            # hopefully!!! we caught the
            # self._adam.get_entry() < newBinaryNode.get_entry()
            # so we don't gotta worry about hittin' that roof
            # woof woof woof
            return self.maxHeapAdd(newBinaryNode, compareNode._dad)
