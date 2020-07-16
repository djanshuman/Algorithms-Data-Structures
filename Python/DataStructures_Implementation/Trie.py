'''
Created on 17-Jul-2020

@author: dibyajyoti

Trie Insert | find Implementation in Python 
'''

class TrieNode:
    def __init__(self,text=''):
        self.text=text
        self.children=dict()
        self.is_word=False

    def __str__(self):
        return "{} -> {}".format(self.text,self.children)

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        current=self.root
        for i , char in enumerate(word):
            if char not in current.children:
                prefix=word[0:i+1]
                current.children[char]=TrieNode(prefix)
                #print(current.children)
            current=current.children[char]
        current.is_word=True

    def search(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                return None
            current=current.children[char]
        if current.is_word: return current

    def display(self):
        print("=====================")
        print(self.display_helper(self.root))
        print("=====================")

    def display_helper(self,root):
        print(root)
        for letter in root.children:
            self.display_helper(root.children[letter])

node=PrefixTree()
node.insert('apple')
node.insert('app')
node.insert('aposematic')
node.insert('appreciate')
node.insert('book')
node.insert('bad')
node.insert('bear')
node.insert('bat')
node.display()
print(node.search('book'))
