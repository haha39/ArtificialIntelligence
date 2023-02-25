import math
from re import I


'''
intial  maze
'''
maze = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1]]

StartX = 0
StartY = 0
EndingX = 5
EndingY = 2


'''
initial node
'''


class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.gCost = 0.0
        self.hCost = 0.0
        self.isObs = 0
        self.parent = None

    def g(self, g):
        self.gCost = g

    def h(self):
        # float type
        self.hCost = math.pow(
            (math.pow((EndingX - self.x), 2) + math.pow((EndingY - self.y), 2)), 0.5)

        # print(self.hCost)

    def setPrent(self, p):
        self.parent = p

    '''def compare(self, node):
        if (self.gCost + self.hCost < node.gCost + node.hCost):
            return 1
        else:
            return -1'''


'''
A Star
'''


class AStar:
    def __init__(self, maze, startNode, endingNode):
        self.openList = []
        self.closeList = []
        self.pathList = []
        self.nodes = [[]]
        self.maze = maze
        self.startX = StartX
        self.startY = StartY
        self.endingX = EndingX
        self.endingY = EndingY
        self.currentNode = startNode
        self.startNode = startNode
        self.endingNode = endingNode

# create the node with it's position
    def createNodes(self, ):
        for i in range(6):
            for j in range(6):
                node = Node()
                node.x = i
                node.y = j
                if maze[i][j] == 1:
                    node.isObs = 1
                self.nodes[i].append(node)
                print("x = %d, y = %d, obs = %d\n" % (
                    self.nodes[i][j].x, self.nodes[i][j].y, self.nodes[i][j].isObs))

# if openList is empty
    def isEmpty(self, ):
        if not self.openList:
            #print("openList is empty, haha\n")
            return 0

# get min node from openList
    def getMin(self, ):
        temp = self.openList[0]

        for node in self.openList:
            if node.gCost + node.hCost < temp.gCost + temp.hCost:
                temp = node

        return temp

# push node into list
    def push(self, node):
        self.openList.append(node)

# remove node from list
    def removeNode(self, node):
        return self.openList.pop(node)  # del? del0?

# obtain node from list
    def getNode(self, node):
        for n in self.openList:
            if n.x == node.x and n.y == node.y:
                # print(n.gCost)
                return n
        return None

# if node is in openList
    def nodeInOpen(self, node):
        for n in self.openList:
            if n.x == node.x and n.y == node.y:
                return 1
        return 0

# if node is in closeList
    def nodeInClose(self, node):
        for n in self.closeList:
            if n.x == node.x and n.y == node.y:
                return 1
        return 0

# if ending is in openlist
    def endingInOpen(self, ):
        for n in self.openList:
            if n.x == self.endingX and n.y == self.endingY:
                return 1
        return 0

# search node haha
    def searchNode(self, node):
        # if out of range
        if node.x < 0 or node.x > 5 or node.y < 0 or node.y > 5:
            return
         # if obs
        if self.maze[node.x][node.y] == 1:
            return
        # already in close list
        if self.nodeInClose(node):
            return
        # G(n)
        if abs(self.currentNode.x - node.x) == 1 and abs(self.currentNode.y - node.y) == 1:
            g = 1.4
        else:
            g = 1.0
        # if not in open, then push
        if self.nodeInOpen(node) == 0:
            node.g(g + self.currentNode.gCost)
            node.h()
            node.parent = self.currentNode
            self.openList.append(node)

        # if in open, then compare
        else:
            n1 = self.getNode(node)
            # print("(%d,%d)  " % (node.x, node.y))
            # print("(%d,%d)  " % (n1.x, n1.y))
            # print("(%f,%f) \n" % (node.gCost, n1.gCost))

            if self.currentNode.gCost + g < n1.gCost:
                # print(123321999000)
                n1.gCost = self.currentNode.gCost + g
                n1.parent = self.currentNode  # dont forget this!!
                # self.openList.remove(node)
                # self.openList.append(n1)

# search your neighbors
    def searchEightNeighbors(self, ):
        # top left
        self.searchNode(Node(self.currentNode.x - 1, self.currentNode.y - 1))
        # top
        self.searchNode(Node(self.currentNode.x - 1, self.currentNode.y))
        # top right
        self.searchNode(Node(self.currentNode.x - 1, self.currentNode.y + 1))
        #     left
        self.searchNode(Node(self.currentNode.x, self.currentNode.y - 1))
        #     right
        self.searchNode(Node(self.currentNode.x, self.currentNode.y + 1))
        # bottom left
        self.searchNode(Node(self.currentNode.x + 1, self.currentNode.y - 1))
        # bottom
        self.searchNode(Node(self.currentNode.x + 1, self.currentNode.y))
        # bottom right
        self.searchNode(Node(self.currentNode.x + 1, self.currentNode.y + 1))

# start to find the path
    def findPath(self):
        # first node
        self.startNode.g(0)
        self.startNode.h()
        self.openList.append(self.startNode)

        # loop till find the ending
        while True:
            self.currentNode = self.getMin()
            self.closeList.append(self.currentNode)
            self.openList.remove(self.currentNode)

            self.searchEightNeighbors()

            # check if it is finish
            if self.endingInOpen():
                temp = self.getNode(self.endingNode)

                while True:
                    self.pathList.append(temp)
                    if temp.parent != None:
                        temp = temp.parent
                    else:
                        return True
            elif len(self.openList) == 0:
                return False
        return True

# show the answer
    def showPath(self, ):
        l = len(self.pathList)
        for i in range(l):
            print("(%d,%d)\n" %
                  (self.pathList[l - i - 1].x, self.pathList[l - i - 1].y))


'''
main
'''


def main():
    #print("Hello World\n")
    # show original maze
    print("show the define coordinates : ")
    for i in range(6):
        for j in range(6):
            print("(%d,%d)" % (i, j), end=" ")
        print("\n")

    # start a* algo
    aStar = AStar(maze, Node(StartX, StartY), Node(EndingX, EndingY))
    print("output : \n")
    if aStar.findPath():
        aStar.showPath()
    else:
        print("fail QQ")


if __name__ == '__main__':
    main()


'''
note:
    float
    .pdf
    somethin - anthology

'''
