'''
https://leetcode.com/problems/string-compression/description/
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        l = 0
        r = 0

        while r < len(chars):
            ele = chars[r]
            count = 0

            while r < len(chars) and chars[r] == ele:
                r += 1
                count += 1

            chars[l] = ele
            l += 1

            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l += 1

        return l



'''

Here's a trace using chars = ['a','a','b','b','c','c','c']:

Setup
chars = ['a','a','b','b','c','c','c']
write = 0, read = 0

Iteration 1: read=0
char  = 'a'
count = 0

  inner while:
    chars[0]='a' == 'a' → read=1, count=1
    chars[1]='a' == 'a' → read=2, count=2
    chars[2]='b' != 'a' → stop

write 'a' → chars[0]='a', write=1
count=2 > 1 → write '2' → chars[1]='2', write=2
Array state:
['a','2','b','b','c','c','c']
       ↑write=2      ↑read=2... wait read=2

Iteration 2: read=2
char  = 'b'
count = 0

  inner while:
    chars[2]='b' == 'b' → read=3, count=1
    chars[3]='b' == 'b' → read=4, count=2
    chars[4]='c' != 'b' → stop

write 'b' → chars[2]='b', write=3
count=2 > 1 → write '2' → chars[3]='2', write=4
Array state:
['a','2','b','2','c','c','c']
                 ↑write=4  ↑read=4

Iteration 3: read=4
char  = 'c'
count = 0

  inner while:
    chars[4]='c' == 'c' → read=5, count=1
    chars[5]='c' == 'c' → read=6, count=2
    chars[6]='c' == 'c' → read=7, count=3
    read=7 → out of bounds → stop

write 'c' → chars[4]='c', write=5
count=3 > 1 → write '3' → chars[5]='3', write=6
Array state:
['a','2','b','2','c','3','c']
                       ↑write=6  ↑read=7

Loop ends: read=7 → out of bounds → stop

Return → 6

Summary Table
Iterread startcharcountwrittenwrite end10a2a,2222b2b,2434c3c,36
Final chars = ['a','2','b','2','c','3','c']
                                        ↑ leftover, ignored
New length  = 6


'''
