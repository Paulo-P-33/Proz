controlador = False

while (controlador == False):
  try: 
    nome = input("Digite seu nome completo: ")
    data_nascimento = int(input("digite o seu ano de nascimento: "))
    idade = 2023 - data_nascimento

    print(f"Seu nome é {nome} e sua idade é {idade} anos!")
    controlador = True
  except:
    print("Você digitou um valor inválido!\n")