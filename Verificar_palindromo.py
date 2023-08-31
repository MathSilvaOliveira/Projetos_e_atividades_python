import re

def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

def sem_especiais(text):
       texto_sem_especiais = re.sub(r'[^\w\s]','', text)
       return texto_sem_especiais


a = input("Digite uma palavra ou frase: ")
texto_sem_caracte_especial = sem_especiais(a)

if eh_palindromo(texto_sem_caracte_especial):
        print("A string é um palíndromo, após remover caracteres especiais")
else:
        print("A string não é um palíndromo, após remover caracteres especiais")
