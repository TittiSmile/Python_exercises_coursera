#in python qual è la differenza tra:

class A:
    
    def __init__(self, nome, anni):
        self.nome=nome
        self.anni=anni
    def __str__(self):
        return "{} {}".format(self.nome, self.anni)

class B(A):
    def __init__(self, nome, anni, indirizzo):
        #A.__init__(self, nome, anni)		#QUESTO
        #super(B, self).__init__(self,nome,anni)	# E QUESTO	
        self.indirizzo=indirizzo

#non credo ci sia una differenza

********************************************************************************************************************************
"""
come sovrascrivo str dalla sottoclasse? nell'esempio di sopra, se stampo un oggetto di tipo B, mi stamperà solo nome ed anni
perchè B fa riferimento a str di A (che contiene solo nome ed anni)
"""
*******************************************************************************************************************************