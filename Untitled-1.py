
def printMatrix(matrix):
    print("\n\n")
    print("------------------Damas_Cinncinatus-----------")
    print("\n")
    print( "0 |  1  |  2  |  3  |  4  |  5  |  6  |  7 \n")
    print("--------------------------------------------")
    for fila in matrix:
         print ("  |  ".join(map(str,fila)))
         print ("-------------------------------------------")
    print("\n")
    print("")
    print("\n\n")
matrix=[[]]
matrix=[[' ' for x in range(8)]for y in range(8)]
n1=[0,2,4,6]
n2=[1,3,5,7]
#p es igual a posicion
for p in n1:
    matrix[0][p]="X"
    matrix[2][p]="X"
    matrix[6][p]="O"
for p in n2:
    matrix[1][p]="X"
    matrix[5][p]="O"
    matrix[7][p]="O"
printMatrix(matrix)
def movimientoX():
    print("X Turno: ")
    x=int(input("Entra el numero  fila: "))
    y=int(input("Entra el numero columna"))
    movimientoDerecha=False
    movimientoIzquierda=False
    cutDerecha=False
    cutIzquierda=False
    Respuesta=" "
    cut=" "
    if (str(matrix[x][y])=="X"):
        if(not y == 7 and not y==0):
            if(str(matrix[x+1][y+1])==" "):
                movimientoDerecha=True
            if(str(matrix[x+1][y-1])==" "):
                movimientoIzquierda=True
        elif(y==7):
            if(str(matrix[x+1][y-1]==" ")):
                cutIzquierda=True
        else:
            if(str(matrix[x+1][y+1])==" "):
                cutDerecha=True
        if(any([cutDerecha,cutIzquierda])):
            movimientoDerecha=False
            movimientoIzquierda=False
        if(any([movimientoDerecha,movimientoIzquierda])):
            if(movimientoDerecha):
                if(movimientoIzquierda):
                    Respuesta=input("moviemiento derecha o izquierda?respuesta con D o I:")
                    Respuesta=Respuesta.upper()
                else:
                    Respuesta="D"
            else:
                Respuesta="I"
        if(any([Respuesta=="D",Respuesta=="I"])):
            if(Respuesta=="D"):
                matrix[x-1][y+1]="X"
                matrix[x][y]=" "
                printMatrix(matrix)
            else:
                matrix[x+1][y-1]="X"
                matrix[x][y]=" " 
                printMatrix(matrix)
        elif(any([cutDerecha,cutIzquierda])):
            if(cutDerecha):
                if (cutIzquierda):
                    Respuesta=input("moviemiento derecha o izquierda?respuesta con D o I: ")
                    Respuesta=Respuesta.upper()
                else:
                    Respuesta="D"
            else:
                Respuesta="I"
        elif(any([Respuesta=="D",Respuesta=="I"])):
            if(Respuesta=="D"):
                matrix[x+1][y+1]=" "
                matrix[x+2][y+2]="X"
                matrix[x][y]=" "
                printMatrix(matrix)
            else:
                matrix[x+1][y-1]=" "
                matrix[x+2][y-2]="X"
                matrix[x][y]=" "
                printMatrix(matrix)
            if(not y>5 and not y <2):
                if(str(matrix[x+1][y+1])=="O"and not str(matrix[x+2][y+2])=="O" and not str(matrix[x+2][y+2])=="X"):
                    cutDerecha=True
                if(str(matrix[x+1][y-1])=="O"and not str(matrix[x+2][y-2])=="O" and not str(matrix[x+2][y-2])=="X"):
                    cutIzquierda=True
            elif(y>5):
                if(str(matrix[x+1][y-1])=="O"and not str(matrix[x+2][y+2])=="O" and not str(matrix[x+2][y-2])=="X"):
                    cutIzquierda=True
            else:
                 if(str(matrix[x+1][y+1])=="O"and not str(matrix[x+2][y+2])=="O" and not str(matrix[x+2][y+2])=="X"):
                    cutDerecha=True
        else:
                print("Movimiento Invalido!!Intente de nuevo.....")
                movimientoX()
    else:
            print("No es corecto")
            movimientoX()
def movimientoO():
    print("X Turno: ")
    x=int(input("Entra el numero  fila: "))
    y=int(input("Entra el numero columna"))
    movimientoDerecha=False
    movimientoIzquierda=False
    cutDerecha=False
    cutIzquierda=False
    Respuesta=" "
    cut=" "
    if (str(matrix[x][y])=="X"):
        if(not y == 7 and not y==0):
            if(str(matrix[x-1][y+1])==" "):
                movimientoDerecha=True
            if(str(matrix[x-1][y-1])==" "):
                movimientoIzquierda=True
        elif(y==7):
            if(str(matrix[x-1][y-1]==" ")):
                cutIzquierda=True
        else:
            if(str(matrix[x-1][y+1])==" "):
                cutDerecha=True
        if(any([cutDerecha,cutIzquierda])):
            movimientoDerecha=False
            movimientoIzquierda=False
        if(any([movimientoDerecha,movimientoIzquierda])):
            if(movimientoDerecha):
                if(movimientoIzquierda):
                    Respuesta=input("moviemiento derecha o izquierda?respuesta con D o I:")
                    Respuesta=Respuesta.upper()
                else:
                    Respuesta="D"
            else:
                Respuesta="I"
        if(any([Respuesta=="D",Respuesta=="I"])):
            if(Respuesta=="D"):
                matrix[x-1][y+1]="O"
                matrix[x][y]=" "
                printMatrix(matrix)
            else:
                matrix[x-1][y-1]="O"
                matrix[x][y]=" " 
                printMatrix(matrix)
        elif(any([cutDerecha,cutIzquierda])):
            if(cutIzquierda):
                if (cutDerecha):
                    Respuesta=input("moviemiento derecha o izquierda?respuesta con D o I: ")
                    Respuesta=Respuesta.upper()
                else:
                    Respuesta="D"
            else:
                Respuesta="I"
        elif(any([Respuesta=="D",Respuesta=="I"])):
            if(Respuesta=="D"):
                matrix[x+1][y+1]=" "
                matrix[x+2][y+2]="X"
                matrix[x][y]=" "
                printMatrix(matrix)
            else:
                matrix[x+1][y-1]=" "
                matrix[x+2][y-2]="X"
                matrix[x][y]=" "
                printMatrix(matrix)
            if(not y>5 and not y <2):
                if(str(matrix[x-1][y+1])=="O"and not str(matrix[x-2][y+2])=="O" and not str(matrix[x+2][y+2])=="X"):
                    cutDerecha=True
                if(str(matrix[x-1][y-1])=="O"and not str(matrix[x-2][y-2])=="O" and not str(matrix[x+2][y-2])=="X"):
                    cutIzquierda=True
            elif(y>5):
                if(str(matrix[x+1][y-1])=="O"and not str(matrix[x-2][y+2])=="O" and not str(matrix[x+2][y-2])=="X"):
                    cutIzquierda=True
            else:
                 if(str(matrix[x+1][y+1])=="O"and not str(matrix[x+2][y+2])=="O" and not str(matrix[x+2][y+2])=="X"):
                    cutDerecha=True
        else:
                print("Movimiento Invalido!!Intente de nuevo.....")
                movimientoO()
    else:
            print("No es corecto")
            movimientoO()
while True:
            movimientoX()
            movimientoO()