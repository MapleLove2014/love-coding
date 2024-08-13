class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s1=set()
        s2=set()
        for i in range(len(s) - 9):
            if s[i:i+10] not in s1:
                s1.add(s[i:i+10])
            else:
                s2.add(s[i:i+10])
        return list(s2)

