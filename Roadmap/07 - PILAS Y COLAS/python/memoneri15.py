"""
Ejercicio
"""

# Pila/Stack (LIFO)

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack(len(stack) - 1)
print(stack_item)

print(stack.pop())

print(stack)

# Cola/Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
Extra
"""

# web


def web_navigation():

    stack = []

    while True:

        action = input(
            "Añade una URL o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            pass
        else:   
            stack.append(action)

        print(f"Has navegado a la web: {stack[len(stack) - 1]}")


  web_navigation()
