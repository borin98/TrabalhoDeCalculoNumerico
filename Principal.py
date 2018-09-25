# baixar as pastas MetodoDaBisseccao e MetodoDeNewton 
# e colocar no mesmo diretório para funcionar o algoritmo

from MetodoDaBisseccao import Bisseccao
from MetodoDeNewton import Newton

def main (  ) :

    print(5*"-"+" Método da Bissecção "+5*"-"+"\n")

    a = float( input ( "Digite o valor do intervalo de a : " ) )
    b = float( input ( "Digite o valor do intervalo de b : " ) )
    epsilon = float( input ( "Digite o valor do epsion1 de máquina : " ) )

    bisseccao = Bisseccao.bisseccao ( a, b, epsilon )
    bisseccao.calculoIteracao()

    print("\n----------- Dados Finais -----------\n")
    print("Intervalo a : {}".format(a))
    print("Intervalo b : {}".format(b))
    print("Raiz estimada : {}".format(bisseccao.raiz))
    print("Interação Totais : {}".format(bisseccao.interacao))
    print("---------------------------------------\n")

    print(5 * "-" + " Método de Newton " + 5 * "-" + "\n")

    epsilon1 = float(input("Digite o valor do epsion1 de máquina : "))
    epsilon2 = float(input("Digite o valor do epsion2 de máquina : "))
    xo = float ( input ( "Digite o valor de xo : " ) )

    newton = Newton.Newton( xo, epsilon1, epsilon2 )
    newton.calculoInteracao()
    print("\n----------- Dados Finais -----------\n")
    print("Valor de xo : {}".format(xo))
    print("Valor da raiz : {} ".format ( newton.raiz ) )
    print("Interações Totais : {}".format(newton.interacao))
    print("---------------------------------------\n")

if __name__ == '__main__':
    main()
