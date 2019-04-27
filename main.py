import sys

if __name__ == '__main__':
    try:
        print("Args count = " + str(len(sys.argv)))
    except Exception as e:
        print(e)
