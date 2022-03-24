from tkinter import *

largeur = 400
hauteur = 200


root = Tk()
canvas = Canvas(root,width=largeur,height=hauteur,background="white")
canvas.pack(fill="both" ,expand=True)

#les coordonnees et le vitesse
x0,y0 =100,100
dx =+10  #vitesse horizontale 
dy =+10 #vitesse verticale 

#le carre a deplacer
carre = canvas.create_rectangle(x0,y0,x0+20,y0+20,width=2,fill="blue")
#carre1 = canvas.create_rectangle(x1,y1,x1+20,y1+20,width=2,fill="blue")

#fonction principale 
def deplacer():
    global x0,y0,dx,dy
    
    x0 = x0 + dx #Nouvelle abscisse
    y0 = y0 + dy #Nouvelle ordonnee
    
    canvas.coords(carre,x0,y0,x0+20,y0+20) #Deplacement
    
    if x0 < 0 or x0 > larguer:
        dx = -dx #changement du sens horizontale 
    if y0 < 0 or y0 >hauteur:
        dy = -dy #changement du sens verticale
    canvas.after(50,deplacer)  #appele apres 50 millesecondes
    
    return
#fonction pour le boutton
def action_deplacer():
    deplacer()
    return

#boutton
button_deplacer = Button(root,text="Deplacer",width = 20, command = action_deplacer )
button_deplacer.pack(pady=10)


button_quitter = Button(root ,text="Quitter " ,width = 20, command = root.quit)
button_quitter.pack(side=BOTTOM ,pady=10)

root.mainloop()

