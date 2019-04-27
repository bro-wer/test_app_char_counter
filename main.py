import sys

def ValidateArgsCount():
    if len(sys.argv) != 2:
        raise Exception("Unexpected args count!")

def CountCharacters():
    print(str(len(sys.argv[1])))

if __name__ == '__main__':
    try:
        ValidateArgsCount()
        CountCharacters()
    except Exception as e:
        print(e)
