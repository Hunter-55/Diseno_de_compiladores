from lexico_state import STATES
from tabulate import tabulate
import os

class LEXICO:
    global states_matrix
    states_matrix = [
        [1,10,304,2,203,204,205,206,207,208,209,210,211,212,213,3,6,7,8,9,226,227,306],
        [1,1,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200],
        [201,201,201,202,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201],
        [216,216,216,216,216,216,216,216,216,216,216,216,216,216,4,4,216,216,216,216,216,216,216],
        [4,4,214,214,214,214,214,214,214,214,214,214,214,214,5,214,214,214,214,214,214,4,214],
        [300,300,300,300,300,300,300,300,300,300,300,300,300,300,300,215,300,300,300,300,300,300,300],
        [217,217,217,218,217,217,217,217,217,217,217,217,217,217,217,217,217,217,217,217,217,217,217],
        [219,219,219,220,219,219,219,219,219,219,219,219,219,219,219,219,219,219,219,219,219,219,219],
        [301,301,301,221,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],
        [9,9,302,302,302,302,302,302,302,302,302,302,302,302,302,302,302,302,302,222,302,9,302],
        [223,10,11,223,223,223,223,223,223,223,223,223,223,223,223,223,223,223,223,223,14,223,223],
        [303,303,303,303,303,303,303,303,303,303,303,303,12,12,303,303,303,303,303,303,303,303,303],
        [305,13,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305],
        [224,13,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224,224],
        [305,15,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305,305],
        [225,15,11,225,225,225,225,225,225,225,225,225,225,225,225,225,225,225,225,225,225,225,225],
    ]

##### MÉTODO CONSTRUCTOR #####
    def __init__(self,files) -> None:
        self.files         = files

##### MÉTODO PARA LEER Y GUARDAR ARCHIVO EN UN STRING #####
    def OpenFile(self):
        file         = open(self.files,'r')
        sources_code = file.read()
        file.close()
        return sources_code
    
##### MÉTODO PARA ANALIZAR EL CÓDIGO FUENTE #####
    def LexicoAnalysis(self,source_code):
        state          = 0                # ESTADOS OBTENIDOS
        counter        = 0                # APUNTADOR DE CARACTERES
        save_char      = []               # GUARDA EN UNA LISTA LOS CARACTERES OBTENIDOS
        source_code    += "\n"            # SE AGREGA UN SALTO DE LINEA PARA MARCAR FIN DE LECTURA DEL ARCHIVO
        size_code      = len(source_code) # TAMAÑO DEL CÓDIGO FUENTE
        previous_state = 0                # SE GUARDA EL ESTADO ANTERIOR
        save_character = ''               # GUARDA EN UN STRING LA RECOPILACIÓN DE CARACTERES

        while counter < size_code:
            character      = source_code[counter]              # OBTENEMOS EL CARACTER POR LA POSICIÓN
            methods_state  = STATES(character,previous_state)  # INSTANCIA DE STATES
            column         = methods_state.GetColumn()         # OBTENEMOS LA COLUMNA
            save_character += character                        # GUARDA LOS CARACTERES COMO TEXTO
            state          = states_matrix[state][column] # CON EL ESTADO Y LA COLUMNA OBTENEMOS EL ESTADO DE LA MATRIZ
            #save_char.append(character)
            # SE CHECA LOS ESTADOS DE LA MATRIZ
            object_state   = methods_state.StatesOfMatrix(state,counter,save_character,save_char)
            state          = object_state['states']         # SE OBTIENE EL ESTADO
            counter        = object_state['counter']        # SE OBTIENE EL INCREMENTO DEL CONTADOR
            previous_state = object_state['previous_state'] # SE OBTIENE EL ESTADO ANTERIOR
            save_character = object_state['save_character'] # SE OBTIENE LA CADENA ENCONTRADAS
            save_char      = object_state['save_char'] # GUARDA LOS TOKENS ENCONTRADOS
        return save_char


###### Función main para instanciar la clase del lexico #####
def main():
    name = input("Nombre del programa: ")

    if os.path.isfile(name):
        lexico      = LEXICO(name)
        source_code = lexico.OpenFile()
        token       = lexico.LexicoAnalysis(source_code)
        print(tabulate(token, headers=['SIMBOLO', 'ESTADO','DESCRIPCION']))
    else:
        print(f'EL ARCHIVO "{name}" NO EXISTE')

if __name__ == '__main__':
    main()


