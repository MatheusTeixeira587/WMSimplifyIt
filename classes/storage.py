import sqlite3

class Storage():

    def __init__(self,n_ruas,n_prateleiras,n_andares,n_posicoes,table = "storage"):
        
        self.table = table
        self.n_ruas = n_ruas
        self.n_prateleiras = n_prateleiras
        self.n_andares = n_andares
        self.n_posicoes = n_posicoes

        #posicoes = []
        #andares = [posicoes*n_posicoes]
        #prateleiras = [andares*n_andares]
        #rua = [prateleiras*n_prateleiras]
        #estoque = estoque[rua*n_ruas]

        estoque = []
        for i in range(n_ruas):            
            rua = []
            for j in range(n_prateleiras):                
                prateleira = []
                for k in range(n_andares): 
                    andar = []                  
                    for l in range(n_posicoes):
                        andar.append(0)
                    prateleira.append(andar)
                rua.append(prateleira)
            estoque.append(rua)

        def add_new(self,ruas,prateleiras,andares,posicoes):
            conn = sqlite3.connect("projetowms.db")
            cur = conn.cursor()

            conn.commit()
            conn.close()