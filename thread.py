import threading
import time

def calcular_soma(lista):
    print(f"Calculando a soma dos números: {lista}")
    soma = sum(lista)
    print(f"Soma: {soma}")

def imprimir_numeros(inicio, fim):
    print(f"Imprimindo números de {inicio} a {fim}")
    for i in range(inicio, fim + 1):
        print(i)
        time.sleep(1)

numeros = [1, 2, 3, 4, 5]

thread1 = threading.Thread(target=calcular_soma, args=(numeros,))
thread2 = threading.Thread(target=imprimir_numeros, args=(1, 5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Tarefas concluídas!")
