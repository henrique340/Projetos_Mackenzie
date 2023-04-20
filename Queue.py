class Queue:

    def __init__(self):
        self.queue = []

    #adicionar um elemento
    def enqueue(self, item):
        self.queue.append(item)

    #remove um elemento
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    #exibir a queue
    def display(self):
        print(self.queue)

    def size(self):
        print(len(self.queue))

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print('Depois de remover um elemento')
q.display()
q.size()