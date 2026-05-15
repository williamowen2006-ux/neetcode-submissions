class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":  # find the # delimiter
                j += 1
            length = int(s[i:j])  # read the length
            res.append(s[j+1 : j+1+length])  # read exactly that many chars
            i = j + 1 + length  # move pointer forward
        return res