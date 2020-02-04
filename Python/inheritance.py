# Inheritance in new style
class SolutionsP(object): # Object is neccessary to include as super is working for new style.
    def __init__(self):
        pass

    def print_name(self, name):
        print('name in parent: ', name)

class SolutionSub(SolutionsP):
    def __init__(self):
        pass

    def print_name(self, name):
        super(SolutionSub, self).print_name(name) # calling to parent class method
        print('name in sub: ', name)

def main():
    s = SolutionSub()
    print('********** NEW STYLE *******************')
    s.print_name('nisha')

if __name__ == '__main__':
    main()

# Inheritance in Old Style 
class SolutionsP: # In old style there is no object class
    def __init__(self):
        pass

    def print_name(self, name):
        print('name in parent: ', name)

class SolutionSub(SolutionsP):
    def __init__(self):
        pass

    def print_name(self, name):
        SolutionsP.print_name(self, name) # Need to call the parent class method
        # like this instead of super class as old style has no super method
        print('name in sub: ', name)

def main():
    s = SolutionSub()
    print('********** OLD STYLE *******************')
    s.print_name('nisha')

if __name__ == '__main__':
    main()