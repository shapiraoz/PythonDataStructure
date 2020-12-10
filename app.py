
import  sys
from lists import Node
from lists import StuckList


def main():
    aName = raw_input("Please enter your name ")
    print("Your name in all capitals is", aName.upper(),
          "and has length", len(aName))

    l = StuckList()
    n = Node(7)
    l.push(n)
    l.push(Node(5))
    l.push(Node(20))
    l.print_list()
    print 'pop node is {}'.format(str(l.pop()))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
