class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
            print(f"Enqueued {item} into the queue.")
        else:
            print("Queue is full! Cannot enqueue more items.")

    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            print(f"Dequeued {item} from the queue.")
            return item
        else:
            print("Queue is empty! Cannot dequeue from an empty queue.")

    def is_empty(self):
        return not bool(self.queue)

    def is_full(self):
        return len(self.queue) == self.capacity

    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def count(self):
        return len(self.queue)

    def display(self):
        if self.queue:
            print("Current queue elements:")
            for item in self.queue:
                print(item)
        else:
            print("Queue is empty.")


# Example usage:
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # Will result in queue full

print("Queue is full:", queue.is_full())

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # Will result in queue empty

print("Queue is empty:", queue.is_empty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element of the queue:", queue.peek())

print("Number of elements in the queue:", queue.count())

queue.display()
