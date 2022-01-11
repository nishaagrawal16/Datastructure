# How many permutation of s1 string into s2.

class Solution:
    def getFeqList(self, s1, s1Feq):
        for i in range(len(s1)):
            index = ord(s1[i]) - 97
            s1Feq[index] += 1

    def permutation(self, s1, s2):
        # Fill 0 for all 26 letters 
        s1Feq = [0]*26
        s2Feq = [0]*26
        # fill s1 letters freq on the corresponding s1Feq.
        self.getFeqList(s1, s1Feq)

        totalPermutations = 0
        # Fill starting letters freq of s2 in s2Feq
        for i in range(len(s1)):
            index = ord(s2[i]) - 97
            s2Feq[index] += 1
        # right index
        r = len(s1) - 1
        result = []
        for i in range(len(s2)):
            count = 0
            for j in range(len(s1Feq)):
                if s1Feq[j] == s2Feq[j] == 1:
                    count += 1
                    if count == len(s1):
                        totalPermutations += 1
                        result.append(s2[i: r+1])
                        break
                    
            index = ord(s2[i]) - 97
            s2Feq[index] -= 1

            if  r < len(s2) - 1:
                r += 1
                index = ord(s2[r]) - 97
                s2Feq[index] += 1
        return len(result), result

                
s = Solution()
s1 = 'abc'
s2 = 'abcadcdabcab'
print(s.permutation(s1, s2))
