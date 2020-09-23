from random import randrange, choice

def gen_mazo(ma,n): # Genera el Mazo a partir de Dos parametros un contador y una lista con un grupo de cartas
    if n==1:
        return choice(ma)
    else:
        return gen_mazo(ma + ma,n-1)

def cal_t(cards,t,c,t_u): #Calcula el valor total de las cartas que trae la lista
    if c==-2:
        return cal_t(cards,t,len(cards),t_u)
    elif c>0:
        if type(cards[c-1])==int:
            return cal_t(cards,t+cards[c-1],c-1,t_u)
        elif type(cards[c-1])==str:
            if cards[c-1]=="A" and t_u==1:
                print("Que valor desea que tome el A, 1 o 11")
                return cal_t(cards,t+int(input()),c-1,t_u)
            elif cards[c-1]=="J" or cards[c-1]=="K" or cards[c-1]=="Q":
                return cal_t(cards,t+10,c-1,t_u)
            elif cards[c-1]=="A" and t_u==2:
                if t<=10:
                    return cal_t(cards,t+11,c-1,t_u)
                else:
                    return cal_t(cards,t+1,c-1,t_u)
    elif c==0:
        return t

def d_card(g,cu,t_c): # Escoge una carta y la agrega a las cartas del usuario o del Crupier   
    
    if t_c==1:
        print("Sus Cartas son : ",cu)
    else:
        print("Las cartas de la Mesa son : ",cu)
    
    if g!=0:
      return d_card(g-1, cu + [gen_mazo(["A",2,3,4,5,6,7,8,9,10,"K","J","Q"],3)],t_c)
    elif g==0 and (cal_t(cu,0,-2,t_c))<21:
     
      if t_c==2:
          return d_card(0, cu + [gen_mazo(["A",2,3,4,5,6,7,8,9,10,"K","J","Q"],3)],t_c)

      elif input("Si desea tomar otra carta digite 1 si desea plantar digite 0")=="1":
          return d_card(0, cu + [gen_mazo(["A",2,3,4,5,6,7,8,9,10,"K","J","Q"],3)],t_c)
      else:
           if t_c==1:
              print("Sus Cartas son : ",cu)
              return cu
           else:
             print("Las cartas de la Mesa son : ",cu)
             return cu
    else:
        if t_c==1:
          print("Sus Cartas son : ",cu)
          return cu
        else:
          print("Las cartas de la Mesa son : ",cu)
          return cu
       
def evaluar(cartas_u,cartas_c):# Evalua las cartas de cada uno y entrega un veredicto Ganaste o Perdiste 

    if cal_t(cartas_c,0,-2,2)<21 and cal_t(cartas_c,0,-2,2)<cal_t(cartas_u,0,-2,1):
        d_card(0,cartas_c,2)
    elif cal_t(cartas_c,0,-2,2) > cal_t(cartas_u,0,-2,1) and cal_t(cartas_c,0,-2,2)<=21:
        return "Perdiste"
    elif cal_t(cartas_u,0,-2,1)>21:
        return "Perdiste"
    else:
        return "Ganaste"

print(evaluar(d_card(2,[],1),d_card(2,[],2)))
