
class BNode:
    def __init__(self, entryValue) -> None:
        self._right = None
        self._left = None
        self._parent = None
        self._entry = entryValue
    def get_branch(self, branchName: str):
       if branchName == "right":
           if self._entry.get_branch("right") is None:
               return float("-inf")
           return self._right
       if self._entry.get_branch("left") is None:
            return float("inf")
       return self._left
    def set_branch(self, branchName: str, entryValue: int):
        if branchName == "right":
            self._right = BNode(entryValue)
        return self._left
    def has_branch(self, branchName: str):
        if branchName == "right" and self._right != None:
            return True
        elif branchName == "left" and self._left != None:
            return True
        else:
            return False
    def get_branch_count(self):
        return int(self.has_branch("right")) + int(self.has_branch("left"))

class MHeap:
    def __init__(self) -> None:
        self._adam = None
    def add(self, entry, startNode=self._adam):
        if self._adam is None:
            self._adam = BNode(entry)
        #okay now we have to see if we go right

        if startNode == entry:
            raise Exception("Can't add duplicate entries")
        if entry <= startNode.get_branch("right") and startNode.has_branch("right"):
            self.add(entry, startNode=startNode.get_branch("right"))
        if entry > startNode.get_branch("left") and startNode.has_branch("left"):
            self.add(entry, startNode.get_branch("left"))
