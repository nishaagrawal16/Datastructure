# Check if two strings are permutation of each other.
# O(n)

# with two array for seprate frequency.
class Solution:
    def getFeqList(self, s1, s1Feq):
        for i in range(len(s1)):
            index = ord(s1[i]) - 97
            s1Feq[index] += 1

    def permutation(self, s1, s2):
        if len(s1) != len(s2):
            return 'No'
        # Fill 0 for all 26 letters 
        s1Feq = [0]*26
        s2Feq = [0]*26
        # Fill s1 letters freq on the corresponding s1Feq.
        self.getFeqList(s1, s1Feq)

        # Fill s2 letters freq on the corresponding s2Feq.
        self.getFeqList(s2, s2Feq)
        for i in range(len(s1Feq)):
            if s1Feq[i] != s2Feq[i]:
                return 'No'
        return 'Yes'

# Check if two strings are permutation of each other.
# O(n)=> Optimal solution

# Take only one array for both s1 and s2.
class Solution:
    def getFeqList(self, s1, s2, feq):
        for i in range(len(s1)):
            indexS1 = ord(s1[i]) - 97
            indexS2 = ord(s2[i]) - 97
            # Add 1 for s1 string indexes
            feq[indexS1] += 1
            # Substract 1 for s2 string indexes
            feq[indexS2] -= 1


    def permutation(self, s1, s2):
        if len(s1) != len(s2):
            return 'No'
        # Fill 0 for all 26 letters 
        feq = [0]*26
        self.getFeqList(s1, s2, feq)
        # See if there is any non-zero value in
        # feq array
        for i in range(len(feq)):
            if feq[i]:
                return 'No'
        return 'Yes'

                
s = Solution()
s1 = 'xyz'
s2 = 'zxy'
print(s.permutation(s1, s2))
