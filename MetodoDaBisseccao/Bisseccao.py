"""

    Classe na qual realiza todo o cálculo
    do método da bisseção e retorna o valor
    aproximado da raiz da função

"""
from math import exp

class bisseccao :

    def __init__(self, intervaloInferior, intervaloSuperior, precisao ) :
        self.intervaloInferior = intervaloInferior
        self.intervaloSuperior = intervaloSuperior
        self.precisao = precisao
        self.interacao = 1
        self.M = self.funcao ( intervaloInferior )
        self.stop = False
        self.raiz = 0
        self.erroAux = self.M
        self.erroTotal = 0

    def funcao(self, x):
        """
        Função que será como exemplo deste exercício
        na qual será : F ( x ) = e^(0.2x) - e^(-0.8x) - 2

        :param x: valor de x
        :return: o valor da função ao respectivo valor de x
        """

        return (exp(0.2 * x) - exp(-0.8 * x) - 2)

    def comparacao(self, x):
        """

        Função que faz a comparação entre a diferenção do intervaloSuperior
        e do intervaloInferior comparada ao epsilon de máquina
        Caso o epsilon seja maior, ele faz as atribuições e para o programa

        :param x : valor de k-ésima interação
        :return : void
        """

        self.erroTotal = abs( self.intervaloSuperior - self.intervaloInferior )

        if ( self.erroTotal < self.precisao ) :

            self.stop = True
            self.raiz = x

        return

    def calculoIteracao(self) :

        while ( ( self.stop == False) and
                ( self.interacao <= 20 ) ) :

            x = ( self.intervaloSuperior + self.intervaloInferior )/2

            fx = (exp(0.2 * x) - exp(-0.8 * x) - 2)

            if ( self.M*fx > 0 ) :

                self.intervaloInferior = x

            else :

                self.intervaloSuperior = x

            print("\n" + "------ Interação {} ------".format(self.interacao))
            print("Intervalo a : {}".format(self.intervaloInferior))
            print("Intervalo b : {}".format(self.intervaloSuperior))
            print("Raiz estimada no intervalo : {}".format(x))
            # chamar a função de comparacao
            self.comparacao ( x )

            print("Erro da máquina : {}".format(self.precisao))
            print("Erro do intervalo ; {}".format(self.erroTotal))
            print(10 * "-" + "\n")
            self.interacao += 1

        self.raiz = x