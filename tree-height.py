# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self):
        self.childern=[]
        self.h=0
    
    
    def join(self,child):
        self.childern.append(child)

        
    def height(self,ht):
        self.h=ht
        


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        
    def create_tree(self):
        node=[Node() for i in range(len(self.parent))]        
        for i in range(len(self.parent)):
            if self.parent[i]==-1:
                root=i
            else:
                node[self.parent[i]].join(i)
        return node,root

    def compute_height(self):
                # Replace this code with a faster implementation
        tree,root=self.create_tree()
        height=0
        if tree[root].childern==[]:
            return height
        else:
            queue=[]
            queue.append(tree[root])
            while len(queue)!=0:
                node=queue.pop(0)
                if node.h==height:
                    height+=1
                for i in node.childern:
                    tree[i].h=height
                    queue.append(tree[i])
                
            return height
                    

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
