class InvalidInputException(Exception):
    pass

class Node:
    def __init__(self, value=None, left=None, right=None, parent=None) -> None:
        self.key = value
        self.left = left
        self.right = right
        self.parent = parent

        # -1 if left heavy
        # 0 if balanced
        # 1 if right heavy
        self.balance_status = 0

        # left or right
        self.child_type = None


    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ',' + str(self.balance_status) + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])


class AVL:
    def __init__(self, root: Node=None) -> None:
        if root is None:
            self.root = None
        else:
            self.root = root

    # def _update_weights(self, node: Node) -> None:
    #     if not isinstance(node, Node):
    #         raise InvalidInputException("_update_weights needs a node as input")

    #     if node.parent:
    #         if node.child_type == "left":
    #             node.parent.balance_status -= 1
    #         if node.child_type == "right":
    #             node.parent.balance_status += 1

    def rotate_right(self, node: Node):
        node_x = node
        node_swap = node.left

        node_swap.parent = node.parent
        if node.child_type == "left":
            node.parent.left = node_swap
        if node.child_type == "right":
            node.parent.right = node_swap

        if node_swap.right:
            node.left = node_swap.right
            node.left.child_type = "left"
            node.left.parent = node


    def do_rotations(self, node: Node) -> None:
        if node:
            if node.child_type == 'left' and node.parent:
                node.parent.balance_status -= 1
                if node.parent.balance_status < 1:
                    self.rotate_right(node.parent)

            if node.child_type == 'right' and node.parent:
                node.parent.balance_status += 1
                if node.parent.balance_status > 1:
                    self.rotate_right(node.parent)

            if node.parent:
                self.do_rotations(node.parent)


    def insert(self, node: Node, current_node: Node=None) -> None:
        if self.root is None:
            self.root = node
            return

        if current_node is None:
            current_node = self.root

        if node.key < current_node.key:
            if current_node.left is None:
                current_node.left = node
                node.parent = current_node
                node.child_type = "left"
                self.do_rotations(node)
                # self._update_weights(node)
            else:
                self.insert(node, current_node.left)
        elif node.key > current_node.key:
            if current_node.right is None:
                current_node.right = node
                node.parent = current_node
                node.child_type = "right"
                self.do_rotations(node)
                # self._update_weights(node)
            else:
                self.insert(node, current_node.right)
        else:
            print("Special case, node already exists")

def main():
    try:
        nod = Node(value=15)
        avl = AVL()

        avl.insert(nod)
        for i in range(20):
            nod = Node(value=i)
            avl.insert(nod)

        print(avl.root)

        import pdb
        pdb.set_trace()
    except Exception as e:
        import traceback
        traceback.print_exc()
        import pdb
        pdb.set_trace()

if __name__ == '__main__':
    main()