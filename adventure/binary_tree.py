# This script creates a binary tree iterator


def create_tree_gas(alist: list):
    bt = None
    if alist != None and alist != []:
        bt = TreeGas(alist[0])
        for each in alist[1:]:
            bt.add(each)
    return bt


class TreeGas:
    """
    Agregar  las estaciones de Gas.
    """

    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.parent = None

    def add(self, data):
        ret = False
        if data == self.data:
            # error - skip it
            pass
        else:
            next = None
            if self.data > data:
                next = self.left
            else:
                next = self.right

            if next == None:
                node = TreeGas(data)
                node.parent = self
                if self.data > data:
                    self.left = node
                else:
                    self.right = node
                ret = True
            else:
                ret = next.add(data)
        return ret

    def to_list(self):
        alist = []

        if self.left:
            alist.append(self.left.to_list())
        alist.append(self.data)
        if self.right:
            alist.append(self.right.to_list())

        return alist


class Iter:
    """
    Recorrido de las estaciones de Gas.
    """

    def __init__(self, bt):
        self.bt = bt
        self.cur = None

    def begin(self):
        if self.bt.left:
            it = Iter(self.bt.left)
            return it.begin()
        else:
            return self.bt

    def end(self):
        if self.bt.right:
            it = Iter(self.bt.right)
            return it.end()
        else:
            return self.bt

    def next(self):
        bt = self.cur
        self.cur = None
        if bt.right:
            it = Iter(bt.right)
            self.cur = it.begin()
        else:
            while bt.parent and self.cur == None:
                if bt.parent.right != bt:
                    self.cur = bt.parent
                else:
                    bt = bt.parent

        return self.cur

    def set_current(self, node):
        self.cur = node

    def current(self):
        return self.cur


if __name__ == "__main__":

    alist = [60, 21, 95, 45, 120, 72, 65, 80, 0]
    bt = create_tree_gas(alist)
    print(f"list is {alist}")
    print(f"tree gas is {bt.to_list()}")

    it = Iter(bt)
    it.set_current(it.begin())
    print(f"it begin = {it.current().data} and it end {it.end().data}")

    while it.current() != it.end():
        print(f"in next= {it.next().data}")
