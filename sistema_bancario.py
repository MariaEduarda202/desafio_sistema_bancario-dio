
menu = '''

[a]depositar
[b] saque
[c] extrato
[d]sair


'''
saldo=0
limite = 500
extrato= ""
numero_de_saque=0
LIMITE_DE_SAQUE=3

while True:

 opcao = input(menu)

if opcao == "a":
  valor= float (input("Informe um valor"))
  if valor > 0:
   saldo += valor
  extrato+= f"desposito R${valor:.2fr}:/n"
 
else:print("Valor inválido")

if  opcao =="b":
   valor = float(input("Informe o valor do saque: "))

   excedeu_o_saldo= valor>saldo 
   excedeu_limite = valor > limite
   execedeu_saque= numero_de_saque >= LIMITE_DE_SAQUE 
  
if excedeu_saldo:
        print("Operação falhou! Você não possui saldo sufuciente.")



elif execedeu_limite:
  print ("Você execedeu o limite ")
 
elif execedeu_saque: print("Você execedeu o limite de saque")
 
elif valor > 0:
     saldo -= valor
     extrato += f'saque {valor:.2fr}'
     numero_de_saque += 1

if opcao =="c":
   
        print("\n=============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===============================")        
elif opcao =="d":
 break
else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")