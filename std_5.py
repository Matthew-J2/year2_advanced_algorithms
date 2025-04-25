class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def insert(self, val_before, new_data):
        """Inserts a new value into the linked list."""
        if val_before is None:
            print("No node to insert after")

        else:
            # Instantiates a new node and updates headers.
            new_node = Node(new_data)
            new_node.nextval = val_before.nextval
            val_before.nextval = new_node


def main():
    list = SLinkedList()
    list.headval = Node("Mon")

    e2 = Node("Tue")
    e3 = Node("Thur")
    e4 = Node("Fri")
    e5 = Node("Sat")
    list.headval.nextval = e2
    e2.nextval = e3
    e3.nextval = e4
    e4.nextval = e5

    list.AtEnd("Sun")
    list.insert(e2, "Weds")
    list.listprint()


if __name__ == "__main__":
    main()