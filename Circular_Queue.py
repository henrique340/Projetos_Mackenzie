class MyCircularQueue():

    def __init__(self, tam):
        self.tam = tam
        self.queue = [None] * tam
        self.head = self.tail = -1

    # Insere um elemento dentro de uma queue circular
    def enqueue(self, elemento):

        if ((self.tail + 1) % self.tam == self.head):
            print("A queue circular está cheio\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = elemento
        else: # add um elemento substituindo o primeiro (head)
            self.tail = (self.tail + 1) % self.tam
            self.queue[self.tail] = elemento

    # Remove um elemento da queue circular
    def dequeue(self): # queue vazia
        if (self.head == -1):
            print("A queue circular está cheia\n")

        # queue com 1 elemento
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.tam
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("Não tem elemento da queue circular")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.tam):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("queue inicial")
obj.printCQueue()

obj.dequeue()
print("Depois de remover um elemento da queue")
obj.printCQueue()