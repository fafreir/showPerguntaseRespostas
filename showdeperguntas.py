print('-' * 90)
print("Bem vindo ao Show de Perguntas e Respostas. ")
print('-' * 90)

perguntas = [['Quem descobriu o Brasil?'],
             ['Qual é o apelido de Edson Arantes do Nascimento?'],
             ['Em que ano terminou a 1ª Guerra Mundial? '],
             ['Atualmente (2022), quem é o CEO da Microsoft? '],
             ['Qual é o nome do fundador do Alibaba? '],
             ['Quais dessas empresas pertencem ao grupo Alphabet? '],
             ['Atualmente (2022), qual é a moeda oficial do Cazaquistão? ']]

opcoes = [["Pero Vás de Caminha", "Vasco da Gama", "Pedro Alvares Cabral", "Cristóvão Colombo"],
          ["Zito", "Zidane", "Rivelino", "Pelé"],
          ['1914', '1918', "1939", "1945"],
          ['Bill Gates', 'Satya Nadella', 'Sundar Pichai', 'Tim Cook'],
          ['Jack Ba', 'Jack Ma', 'Jack Na', 'Jack Ta'],
          ['Apple', 'Amazon', 'Google', 'Facebook'],
          ['Benge', 'Menge', 'Tenge', 'Zenge']]

answer = [["Pedro Alvares Cabral"], ["Pelé"], ["1918"], ['Satya Nadella'], ['Jack Ma'], ['Google'], ['Tenge']]


rcerta = 0
i = 0
rinc = 0

while i < len(perguntas):
    print(f'Pergunta {i + 1}')
    print(str(perguntas[i])[1:-1])
    print()

    y = 0
    while y < 4:
        print(f'{y + 1} {opcoes[i][y]}')
        y += 1

    print()
    correta = int(input("Valendo ... Escolha a opção/numeração correta (1,2,3,4) : "))
    correta -= 1
    print(f"Sua resposta: {opcoes[i][correta]}")

    a = list((str(answer[i])[1:-1]).split("'"))[1:-1]
    b = list((opcoes[i][correta]).split(","))

    if a == b:
        print("*" * 50)
        print("Uhullll, Parabéns sua resposta está correta")
        rcerta += 1
        print("*" * 50)

    else:
        print("*" * 50)
        print("Resposta Incorreta")
        print(f"A opção correta é: {str(a)[1:-1]}")
        rinc += 1
        print("*" * 50)
    print()

    i += 1
print(f"Parabéns, você acertou {rcerta} pergunta(s)")
print(f'Você errou {rinc} pergunta(s)')