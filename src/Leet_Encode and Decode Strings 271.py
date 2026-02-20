class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = [], 0

        while i < len(s):  # ✅ use s, the input string
            j = i
            while s[j] != "#":  # ✅ compare the character at s[j], not j itself
                j += 1

            length = int(s[i:j])  # ✅ parse length from s
            i = j + 1  # ✅ move past '#'
            res.append(s[i:i + length])
            i += length  # ✅ move i to start of next encoded chunk
        return res

    
#     def decode(self, s):
#     res , i = [] , 0

#     # str(len(s)) + "#" + s
#     while(i < len(str)):
#         j = i
#         while (j != "#"):
#             j+= 1
#         x = int(str[i:j])
#         res.append(str[j+1:j + 1 + length])
#         i = j + 1 + length
# return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
