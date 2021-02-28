# Implemente uma classe chamada 'aluno' com atributos nome, endereco e lista de notas (floats)
# Nome e endereço são fornecidos na criação do objeto
# Método setNota(float) recebe nota e insere na lista
# Método media() retorna a média das notas do aluno
# Método imprimeDados() imprime dados do aluno: nome, endereço e média das notas
# O programa deve pedir nome e endereço do aluno e criar um objeto com estes dados
# Em seguida, pede algumas notas e armazena-as, e mostra os dados (nome, endereço e média)

class aluno:
    nome = None
    endereco = None 
    notas = []
    quant = None
    média = None

    def __init__(self):
        self.nome = input("Digite o NOME do aluno:")
        self.endereco = input("Digite o ENDEREÇO do aluno:")
    
    def  setNota(self):
        self.quant = int(input("Digite quantas notas serão digitadas:"))
        cont = 1
        while  cont < (self.quant+1):
            nota = float(input(f"Digite a nota {cont} do aluno:"))
            self.notas.append(nota)
            cont += 1

    def media(self):
        self.média = sum(self.notas)/self.quant
        return self.média 

    def imprimeDados(self):
        print("=========="*10)
        print("\t\t\tDADOS DO ALUNO DIGITADO")
        print(f"\t\t\tALUNO:{self.nome}")
        print(f"\t\t\tENDEREÇO:{self.endereco}")
        print(f"\t\t\tMÉDIA:{self.média}")
        print("=========="*10)
############################################################################
a = aluno()
a.setNota()
a.media()
a.imprimeDados()