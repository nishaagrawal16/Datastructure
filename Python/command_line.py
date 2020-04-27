import sys
class Solutions:
    def abc(self):
        pass

def main(argv):
    print(len(argv), argv)
    s = Solutions()
    print (dir(s))

if __name__ == '__main__':
    main(sys.argv)

# Output:
# -------
# (1, ['command_line.py'])
# ['__doc__', '__module__', 'abc']
