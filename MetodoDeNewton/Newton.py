"""


"""

from math import exp, fabs

class Newton :

    def __init__(self, xo, precisao1, precisao2) :

        self.xo = xo
        self.precisao1 = precisao1
        self.precisao2 = precisao2
        self.stop = False
        self.raiz = float(0)
        self.interacao = 1
        self.erroFinal = 0

    def funcao(self, x):
        """
        Função que será como exemplo deste exercício
        na qual será : F ( x ) = e^(0.2x) - e^(-0.8x) - 2

        :param x: valor de x
        :return: o valor da função ao respectivo valor de x
        """

        return (exp(0.2 * x) - exp(-0.8 * x) - 2)

    def funcaoDerivada ( self, x ) :
        """
        Função que será como exemplo deste exercício
        na qual será : dF/dx ( x ) = (0.2)*e^(0.2x) + (0.8)*e^(-0.8x)

        :param x: valor de x
        :return: o valor da função ao respectivo valor de x
        """

        return ( (0.2)*exp(0.2*x) + (0.8)*exp(-0.8*x) )

    def calculoInteracao(self) :

        if (  fabs( self.funcao ( self.xo ) ) < self.precisao1 ) :

            self.raiz = self.xo
            self.stop = True

        while ((self.stop == False) and
               (self.interacao <= 20)) :

            x = self.xo - ( self.funcao ( self.xo )/self.funcaoDerivada ( self.xo ) )

            if ( ( abs(self.funcao(self.xo)) < self.precisao1 ) or
                   ( abs ( x - self.xo ) ) < self.precisao2 ) :

                self.raiz = x
                self.stop = True

            print("------ Interação {} ------ \n".format(self.interacao))
            print("Valor estimado da raiz : {}".format(self.xo))
            print("Erro 1 da interação {}".format(fabs(self.funcao(self.xo))))
            print("Erro 1 da máquina {}".format(self.precisao1))
            print("Erro 2 da interação {}".format(abs(x - self.xo)))
            print("Erro 2 da máquina {}\n".format(self.precisao2))
            print("-------------\n")

            self.xo = x
            self.interacao += 1

