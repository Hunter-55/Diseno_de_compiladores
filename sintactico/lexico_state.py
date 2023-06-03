import re
from colorama import Fore, Back, Style

class STATES:

##### MÉTODO CONSTRUCTOR #####
    def __init__(self,character,previous_state) -> None:
        self.character      = character
        self.previous_state = previous_state

##### MÉTODO PARA OBTENER LA COLUMNA #####
    def GetColumn(self):
        auxs    = ["'",'"']
        symbols = ['[a-zA-Z]','[0-9]','e','=','[',']',':','(',')','{','}',',','+','-','*','/','<','>','!',auxs,'.',' ']
        
        for column in range(len(symbols)):
            # DETECTA LETRAS O NÚMEROS
            if symbols[column] == '[a-zA-Z]' or symbols[column] =='[0-9]':
                if self.character == 'e' and self.previous_state == 10: # antes era 1 de columna
                    return 2
                elif self.character == 'e' and self.previous_state == 15:# antes era 20 de columna
                    return 2
                else:
                    if re.search(symbols[column],self.character) and self.previous_state == 9:
                        return column
                    elif re.search(symbols[column],self.character):
                        self.comilla = 0
                        return column
            # DETECTA LAS COMILLAS ' O "
            elif isinstance(symbols[column],list):
                if self.character in auxs:
                    return column
            # DETECTA SIMBOLOS
            if self.character == symbols[column]:
                return column
        # DETECTO SIMBOLO NO ACEPTADO
        else:
            return 22

##### MÉTODO PARA DETECTAR ESTADOS POR CARACTERES #####
    def StatesOfMatrix(self,state,counter,save_character,save_char):
        object_states  = {}
        state_aux      = 0 
        save_character = save_character.replace('\n','')# ELIMINA LOS SALTOS DE LINEA

        # LISTA DE CÓDIGOS DE ERROR
        symbols_error   = [300,301,302,303,304,305,306]# ESTADOS FINALES (*)
        descrip_error   = ['ERROR DE COMENTARIO FALTA * ó /','ERROR DE SÍMBOLO DIFERENTE','ERROR DE TEXTO NO CIERRA COMILLA','ERROR NOTACIÓN CIENTIFICA','ERROR SÍMBOLO INCORRECTO','ERROR EN NUMERO','ERROR SIMBOLO NO ACEPTADO']
        
        # LISTA DE CÓDIGO DE ÉXITO
        symbols_success = [200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227]
        descrip_success = ['IDENTIFICADOR','IGUAL','DOBLE IGUAL','CORCHETE ABIERTO CUADRADO','CORCHETE CERRADO CUADRADO','DOBLE PUNTOS','PARENTESIS ABIERTO','PARENTESIS CERRADO','LLAVE ABIERTA','LLAVE CERRADA','COMA','SIMBOLO MAS','SIMBOLO MENOS','SIMBOLOS MULTIPLICAR','COMENTARIOS','COMENTARIOS','DIVISIÓN','MENOR QUE','MENOR IGUAL QUE','MAYOR QUE','MAYOR IGUAL QUE','DIFERENTE QUE','TEXTO','NUMERO ENTEROS','NUMERO CON NOTACION CIENTIFICA','NUMERO DECIMALES','PUNTO','ESPACIO']
        finish_success  = [200,201,214,216,217,219,223,224,225]# ESTADOS FINALES (*)

        # LISTA DE PALABRAS RESERVADAS
        reserved = ['def','main','return','while','do','cycle','repeat','condiction','if','elseif','else','for','print','len','int','float','input','abs','str','pow','round','float','sum','min','max','range','or','and','not','in']

        # VALIDA LOS ESTADOS DE ERROR
        if state in symbols_error:
            for i in range(len(symbols_error)):
                if state == symbols_error[len(symbols_error)-1]:
                    state_aux        = state
                    state            = 0
                    cadenaencontrada = save_character.strip()# esta linea quita los espacios y saltos de linea a la izquierda y derecha de lo encontrado.
                    if save_character != '':
                        save_char.append([cadenaencontrada,state_aux,descrip_error[len(symbols_error)-1]])# TOKEN
                        #print(f"{descrip_error[len(symbols_error)-1]}: {cadenaencontrada}")
                else:  
                    if state == symbols_error[i]:
                        counter          -= 1
                        state_aux        = state
                        state            = 0
                        cadenaencontrada = save_character.strip()# esta linea quita los espacios y saltos de linea a la izquierda y derecha de lo encontrado.
                        save_char.append([cadenaencontrada,state_aux,descrip_error[i]])# TOKEN
                        #print(f"{descrip_error[i]}: {cadenaencontrada}")
            save_character = ""

        # VALIDA LOS ESTADOS DE EXITO
        if state in symbols_success:
            for i in range(len(symbols_success)):
                if state == symbols_success[i]:
                    if state in finish_success:
                        counter -= 1
                    state_aux        = state
                    state            = 0
                    cadenaencontrada = save_character.strip()# esta linea quita los espacios y saltos de linea a la izquierda y derecha de lo encontrado.

                    # VERIFICA QUE EL ESTADO SEA UNA PALABRA RESERVADA O UNA VARIABLE
                    if state == symbols_success[0]:
                        for i in range(len(reserved)):
                            if cadenaencontrada == reserved[i]:
                                save_char.append([cadenaencontrada,state_aux,'PALABRA RESERVADA'])# TOKEN
                                #print(f"PALABRA RESERVADA: {cadenaencontrada}")
                            else:
                                save_char.append([cadenaencontrada,state_aux,descrip_success[i]])# TOKEN
                                #print(f"{descrip_success[i]}: {cadenaencontrada}")
                    else:
                        #print(cadenaencontrada," - ",state_aux," - ",descrip_success[i])
                        if state_aux != 227:
                            save_char.append([cadenaencontrada,state_aux,descrip_success[i]])# TOKEN
                        #print(f"{descrip_success[i]}: {cadenaencontrada}")
            save_character = ""

        self.previous_state = state # SE PASA EL ESTADO COMO ESTADO ANTERIOR
        counter             += 1    # SE INCREMENTA EL CONTADOR

        object_states = {
            'states'         : state,
            'counter'        : counter,
            'previous_state' : self.previous_state,
            'save_character' : save_character,
            'save_char'      : save_char        
        }

        return object_states



