# Date: 17-Feb-2020
# Find the minimum distance to cover the each point of an array X and Y.

class Solutions:
  def coverPoints(self, x_li, y_li):
    dis = 0
    for i in range(1, len(x_li)):
      x = abs(x_li[i] - x_li[i-1])
      y = abs(y_li[i] - y_li[i-1])
      dis += max(x, y)
    return dis      

def main():
  s = Solutions()
  x = [0, 2, 1]
  y = [-1, -2, 1]
  print(s.coverPoints(x, y))

if __name__ == '__main__':
  main()
