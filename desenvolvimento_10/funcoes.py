def calculadora(num1, num2, operacao):
  if operacao == "somar": 
    return num1 + num2
  elif operacao == "subtrair":
    return num1 - num2
  elif operacao == 'multiplicar':
    return num1 * num2
  elif operacao == "dividir":
    if num1 >= num2: 
      return num1 / num2
  else: 
      return 0
    
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite uma das operações (somar, subtrair, dividir, multiplicar) :")

resultado = calculadora(num1, num2, operacao)

print(f"Você escolheu a operação {operacao} e o resultado é {resultado}")