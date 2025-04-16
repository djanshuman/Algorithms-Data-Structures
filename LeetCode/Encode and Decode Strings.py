import unittest


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    # 4#lint4#code4#love3#you

    def decode(self, str):
        # write your code
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1:j + 1 + length])
            i = j + 1 + length
        return res


class TestEncodeDecode(unittest.TestCase):
    val_1 = ['lint', 'code', 'love', 'you']
    val_2 = ['Hello', 'c$#$#$ode', 'lo4543ve', 'yo224u']
    val_3 = '5#Hello9#c$#$#$ode8#lo4543ve6#yo224u'

    def test_encode(self):
        obj = Solution()
        self.assertEqual(obj.encode(self.val_1), '4#lint4#code4#love3#you')
        self.assertEqual(obj.encode(self.val_2), '5#Hello9#c$#$#$ode8#lo4543ve6#yo224u')
        self.assertEqual(obj.decode(self.val_3), ['Hello', 'c$#$#$ode', 'lo4543ve', 'yo224u'])


if __name__ == "__main__":
    unittest.main()
