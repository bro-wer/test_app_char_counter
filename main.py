import sys

def ValidateArgsCount():
    if len(sys.argv) != 2:
        raise Exception("Unexpected args count!")

if __name__ == '__main__':
    try:
        ValidateArgsCount()
        print(str(len(sys.argv[1])))
    except Exception as e:
        print(e)
