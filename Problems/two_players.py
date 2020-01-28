# ****************************************************************************
# There are two players which are playing a game in which each player has 
# assign a character. He needs to remove the character which are more than
# one in a adjacent sequence and get the hightest score. Suppose P1 has 'a'
# and P2 has 'x'. P1 needs to delete aa and aaa and save only one character.
# Simlarly P2 needs to do this for x character.
# O(n)
# ****************************************************************************


class Solution(object):
  # O(n2)
  def count_max_score(self, str1):
    p1_score = 0
    p2_score = 0
    i = 0
    j = 0
    while(i < len(str1)):
      if str1[i] == 'a':
        # if i == 15:
        #   import pdb; pdb.set_trace()
        j = i + 1
        count = 0
        while(j < len(str1)):
          if str1[j] == 'a':
            count = count + 1              
          else:
              i = j
              break
          j = j + 1
        if count != 0:
           p1_score = p1_score + 1

      # Needs to break here otherwise it will become the infinite loop.
      if (j == len(str1)):
        break

      count = 0
      if str1[i] == 'x':
        j = i + 1
        while(j < len(str1)):
          if str1[j] == 'x':
            count = count + 1
          else:
              i = j
              break
          j = j + 1
        if count != 0:
          p2_score = p2_score + 1
    print('P1 score= {} \nP2 score= {}'.format(p1_score, p2_score))  

  # O(n) Here we need two flags, one for 'a' and another for 'x'.
  def count_max_score_optimize(self, str1):
    p1_score = 0
    p2_score = 0
    a_flag = 0
    x_flag = 0
    i = 1
    while(i < len(str1)):
      if str1[i] == 'a':
        if str1[i-1] == 'a':
          a_flag = 1
        else:
          p2_score = p2_score + x_flag
          x_flag = 0

      if str1[i] == 'x':
        if str1[i-1] == 'x':
          x_flag = 1
        else:
          p1_score = p1_score + a_flag
          a_flag = 0
      i = i + 1
    p1_score = p1_score + a_flag
    p2_score = p2_score + x_flag

    print('P1 score= {} \nP2 score= {}'.format(p1_score, p2_score))  

def main():  
  s = Solution()
  s.count_max_score('axaaaxxxaxaxaaaaaaxaxaxa')
  s.count_max_score_optimize('axaaaxxxaxaxaaaaaaxaxaxa')
  
if __name__ == '__main__':
  main()
