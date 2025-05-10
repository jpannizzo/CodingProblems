class QueueUsingStacks:
    '''
    Queues are FIFO while stacks are LIFO. 
    Using 2 stacks have a stack_in that stores the initial enqueue and a stack_out to reverse the stack during dequeue or peek.
    transfer_stacks() is only used if stack_out is empty.
    The last print statement in each function ends with 2 breaklines for readability.
    '''
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)
        print(f"Current stack_in: {self.stack_in}")
        print(f"Current stack_out: {self.stack_out}", end="\n\n")

    def dequeue(self):
        if not self.stack_out:
            self.transfer_stacks()

        print(f"Current stack_in: {self.stack_in}")
        print(f"Current stack_out before pop: {self.stack_out}", end="\n\n")

        if self.stack_out:
            return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            self.transfer_stacks()

        print(f"Current stack_in: {self.stack_in}")
        print(f"Current stack_out: {self.stack_out}")

        if self.stack_out:
            # return last item on stack_out
            return print(f"Top of the queue: {self.stack_out[-1]}", end="\n\n")
        
        return print("Top of the queue: None", end="\n\n")
        
    def transfer_stacks(self):
        # reverse order and put into stack out
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

qus = QueueUsingStacks()

qus.enqueue(10) # add 10 to queue
qus.peek() # check top of queue = 10
qus.dequeue() # pop 10 off queue
qus.peek() # check top of queue. queue is empty. top of queue = None
qus.dequeue() # verify no error when dequeue empty queue
qus.enqueue(3) # add 3 to queue
qus.enqueue(7) # add 7 to queue
qus.enqueue(11) # add 11 to queue
qus.peek() # check top of queue = 3
qus.enqueue(44) # add 44 to queue
qus.dequeue() # pop 3 off queue
qus.peek() # check top of queue = 7
qus.enqueue(4) # add 4 to queue
qus.dequeue() # pop 7 off queue
qus.dequeue() # pop 11 off queue
qus.dequeue() # pop 44 off queue. stack_in transfers to stack_out
qus.dequeue() # pop 4 off queue
qus.dequeue() # empty queue so nothing is popped
qus.peek() # return None. empty queue
