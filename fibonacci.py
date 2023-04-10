num = input("Digite um numero para verificar se pertence a sequência de fibonacci: ")
try:
    num = int(num)
except:
    print("Digite o numero inteiro.")
else:
    a = 0
    b = 1
    while b < num:
        temporario=b
        b= a + b
        a=temporario
    if b == num:
        print(f"{num} pertence a sequencia de fibonacci.")
    else:
        print(f"{num} não pertence a sequencia de fibonacci.")