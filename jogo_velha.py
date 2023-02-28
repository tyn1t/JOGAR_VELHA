import random
matriz = [[0,0,0],
           [0,0,0],
           [0,0,0]]
def verifica_int(mensagem, ini, fim):
    while True:
       try:
          valor = int(input(mensagem))
          if valor >= ini and valor <= fim:
             return valor
       except ValueError:
          print("Error digite valor ") 
       except IndexError:
          print(f"Digite valor entre {ini} e {fim}")      
          
 
def menu():
   print('''
         JOGAR:   [1]
         EXEMPLO: [2]
         
         SAIR:    [0]
         ''') 
   return verifica_int("EScolhar uma opção: ",0,2)

def imprima():
    print('-'*50,'JOGO DA VELHA','-'*50)
    print(f"""
                                                       {matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}
                                                       -+-+-
                                                       {matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}
                                                       -+-+-
                                                       {matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}
                                                              
""", end="")

def Ex():
   print(f'''
    [linha:1,2,3 ]  = L                                   
    [coluna:1,2,3]  = C 
    
      Ex:                                 
           C 1   2   3      
         L                             
         1  ___|___|___      ___|___|___                            
         2  ___|___|___   =  ___|___|___                             
         3  3,1|   |3,3       X |   | O        
''')

def rest():
    for x in range(3):
        for y in range(3):
            matriz[x][y] = 0
    return matriz

 
def   ganha():
      jogador = 0
      
      for x in range(3):
         # para confimar as linha
         if matriz[x][0] == 'X' and matriz[x][1] == 'X' and matriz[x][2] == 'X':
            jogador = 3
         elif matriz[x][0] == 'O' and matriz[x][1] == 'O' and matriz[x][2] == 'O':
            jogador -= 3
         for y in range(3):
            # PARA CONFIMAR AS COLUNAS 
            if matriz[0][y] == 'X' and matriz[1][y] == 'X' and matriz[2][y] == 'X':
               jogador = 3
            elif matriz[0][y] == 'O' and matriz[1][y] == 'O' and matriz[2][y] == 'O':
               jogador -= 3
         # CONFIMAR DIAGONAL 
         if ((matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X') or 
         (matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X')):
               jogador = 3
         elif ((matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O') or 
                (matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O')):
               jogador -= 3
               
         
          
         if jogador ==  3  or jogador == -3:
            return jogador
            
      
         

      #if V == 9:
      #   return V

def main():    
    XO = 'XO'        
    jogar = random.sample(XO,1)
    troca = False
    Inicia = 0
    while True:
        
        imprima()
        # Troca jogador 
        if troca:
         if jogar[0] == 'X':
               jogar = 'O' 
         elif jogar[0] == 'O':
               jogar = 'X'
               
         print(f'Jogador: {jogar[0]} ')
        elif troca == False:
           if Inicia == 0:
              print(f'JOGADOR [{jogar[0]}]')   
           elif Inicia == 1:
              print(f'JOGADOR [{jogar[0]}] Não jogou por favor jogue')  
        
        # Jogador Escolhe as posição 
        try:   
            linha  = int(input('Linha: ',end=" "))
            coluna = int(input('Coluna: ',end=" "))
            if matriz[linha-1][coluna-1] == 0:
               matriz[linha-1][coluna-1] = jogar[0]
               troca = True
               Inicia = 1
        except ValueError:
            print(f"Digitou Errado Valor")
            troca = False
        except IndexError:
            print(f"Digitou Errado Valor da posição")
            troca = False
            
        #MOSTRA O GANHADOR DA PARTIDA
        g = ganha()
        
        if g == 3:
           print('JOGADOR X GANHO PARABÉNS')
           break
      
        elif g == -3:
           print('JOGADOR O GANHO PARABÉNS')
           break
        
        elif g == 9:
           print('VELHA ')
           break
          
         
if __name__ == '__main__':
   while True:
      opecao = menu()
      if opecao == 0:
         break
      elif opecao == 1:
         rest()
         main()
      elif opecao == 2:
         Ex()
  