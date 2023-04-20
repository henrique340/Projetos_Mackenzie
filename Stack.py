#criando um stack
def Criar_Stack():
    stack = []
    return stack

#checando se a stack está vazia
def Stack_empty(stack):
    return len(stack) == 0

#addicionando itens na stack
def Push_stack(stack, item):
    stack.append(item)
    print('item adicionado: '+ item)

#removendo um item
def Pop_stack(stack):
    if Stack_empty(stack):
        return 'stack está cheia'
    return stack.pop()

stack = Criar_Stack()
Push_stack(stack, str(1))
Push_stack(stack, str(2))
Push_stack(stack, str(3))
Push_stack(stack, str(4))
print('item deletado: '+ Pop_stack(stack))
print('stack depois de deletar um elemento: ', stack)

