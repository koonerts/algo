"""
Main

"""
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate_list(head, -2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to main
    print(main([]))
