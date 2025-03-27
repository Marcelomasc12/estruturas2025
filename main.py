# Criando um array de 5 posicoes vazias
class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE

    # Função que serve para definir se o array está vazio ou não
    def isEmpty(self):
        return self.size() == 0

    # Função que serve para retornar o número de elementos já armazenados no array
    def size(self):
        return self.insertPosition

    # Função que serve para definir se precisamos de mais memória
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)

    # Função para inserir um novo elemento na lista
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1

    # Função para aumentar a memória quando necessário
    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):  # Correção: iterar até self.insertPosition
            newArray[position] = self.elements[position]
        self.elements = newArray

    # Função para limpar o array
    def clear(self):
        self.elements = [None] * self.SIZE  # Simplificação
        self.insertPosition = 0

    # Função para remover o último elemento
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1

    # Função para remover um elemento em uma posição específica
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return ""
        removedElement = self.elements[position]
        index = position
        while index < self.insertPosition - 1:
            self.elements[index] = self.elements[index+1]
            index += 1
        self.insertPosition -= 1
        return removedElement

    # Função para remover um elemento em uma posição específica
    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1

    # Função para retornar um elemento em uma posição específica
    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]

# implementacao de uma pilha em Python
class PersonalStack:
    list = PersonalArray()

    # Funcao que insere um elemento na posicao 0 da nossa fila
    def push(self, newElement):
        self.list.insertAt(0, newElement)

    # Funcao que remove um elemento da fila (no caso sempre a ultima posicao)
    def pop(self):
        return self.list.removePosition(0)

# implementacao de uma fila em Python
class PersonalQueue:
    list = PersonalArray()

    # Funcao que insere um elemento na posicao 0 da nossa fila
    def enqueue(self, newElement):
        self.list.insertAt(0, newElement)

    # Funcao que remove um elemento da fila (no caso sempre a ultima posicao)
    def dequeue(self):
        return self.list.removePosition(self.list.size() - 1)


class BrowserHistory:
    def __init__(self):
        self.history = PersonalStack()
        self.forward_history = PersonalQueue()

    def navigate_to(self, url):
        self.history.push(url)
        self.forward_history.list.clear()

    def go_back(self):
        if self.history.list.size() <= 1:
            return None
        current_url = self.history.pop()
        self.forward_history.enqueue(current_url)
        return self.history.list.elementAt(0)

    def go_forward(self):
        if self.forward_history.list.isEmpty():
            return None
        next_url = self.forward_history.dequeue()
        self.history.push(next_url)
        return next_url

    def get_history(self):
        history = []
        for i in range(self.history.list.size()):
            history.append(self.history.list.elementAt(i))
        return history



browser = BrowserHistory()

browser.navigate_to("www.google.com")
browser.navigate_to("www.youtube.com")
browser.navigate_to("www.facebook.com")

print("Histórico:", browser.get_history())

print("Voltar:", browser.go_back())
print("Histórico:", browser.get_history())

print("Avançar:", browser.go_forward())
print("Histórico:", browser.get_history())
