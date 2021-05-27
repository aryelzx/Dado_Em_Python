#simulador de dado de 1 a 6
#sem interface (incompleto)
import random 
import PySimpleGUI as sg
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
        
    def Iniciar(self):
        #criar a janela 
        self.janela = sg.Window('simulador de dado',layout=self.layout)
        #ler eventos
        self.eventos, self.valores = self.janela.Read()
        #fazer algo com os valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos sua participação!!!')
            else:
                print('favor digitar sim,s,não ou n')    
        except:
            print('Ocorreu um erro durante sua operação!')
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar() 
        