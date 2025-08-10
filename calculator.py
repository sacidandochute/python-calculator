from math import sqrt

print("calculadora versão 1.5\n")  
print("REPORTAR PROBLEMAS!\n")
print("GRAÇAS AO DEEPSEEK, A VERSÃO 1.5 EXISTE!\n")

historico = []

while True:
    print("Qual modo de calcular? (*, /, +, -, exp, sqrt):")  
    modo = input().strip().lower()

    # --- FASE ESPECIAL PARA RAÍZ QUADRADA --- NÃO TRADUZIR PARA OUTRO IDIOMA ---
    if modo == "sqrt":
        print("\nDigite o número para raíz quadrada:")
        num1 = float(input())
        if num1 >= 0:
            resultado = sqrt(num1)
        else:
            resultado = "Erro: número negativo!"
        print("\nResultado:", resultado)
        historico.append(f"√{num1} = {resultado}")
    else:
        # --- OPERAÇÕES NORMAIS --- NÃO TRADUZIR PARA OUTRO IDIOMA ---
        print("\nDigite o primeiro número:")  
        num1 = float(input())  
        print("Digite o segundo número:")  
        num2 = float(input())

        if modo == "*": resultado = num1 * num2
        elif modo == "/": resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero!"  
        elif modo == "+": resultado = num1 + num2
        elif modo == "-": resultado = num1 - num2
        elif modo == "exp": resultado = num1 ** num2
        elif modo == "deepseek":
            print("┌───────────────────────────────────────────────┐")
            print("│     CALCULADORA VERSÃO 1.5.3 POR DEEPSEEK     │")
            print("│        ➤  COLABORAÇÃO IA-HUMANA              │")
            print("└───────────────────────────────────────────────┘")
            resultado = "🔓 Easter Egg desbloqueado!"
        else:  
            resultado = "Modo inválido!"
            print(resultado)
            continue  # Pular para próximo loop se inválido

        print("\nResultado:", resultado)
        historico.append(f"{num1} {modo} {num2} = {resultado}")

    # Continuar? 
    if input("\nContinuar? (s/n): ").lower() != "s":
        print("\nHistórico:", "\n".join(historico))
        break