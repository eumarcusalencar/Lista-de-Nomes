nomes = []
print("selecione sua opção :")


while True:
    plz=(len(nomes))-1
    print("""

|-|-|-|-|-|-||-|-|-|-|-|-|Menu|-|-|-|-|-|-||-|-|-|-|-|-|


|1| - Adicionar Nome  

|2| - Excluir Nome 

|3| - Ver Lista 

|4| - Alterar Nome

|5| - Excluir ultimo nome 

|6| - Verificar se o nome está na lista 

|7| - Sair""")
    print(" ")
    opcao = int(input(">> "))

    if opcao == 1:
        addNome = input("\nEscreva o nome que você deseja adicionar : ")
        if addNome in nomes :
            print ("\n Esse nome já está na lista : ")

        else:
            nomes.append(addNome)
            print(" ")
            print("Nome adicionado com sucesso: ")

    if opcao == 2:
         print("\n Lista atual",nomes,"\n insira a posição : ")
         posicao = int(input(">> "))
         del(nomes[posicao - 1])
         print(" ")
         print(" Nome excluido com sucesso")


    if opcao == 3:
        print(nomes)

    if opcao==4:
        alter=input("Qual nome deseja alterar ? ")
        

        try:
            posicao = nomes.index(alter)
            nomes.remove(alter)
            new=input("Qual novo nome deseja inserir : ")
            nomes.insert(posicao,new)
            print(" Nome substituido com sucesso")
        except:
            print("O nome informado não esta na lista.")
                     

    if opcao ==5:
        nomes.pop()
        print("Ultimo nome excluido com sucesso")



    if opcao ==6:
        vrfnome = input(" Digite o nome que voce deseja verificar :")
        print(nomes.index(vrfnome))

        if True:
            print(" O nome pertence a lista !")

        else:
            print(" O nome não pertence a lista !")
  
    if opcao == 7:
        exit = int(input("""

Deseja mesmo sair ?

[1]- Sim

[2]- Não

"""))
    if exit == 1:
        print("Programa encerrado")

        break

        print()
        
