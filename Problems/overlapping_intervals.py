# TODO

class Solutions:
  def overlapping(self, li):
    l2 = []
    i = 0
    j = 0
    n = len(li)
    while i < n:
      flag = 0
      print('nishaa', j)
      while j < len(li) - 1:
        print('j: ', j, li[j][1])
        if li[j][1] >= li[j+1][0]:
          flag = 1
          new_elem = [li[j][0], li[j+1][1]]
          del li[j]
          del li[j]
          print('after del: ', li, j)
          li.insert(j, new_elem)
          j += 2
        else:
          j += 1
      i = i + 1
      print(li)
      if flag == 0:
        break

def main():
  s = Solutions()
  # li = [[1,3],[2,6],[8,10],[15,18]]
  # li = [[1,3],[2,6]]
  # li = [[1,4],[4,5]]
  li = [[1,3],[2,9],[8,16],[15,18]]
  s.overlapping(li)

if __name__ == '__main__':
  main()

