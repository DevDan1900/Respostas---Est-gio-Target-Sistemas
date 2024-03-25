## QUESTÃO 1
INDICE = 13
SOMA = 0 
K = 0

while K < INDICE:  
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

## QUESTÃO 2
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    numero = int(input("Digite um número para verificar se pertence: "))
    
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência")
    else:
        print(f"O número {numero} não pertence à sequência")

if __name__ == "__main__":
    main()

## QUESTÃO 3
#a) 1, 3, 5, 7, 9
    #Número anterior + 2 = 9
#b) 2, 4, 8, 16, 32, 64, 128
    #Número Anterior multiplicado por 2 = 128
#c) 0, 1, 4, 9, 16, 25, 36, 49
    #Adicionando números ímpares e soma ao último (13+36) = 49
#d) 4, 16, 36, 64, 100
    #Cada número é igual ao quadrado da sequencia de número par (10**2) = 100
#e) 1, 1, 2, 3, 5, 8, 13
    #Soma o numero atual mais o anterior (8+5) = 13
#f) 2,10, 12, 16, 17, 18, 19, 200
    #Sequencia de números qu começam com a letra D. Próximo será Duzentos = 200
    
## QUESTÃO 4
import time

def descobrir_interruptores_lampadas():
    # Ligar o primeiro interruptor
    print("Ligando o primeiro interruptor...")
    time.sleep(2)  
    print("Desligando o primeiro interruptor...")
    time.sleep(1) 
    print("Ligando o segundo interruptor...")
    time.sleep(2)  
    print("Desligando o segundo interruptor...")
    time.sleep(1)  
    
    estado_lampada_1 = "acesa"
    estado_lampada_2 = "fria"
    estado_lampada_3 = "apagada"
    
    print("Estado da lâmpada 1:", estado_lampada_1)
    print("Estado da lâmpada 2:", estado_lampada_2)
    print("Estado da lâmpada 3:", estado_lampada_3)
    
    if estado_lampada_1 == "acesa":
        print("O primeiro interruptor controla a lâmpada 1.")
    elif estado_lampada_2 == "fria":
        print("O segundo interruptor controla a lâmpada 2.")
    else:
        print("O terceiro interruptor controla a lâmpada 3.")

descobrir_interruptores_lampadas()

#A lâmpada acesa está associada ao interruptor que você ligou na primeira vez.
# A lâmpada que não foi tocada (fria) está associada ao interruptor que você ligou na segunda vez.
# A lâmpada restante está associada ao interruptor que não foi utilizado.


## QUESTÃO 5
def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

texto = input("Digite um texto para inverter: ")
texto_invertido = inverter_string(texto)
print("String invertida:", texto_invertido)
