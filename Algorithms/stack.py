class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
            print(f"Pushed {item} into the stack.")
        else:
            print("Stack overflow! Cannot push more items.")

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack underflow! Cannot pop from an empty stack.")

    def is_empty(self):
        return not bool(self.stack)

    def is_full(self):
        return len(self.stack) == self.capacity

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def count(self):
        return len(self.stack)

    def change(self, position, new_item):
        if 0 <= position < len(self.stack):
            self.stack[position] = new_item
            print(f"Changed item at position {position} to {new_item}.")
        else:
            print("Invalid position!")

    def display(self):
        if self.stack:
            print("Current stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty.")


# Example usage:
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)  # Will result in stack overflow

print("Stack is full:", stack.is_full())

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()  # Will result in stack underflow

print("Stack is empty:", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element of the stack:", stack.peek())

print("Number of elements in the stack:", stack.count())

stack.change(1, 25)

stack.display()