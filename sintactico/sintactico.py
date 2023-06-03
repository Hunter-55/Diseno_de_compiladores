import os
from tabulate import tabulate
from lexico import LEXICO

class Methods:
    # LISTAS CONSTATES GLOBALES
    global symbols_success,descrip_success,symbolsSyntactic,terminalNO,getProductions
    symbols_success = [200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,500]
    descrip_success = ['IDENTIFICADOR','IGUAL','DOBLE IGUAL','CORCHETE ABIERTO CUADRADO','CORCHETE CERRADO CUADRADO','DOBLE PUNTOS','PARENTESIS ABIERTO','PARENTESIS CERRADO','LLAVE ABIERTA','LLAVE CERRADA','COMA','SIMBOLO MAS','SIMBOLO MENOS','SIMBOLOS MULTIPLICAR','COMENTARIOS','COMENTARIOS','DIVISIÓN','MENOR QUE','MENOR IGUAL QUE','MAYOR QUE','MAYOR IGUAL QUE','DIFERENTE QUE','TEXTO','NUMERO ENTEROS','NUMERO CON NOTACION CIENTIFICA','NUMERO DECIMALES','PUNTO','ESPACIO']
    # LISTA DE LA TABLA SINTACTICA MATRIX
    symbolsSyntactic = ['=','[',']',':','(',')','{','}',',','+','-','*','/','<','>','<=','>=','==','!=','“',"'",'.','DEF','MAIN','RETURN','WHILE','DO','CYCLE','REPEAT','CONDICTION','IF','ELSEIF','ELSE','FOR','PRINT','LEN','INT','FLOAT','INPUT','ABS','STR','POW','ROUND','FLOAT','SUM','MIN','MAX','RANGE','OR','AND','NOT','IN','IDENTIFICADOR','TEXTO','NUMERO','EOF']
    #NO terminales de la tabla sintactica de la matrix
    terminalNO = ['PROGRAMA','FUNCIONES','VARIABLES','LIST','LISTAELEMENTOS','LISTANUMEROS','LISTANUMEROSPRIMA','LISTATEXTOS','LISTATEXTOSPRIMA','FUNCION','MAIN','NOMBREFUNCION','PARAMETROS','LISTAPARAMETROS','LISTAPARAMETROSPRIMA','RETURN','LISTARETURN','LISTARETURNPRIMA','BLOQUE','ESTATUTOS','ESTATUTO','FUNCION_BUILT_IN','VARIABLESIMPRIMIR','VARIABLESPRIMA','ELSEIF','ELSE','RANGO','VALOR1','VALOR2','VALOR3','BOOLEXP','BOOLEXP_PRIMA','BOOLTERM','BOOLTERM_PRIMA','BOOLFACTOR','RELTERMP','RELTERM','EXPARITM','EXPPRIMA','TERMINO','TERMPRIMO','FACTOR','OPERADOR']    

    getProductions =[
        [200,'FUNCIONES','VARIABLES'], # 1
        ['FUNCIONES','FUNCION'], # 2
        [], # 3
        ['LIST',201,200], # 4
        [], # 5
        [204,'LISTAELEMENTOS',203],# 6
        ['EXPARITM'], # 7
        [222],# 8
        ['LISTANUMEROS'], # 9
        ['LISTATEXTOS'],# 10
        ['LISTANUMEROSPRIMA',225,224,223],#....LISTA DE NUMEROS..[[223,224,225]] # 11
        ['LISTANUMEROS'],# 12
        [],# 13
        ['LISTATEXTOSPRIMA',222],# 14
        ['LISTATEXTOS'],# 15
        [],# 16
        ['RETURN','BLOQUE',205,'PARAMETROS','NOMBREFUNCION',200],# 17
        ['BLOQUE',205,200],#............................. # 18
        [200],# 19
        [207,'LISTAPARAMETROS',206],# 20
        ['LISTAPARAMETROSPRIMA',200],# 21
        [],# 22
        ['LISTAPARAMETROS'],# 23
        [],# 24
        ['LISTARETURN',200],# 25
        ['LISTARETURNPRIMA',200],# 26
        ['LISTARETURN'],# 27
        [],# 28
        [209,'ESTATUTOS',208],# 29
        ['ESTATUTOS','ESTATUTO'],# 30
        ['FUNCION',201,200],# 31
        ['BLOQUE',205,'BOOLEXP',200],# 32
        ['BOOLEXP',200,'BLOQUE',205,200],# 33
        ['BOOLEXP',200,'BLOQUE',205,200],#.............................200 : 34
        ['ELSE','ELSEIF','BLOQUE',205,'BOOLEXP',200],# 35
        ['BLOQUE',205,'RANGO',200,200,200],# 36
        [207,'VARIABLESIMPRIMIR',206,200],# 37
        ['FUNCION_BUILT_IN'],# 38
        [207,'LISTAPARAMETROS',206,'NOMBREFUNCION'],# 39
        [207,200,206,200],# 40
        [207,200,206,200],
        [207,200,206,200],
        [207,200,206,200],
        [207,'EXPARITM',206,200],
        [207,'EXPARITM',206,200],# 45
        [207,'EXPARITM',206,200],
        [207,'EXPARITM',206,200],
        [207,'EXPARITM',206,200],
        [207,200,206,200],
        [207,200,206,200],# 50
        [207,200,206,200],
        ['VARIABLESPRIMA',200],
        ['VARIABLESPRIMA',222],#........................... : 53
        ['VARIABLESIMPRIMIR',210],
        [],# 55
        ['ELSEIF','BLOQUE',205,'BOOLEXP',200],
        [],
        [],
        ['BLOQUE',205,200],
        [207,'VALOR1',206,200],# 60
        ['VALOR2','EXPARITM'],
        [],
        ['VALOR3','EXPARITM',210],
        [],
        ['EXPARITM',210],# 65
        ['BOOLEXP_PRIMA','BOOLTERM'],
        ['BOOLEXP_PRIMA','BOOLTERM',200],
        [],
        ['BOOLTERM_PRIMA','BOOLFACTOR'],
        ['BOOLTERM_PRIMA','BOOLFACTOR',200],# 70
        [],
        ['BOOLFACTOR',200],#-------- : 72
        [207,'RELTERMP','RELTERM',206],#......................
        ['RELTERMP','RELTERM'],
        ['RELTERM','OPERADOR'],# 75
        [],
        ['EXPARITM'],
        ['EXPPRIMA','TERMINO'],
        ['EXPPRIMA','TERMINO',211],
        ['EXPPRIMA','TERMINO',112],# 80
        [],
        ['TERMPRIMO','FACTOR'],
        ['TERMPRIMO','FACTOR',213],
        ['TERMPRIMO','FACTOR',216],
        [],# 85
        [200],
        [225,224,223],#..........LISTA DE NUMEROS............[[223,224,225]]
        [217],
        [219],
        [218],# 90
        [220],
        [202],
        [221],
        [],
        []# 95
    ]

    # SE OBTIENE LA COLUMNA DE LA TABLA SINTACTICA MATRIX
    def EquivalentColumn(self,tokenPosition0):
        nameAxu = ""
        if isinstance(tokenPosition0,list):
            # VALIDA LOS ESTADOS DE EXITO
            if tokenPosition0[1] in symbols_success:
                for i in range(len(symbolsSyntactic)):
                    if tokenPosition0[0].lower() == symbolsSyntactic[i].lower():
                        return i
                if tokenPosition0[2] == 'IDENTIFICADOR':
                    return 52
                elif tokenPosition0[2] == 'TEXTO':
                    return 53
                elif tokenPosition0[2].find('NUMERO') != -1:
                    return 54
            else:
                return 404
        else:
            # VALIDA LOS ESTADOS DE EXITO descrip_success 
            """if tokenPosition0 in terminalNO:
                for i in range(len(terminalNO)):
                    if tokenPosition0 == terminalNO[i]:
                        nameAxu = descrip_success[i]
                        break
                
                for i in range(len(symbolsSyntactic)):
                    if nameAxu.lower().find(symbolsSyntactic[i].lower()) != -1:
                        return i
                
                for i in range(len(descrip_success)):
                    if nameAxu.lower().find(descrip_success[i].lower()) != -1:
                        return i
                print("ajajjaja ",nameAxu)"""

            if tokenPosition0 in symbols_success:
                for i in range(len(symbols_success)):
                    if tokenPosition0 == symbols_success[i]:
                        nameAxu = descrip_success[i]
                        break

                for i in range(len(symbolsSyntactic)):
                    if nameAxu.lower().find(symbolsSyntactic[i].lower()) != -1:
                        return i
                
                for i in range(len(descrip_success)):
                    if nameAxu.lower().find(descrip_success[i].lower()) != -1:
                        return i
            else:
                return 404

# SE OBTIENEN LAS FILAS DE LA TABLA SINTACTICA MATRIX
    def EquivalentRow(self,syntacticStackPosition):
        if syntacticStackPosition in terminalNO:
            for i in range(len(terminalNO)):
                if syntacticStackPosition == terminalNO[i]:
                    return i
        else:
            return 404

# REGRESA EL SIMBOLO DE LA LISTA SEGÚN LA POSICIÓN   
    def ColumnEquivalentTerminalSymbol(self,position):
        return symbolsSyntactic[position].lower()

# OBTENEMOS LA PRODUCCIONES O NT PARA OBTENER LAS DE MAS PRODUCCIONES
    def GetProduction(self,productionNumber, syntacticStack):
        production = productionNumber - 1

        if production <= len(getProductions):
            syntacticStack.extend(getProductions[production])
            return syntacticStack
        else:
            syntacticStack.extend([404])
            return syntacticStack

# OBTENER LOS SIMBOLOS QUE SE ESPERAN
    def TokenExpected(self,row,syntacticMatrix):
        columnas        = []
        tokensesperados = []
        contador        = 0
        
        for token in syntacticMatrix[row]:
            if token != 404:
                columnas.append(contador)
            contador+=1
            
        for col in columnas:
            simboloterminal = Methods().ColumnEquivalentTerminalSymbol(col)
            tokensesperados.append(simboloterminal)
            
        return tokensesperados


class Syntatic:
    global syntacticMatrix, error
    error           = 404
    syntacticMatrix = [
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,1,error,error,1],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,2,3,error,error,error,error,error,error,error,error,error,error,error,2,2,2,2,2,2,2,2,2,2,2,2,error,error,error,error,error,2,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,5,5,error,error,error,error,error,error,error,error,error,error,error,5,5,5,5,5,5,5,5,5,5,5,5,error,error,error,error,error,4,error,error,error],
        [error,6,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,7,8,7,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,10,9,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,11,error],
        [error,error,13,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,12,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,14,error,error],
        [error,error,16,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,15,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,17,error,error,error,error,error,error,error,error,error,error,error,error,38,38,38,38,38,38,38,38,38,38,38,38,error,error,error,error,error,39,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,18,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,19,error,error,error],
        [error,error,error,error,20,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,22,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,21,error,error,error],
        [error,error,error,error,error,24,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,23,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,25,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,26,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,28,28,error,28,28,error,28,error,28,error,error,28,28,28,28,28,28,28,28,28,28,28,28,28,28,error,error,error,error,error,27,error,error,error],
        [error,error,error,error,error,error,29,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,error,error,94,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,30,30,error,30,error,30,error,error,30,30,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,30,error,error,error],
        [error,error,error,error,error,error,error,95,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,32,33,error,34,error,35,error,error,36,37,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,31,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,40,41,42,43,44,45,46,47,42,49,50,51,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,52,53,error,error],
        [error,error,error,error,error,55,error,error,54,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,error,error,57,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,57,57,error,57,error,57,56,57,57,57,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,57,error,error,error],
        [error,error,error,error,error,error,error,58,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,58,58,error,58,error,58,error,59,58,58,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,58,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,60,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,61,error,61,error],
        [error,error,error,error,error,62,error,error,63,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,error,64,error,error,65,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error],
        [error,error,error,error,66,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,66,error,66,error,66,error],
        [error,error,error,68,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,68,68,error,68,error,68,error,error,68,68,error,error,error,error,error,error,error,error,error,error,error,error,error,67,error,error,error,68,error,error,error],
        [error,error,error,error,69,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,69,error,69,error,69,error],
        [error,error,error,71,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,71,71,error,71,error,71,error,error,71,71,error,error,error,error,error,error,error,error,error,error,error,error,error,71,70,error,error,71,error,error,error],
        [error,error,error,error,73,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,72,error,74,error,74,error],
        [error,error,error,76,error,76,error,error,error,error,error,error,error,75,75,75,75,75,75,error,error,error,error,error,error,76,76,error,76,error,76,error,error,76,76,error,error,error,error,error,error,error,error,error,error,error,error,error,76,76,error,error,76,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,77,error,77,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,78,error,78,error],
        [error,error,error,81,error,81,error,error,81,79,80,error,error,81,81,81,81,81,81,error,error,error,81,81,81,81,error,81,error,81,error,error,81,81,81,81,81,81,81,81,81,81,81,81,81,81,error,81,81,error,error,81,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,82,error,82,error],
        [error,error,error,85,error,85,error,error,85,85,85,83,84,85,85,85,85,85,85,error,error,error,85,85,85,85,error,85,error,85,error,error,85,85,85,85,85,85,85,85,85,85,85,85,85,85,error,85,85,error,error,85,error,error,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,86,error,87,error],
        [error,error,error,error,error,error,error,error,error,error,error,error,error,88,89,90,91,92,93,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error,error]
        ]

    def SyntacticAnalysis(self,token):
        # inicializamos la pila del programa con PROGRAMA 
        syntacticStack = [500,'PROGRAMA']#-----------------CHECAR
        objMethods     = Methods()
        while len(token) > 0:
            print(syntacticStack)
            print(token[0])
            if syntacticStack[-1] == token[0][1]:
                #se elimina el ultimo elemento en el stack sintactico
                syntacticStack.pop()
                #se elimina el primer elemento en la tabla de tokens
                token.pop(0)
            else:
                # SE OBTIENE LA COLUMNA Y LA FILA
                column = objMethods.EquivalentColumn(token[0])
                row    = objMethods.EquivalentRow(syntacticStack[-1])
                
                # SE VALIDA QUE EL SIMBOLO TERMINAL SE ENCUENTRE
                if row == error or column == error:
                    terminalSymbolColumn = objMethods.EquivalentColumn(syntacticStack[-1])
                    expectedToken        = objMethods.ColumnEquivalentTerminalSymbol(terminalSymbolColumn)
                    print(f"SE ENCONTRO UN ERROR, SE ESPERA: ' {expectedToken} '")
                    #print(f"Nota: si alguno de los tokens de simbolos terminales es de 200 a 203 el error es de lexico.")
                    break

                # OBTENER LA PRODUCCIÓN CON LA FILA Y COLUMNA EN LA MATRIZ SINTACTICA
                productionNumber = syntacticMatrix[row][column]
                #print(productionNumber)
                #print(row,"  ---  ",column,"  ---  ",productionNumber)
                #print(symbolsSyntactic)
                #print(f"Producción que va a incluirse: {productionNumber}")
                syntacticStack.pop()
                #se añade la producción.
                syntacticStack = objMethods.GetProduction(productionNumber, syntacticStack)
                #print(symbolsSyntactic)

                # SI SE ENCUENTRA UN ERROR DE SINTAXTICO
                if syntacticStack[-1] == 404:
                    tokensesperados = objMethods.TokenExpected(row,syntacticMatrix)
                    print(f"ERROR SINTACTICO, SE ESPERABA ALGUNO TOKENS TERMINALES: {tokensesperados}")
                    #print(f"Nota: si alguno de los tokens de simbolos terminales es de 200 a 203 el error es de lexico.")
                    break
        
        #Si la tabla de token fue vaciada se informa que no hubo errores sintacticos.
        if len(token) == 0:
            print("¡¡¡¡ EL PROGRAMA COMPILÓ CORRECTAMENTE !!!.")


def main():
    name  = input("Nombre del programa: ")
    token = []

    if os.path.isfile(name):
        lexico      = LEXICO(name)
        source_code = lexico.OpenFile()
        token       = lexico.LexicoAnalysis(source_code)
        #print(tabulate(token, headers=['SIMBOLO', 'ESTADO','DESCRIPCION']))
        syntatic = Syntatic()
        syntatic.SyntacticAnalysis(token)
    else:
        print(f'EL ARCHIVO "{name}" NO EXISTE')


if __name__ == '__main__':
    main()