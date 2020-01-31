class fileOperations:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        fp = open(self.file_name) # By default, it will open in read mode
        print(fp.read()) # Returns the entire file content at one point
        if not fp.closed: # Check file is open or not
            fp.close()

    def readline_file(self):
        # No need to closed the file when using open with because open with
        # is a context manager which is responsible for taking care of closing
        # the file.        
        with open(self.file_name) as fp:
            while True:
                line = fp.readline()
                if line == '':
                    break
                else:
                    print(line)

    def readlines_file(self):
        fp = open(self.file_name)
        print(fp.readlines()) # Returns the entire rows in the list
        if not fp.closed: # Check file is open or not
            fp.close()

    def write_into_file(self):
        # For append the content into an existing file or create a new file if
        # not present.(w+ is also writing to the file and if file is not
        # present it will create it)
        fp = open(self.file_name, 'a')
        # While writing into a file we need to explicitly give the new line character.
        fp.write('I am writing a program to write into the file.\n')
        if not fp.closed: # Check file is open or not
           fp.close()       

def main():
    fo = fileOperations('test.txt')
    print('******* Read file by using read() *******')
    fo.read_file()
    print('******* Read file by using readline() *******')
    fo.readline_file()
    print('******* Read file by using readlines() *******')
    fo.readlines_file()
    print('******* Write into a file by using write() *******')
    fo.write_into_file()

if __name__ == '__main__':
    main()