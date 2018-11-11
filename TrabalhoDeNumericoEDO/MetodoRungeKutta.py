import numpy as np
import matplotlib.pyplot as plt

def montaGrafico ( xResp, yResp, yPrev ) :
    """

    Função que monta os gráficos

    """

    plt.figure ( 0 )
    plt.plot ( xResp, yResp, "--r", linewidth = 2 )
    plt.xlabel("tempo (s)")
    plt.ylabel("Número de indivíduos")
    plt.title ( "Números de indivíduos por tempo" )
    plt.grid ( True )

    plt.plot ( xResp, yPrev, "--b", linewidth = 2  )
    plt.xlabel("tempo (s)")
    #plt.rcParams['figure.figsize'] = (0.0001,1)
    plt.ylabel("Número de indivíduos")
    plt.title ( "Números de indivíduos por tempo" )
    plt.legend ( ["Valor Real", "Aproximação"] )
    plt.grid ( True )
    #plt.rcParams['figure.figsize'] = (1000,0.01)
    plt.show (  )

    return

def montaVetorOriginal ( h = 0, k = 0, r = 0, yo = 0, xo = 0, totalint = 0, ) :
    """
    Função que monta o valor estimado
    dos valores originais

    """
    passo = 0
    tam = totalint + 1
    vetorX = np.zeros ( tam )
    vetorY = np.zeros ( tam )

    vetorX[0] = 0
    vetorY[0] = yo

    for i in range ( 0, totalint ) :

        xo += h
        e = np.exp ( r*xo )
        part1 = e*yo*k
        part2 = k + ( e - 1 )*yo
        y = part1/ part2

        vetorX[i+1] = xo
        vetorY[i+1] = y

    return vetorX, vetorY

def main ( ) :

    y = float ( input ( "Digite o valor inicial de Yo : " ) )   # valor inicial de y ( 0 ) = 1
    a = float ( input ( "Digite o valor do intervalo a : " ) )
    b = float ( input ( "Digite o valor do intervalo b : " ) )
    h = float ( input ( "Digite o valor do espaçamento dos valores : " ) )
    r = float ( input ( "Digite o valor de r : " ) )
    k = float ( input ( "Digite o valor de k : " ) )

    totalint = int( ( b - a ) /h)     # número total de interações
    tam = totalint + 1
    arrayResultados = np.zeros ( tam )     # vetor que contém o resultado de cada interação
    f = 0       # valor de f( x, y(x) )
    Yo = y
    arrayResultados[0] = y

    arrayX, arrayY = montaVetorOriginal (
        h = h,
        r = r,
        k = k,
        yo = Yo,
        totalint = totalint
     )

    y = Yo

    for i in range ( 0, totalint ) :

        f = ( 1 - ( y/k ) )*( r*y )

        k1 = f
        k2 = f + ( (k1*h)/2 )
        k3 = f + ( (k2*h)/2 )
        k4 = f + h*k3

        soma = ( k1 + ( 2*k2 ) + ( 2*k3 ) + k4 )

        y = y + ( ( soma*h )/6)

        arrayResultados[i+1] = y

    print ( "Array resultado Previsão : {}\n" .format ( arrayResultados) )
    print ( "Array valores Reais : {}\n" .format ( arrayY ) )
    print ( "Array valores de x : {}".format ( arrayX ) )
    print ( "Tam arrayResultados : {}\n".format ( len ( arrayResultados ) ) )

    montaGrafico (
        xResp = arrayX,
        yResp = arrayY,
        yPrev = arrayResultados
    )

if __name__ == '__main__':
    main()
