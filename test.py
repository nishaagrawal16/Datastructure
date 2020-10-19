# Date: 19-Oct-2020
# Find the given strings has only one letter edit away.

def oneEditAway(str1, str2):
    edit_count = 0
    # When both strings are of same length
    if len(str1) == len(str2):
        if str1 == str2:
            return False
        else:
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    edit_count += 1
                if edit_count > 1:
                    return False            
    elif len(str2) - len(str1) > 1 or len(str1) - len(str2) > 1:
        # Strings length difference is greater than 1.
        return False
    else: # Length difference is exactly one.
        if str1 not in str2 and str2 not in str1:
            return False
    return True

def main():
    str1 = 'abc'
    str2 = 'abd'
    if oneEditAway(str1, str2):
        print('both strings are one letter edit away')
    else:
        print('both strings are not one letter edit away')

if __name__ == '__main__':
    main()
