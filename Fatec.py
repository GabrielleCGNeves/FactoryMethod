# class Transporte()

# class Navio(Transporte)

# class Caminhao(Transporte)

# class Factory()
#     def criar_transporte(self, transporte):
#         if transporte == caminhao:
#             return Caminhao()
#         if transporte == navio:
#             return Navio()
        

# class Creator()
      
# class Factory_Caminhao()
#     def criar_transporte()
#         return Caminhao()
    
# class Factory_Navio()
#     def criar_transporte()
#         return Caminhao()

# factory = Factory()

# caminhao = factory.criar_transporte(caminhao)
# caminhao2 = factory.criar_transporte(caminhao)
# navio = factory.criar_transporte(navio)


from abc import ABC, abstractmethod

# As relações com as instituição devem ser: Aluno, Professor, Coordenador, Diretor, Administrativo ou Vestibulando;

# O programa deve utilizar deve analisar a relação com a instituição (FATEC) e apresentar uma das seguintes msg na interface:

#     "XXXXXXXX tem relação com a instituição como XXXXXXXXXXXXX"

# Caso não seja encontrado a relação com a instituição mostrar a msg na interface:

#     "XXXXXXXX não tem nenhuma relação com a instituição, acompanhar até a secretaria"

class Fatec(ABC):
    
    @abstractmethod
    def apresentar(self, nome):
        pass

class Aluno(Fatec):
    def apresentar(self, nome):
        print(f"O aluno {nome} tem relação com a Fatec.")

class Professor(Fatec):
    def apresentar(self, nome):
        print(f"O docente {nome} tem relação com a Fatec.")

class Coordenador(Fatec):
    def apresentar(self, nome):
        print(f"O coordenador acadêmico {nome} tem relação com a Fatec.")

class Diretor(Fatec):
    def apresentar(self, nome):
        print(f"O diretor acadêmico {nome} tem relação com a Fatec.")

class Administrativo(Fatec):
    def apresentar(self, nome):
        print(f"O responsável administrativo {nome} tem relação com a Fatec.")

class Vestibulando(Fatec):
    def apresentar(self, nome):
        print(f"O vestibulando {nome} tem relação com a Fatec.")

class Factory():
    def criar_relacao(self, relacao):
                
        match relacao:
            case 'aluno':
                return Aluno()
            
            case 'professor':
                return Professor()    
                
            case 'coordenador':
                return Coordenador()    

            case 'diretor':
                return Diretor()   

            case 'administrativo':
                return Administrativo()      
            
            case 'Vestibulando':
                return Vestibulando()
            
            case _:
                raise ValueError("Relação não encontrada")   
                 
def menu():
    return int(input("""
1 -- Consultar Situação
0 -- Sair
"""))

if __name__ ==  '__main__':
    nome = ''
    relacao = ''

    verificador = Factory()

    while True:
        chave = menu()

        match chave:
            case 1:
                nome = input("Insira o nome que deseja consultar: ")
                relacao = input("Insira a relação: ").lower()

                cargo = verificador.criar_relacao(relacao)

                cargo.apresentar(nome)
            
            case 0: 
                print("A aplicação será encerrada")
                raise SystemExit
