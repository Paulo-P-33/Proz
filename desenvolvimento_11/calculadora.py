#Calculadora que será executada até o usuário mandar sair

def calculadora(num1, num2, operacao):
  if operacao == 1: 
    return num1 + num2
  elif operacao == 2:
    return num1 - num2
  elif operacao == 3:
    return num1 * num2
  elif operacao == 4:
    if num1 >= num2: 
      return num1 / num2
  else: 
      return 0

while True:
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  print("\n1 - somar\n2 - subtrair\n3 - multiplicar\n4 - dividir\n0 - sair\n")
  operacao = int(input("Escolha uma das operações acima:"))
  resultado = calculadora(num1, num2, operacao)
  if resultado == 0:
    print("Calculadora encerrada!")
    break    
  print(f"Você escolheu a operação {operacao} e o resultado é {resultado}\n")


