import decode as d
import coding as c
import tkinter as t
import os, sys, stat
from random import randint
global window
window=t.Tk(className="Hibiscus")


def delete_item():
    for i in window.winfo_children():
        if i.winfo_name()!='menu':
            i.destroy()

def generate(n):
    """
    Generate the first number under 100
    """
    res=[2]
    for i in range(3,n):
        bool=True
        for j in res:
            if i%j==0:
                bool=False
                break
        if bool:
            res.append(i)
            
    return res

def motdepasse(n,l):
    """
    Créé un mot de passe de longueur n
    """
    res=''
    while n>0:
        tmp=chr(randint(33,126))
        if not tmp in l:
            res+=tmp
            n-=1
    return res

def obtenir(dyn):
    """
    permet d'obtenir une ou pls ligne
    """
    delete_item()
    dyn=t.Canvas(window)
    dyn.grid(column=0,row=0)
    txt=t.Label(dyn,text="Code PIN")
    PIN=t.Entry(dyn,width=30,show='*')
    txt.grid(row=0,column=0)
    PIN.grid(row=0,column=1)
    txt=t.Label(dyn,text="Site ou logiciel")
    wfor=t.Entry(dyn,width=30)
    txt.grid(row=1,column=0)
    wfor.grid(row=1,column=1)
    txt5=t.Label(dyn,text="Nom du fichier")
    file=t.Entry(dyn,width=30)
    txt5.grid(row=2,column=0)
    file.grid(row=2,column=1)
    menu1=t.Button(dyn,padx=0, pady=0, width=25,text="Obtenir",command=lambda:after3(PIN.get(),wfor.get(),file.get(),dyn))
    menu1.grid(row=5,column=1)
    
def after3(PIN,wfor,name,dyn,delet=False):
    """
    The treatment after decode and deleter
    """
    
    try:
        PIN=int(PIN)
        PIN=key(PIN)
    except ValueError:
        erreur("Le code pin n'est pas un nombre")
    try:
        file=open("../code/"+name,'rb')
        file.close()
    except FileNotFoundError:
        try:
            file=open("../code/"+name+".txt",'rb')
            name+='.txt'
            file.close()
        except FileNotFoundError:
            erreur("Le fichier n'existe pas ou n'est pas dans le dossier code")
    a=d.decode(PIN,name,wfor)
    try:
        a.decode()
        delete_item()
    except d.decodeError:
        erreur("Le site n'existe pas sur ce fichier")
    dyn=t.Canvas(window)
    dyn.grid(column=0,row=0) 
    res=a.getres().split('\n')
    res.remove('')
    var=t.IntVar()
    for i in range(len(res)):
        rank=0
        if delet:
            w=t.Checkbutton(dyn,text=str(i+1),onvalue=i,variable=var)
            w.grid(column=rank,row=i)
            rank+=1
        tmp=final(res[i])
        txt=t.Label(dyn,text="Site ou logiciel")
        txt.grid(column=rank,row=i)
        txt=t.Label(dyn,text=tmp[0])
        txt.grid(column=rank+1,row=i)
        txt=t.Label(dyn,text="Email et/ou id")
        txt.grid(column=rank+2,row=i)
        id=t.Entry(dyn)
        id.insert(0,tmp[1])
        id.grid(column=rank+3,row=i)
        txt=t.Label(dyn,text="Mot de passe")
        txt.grid(column=rank+4,row=i)
        id=t.Entry(dyn)
        id.insert(0,tmp[2])
        id.grid(column=rank+5,row=i)
    if delet:
        b=t.Button(dyn,text="Supprimer",command=lambda:suppr(var.get(),res))
        b.grid(column=3,row=i+1)

def suppr(var,res):
    print(res[var])
    
def password(entry):
    """
    Genere un mot de passe
    """
    pop=t.Tk(className="Longueur")
    txt=t.Label(pop,text="Longueur du mot de passe")
    length=t.Entry(pop,width=5)
    txt.grid(row=0,column=0)
    length.grid(row=0,column=1)
    txt1=t.Label(pop,text='Caracteres interdits')
    warn=t.Entry(pop,width=10)
    txt1.grid(row=1,column=0)
    warn.grid(row=1,column=1)
    test=t.Button(pop,text='Generer',command=lambda:after(pop,entry,int(length.get()),set(warn.get())))
    test.grid(row=2)
    t.mainloop()

def after(f,entry,a,b):
    entry.delete(0,t.END)
    entry.insert(0,motdepasse(a,b))
    enleve(f)
    
def enleve(f):
    f.destroy()

def deleter(fenetre):
    """
    Supprime l'item choisi
    """
    delete_item()
    fenetre=t.Canvas(window)
    fenetre.grid(column=0,row=0)
    txt1=t.Label(fenetre, text="Adresse mail et/ou identifiant (facultatif)")
    txt1.grid(row=0,column=0)
    mail=t.Entry(fenetre,width=50)
    mail.grid(row=0,column=1,columnspan=2)
    code=t.Entry(fenetre,width=30)
    txt2=t.Label(fenetre,text="Mot de passe (facultatif)")
    txt2.grid(row=1,column=0)
    code.grid(row=1,column=1)
    txt3=t.Label(fenetre,text='Site ou logiciel (facultatif)')
    wfor=t.Entry(fenetre,width=30)
    txt3.grid(row=2,column=0)
    wfor.grid(row=2,column=1)
    txt4=t.Label(fenetre,text="Code PIN")
    PIN=t.Entry(fenetre,width=30,show="*")
    txt4.grid(row=3,column=0)
    PIN.grid(row=3,column=1)
    txt5=t.Label(fenetre,text="Nom du fichier")
    file=t.Entry(fenetre,width=30)
    txt5.grid(row=4,column=0)
    file.grid(row=4,column=1)
    menu1=t.Button(fenetre,padx=0, pady=0, width=25,text="Rechercher",command=lambda:after3(PIN.get(),wfor.get(),file.get(),fenetre,True))
    menu1.grid(row=5,column=2)
        
def generer(fenetre):
    """
    Créer la fenetre de génération de mot de passe
    """
    delete_item()
    fenetre=t.Canvas(window)
    fenetre.grid(column=0,row=0)
    txt1=t.Label(fenetre,text="Adresse mail et/ou identifiant")
    txt1.grid(row=0,column=0)
    mail=t.Entry(fenetre,width=50)
    mail.grid(row=0,column=1,columnspan=2)
    code=t.Entry(fenetre,width=30)
    yes=t.Button(fenetre,text="Générer un mot de passe",command=lambda:password(code))
    yes.grid(row=1,column=0)
    txt2=t.Label(fenetre,text="Mot de passe")
    txt2.grid(row=1,column=1)
    code.grid(row=1,column=2)
    txt3=t.Label(fenetre,text='Site ou logiciel')
    wfor=t.Entry(fenetre,width=30)
    txt3.grid(row=2,column=0)
    wfor.grid(row=2,column=1)
    txt4=t.Label(fenetre,text="Code PIN")
    PIN=t.Entry(fenetre,width=30,show="*")
    txt4.grid(row=3,column=0)
    PIN.grid(row=3,column=1)
    txt5=t.Label(fenetre,text="Nom du fichier")
    file=t.Entry(fenetre,width=30)
    txt5.grid(row=4,column=0)
    file.grid(row=4,column=1)
    menu1=t.Button(fenetre,padx=0, pady=0, width=25,text="Enregistrer",command=lambda:after2(PIN.get(),wfor.get(),code.get(),mail.get(),file.get(),fenetre))
    menu1.grid(row=5,column=2)

def final(line):
    """
    Treatment of the result of the class decode
    :param line:(str) the result of the class decode
    """
    CTE=['wfor:',' identity:',' password:']
    res=[line]
    for i in CTE:
        for j in range(len(res)):
            res=res[:j]+res[j].split(i)+res[j+1:]
            try:
                res.remove('')
            except ValueError:
                pass
    return res

def key(PIN):
    """
    Change the pin code
    :param PIN: (int) the pin code
    """
    cent=100
    tmp=PIN//cent
    tmp1=PIN
    tmp2=PIN
    while cent<=tmp:
        cent=cent*10
    PREMIERS=generate(cent)
    if not (tmp in PREMIERS) and tmp==1:
        return (PIN+100)
    elif not (tmp in PREMIERS) and tmp>0:
        return key(PIN-100)

    else:
        return PIN
    
def after2(PIN,wfor,code,mail,name,fenetre):
    """
    The treatment of the form's data for the generation of password
    :param PIN: (int) the pin code
    :param wfor: (str) the name of the application or site
    :param code: (str) the password
    :param mail:(str) the mail or identifiant
    :param name: (str) the name of the file
    :param fenetre: (tk.Tk) the current window
    """
    print("Traitement des données")
    bool=True
    other=True
    try:
        PIN=int(PIN)
        PIN=key(PIN)
    except ValueError:
        erreur("Le code pin n'est pas un nombre")
        bool=False
    if wfor=='':
        erreur("Le site ou logiciel n'a pas été renseigne")
        bool=False
    if code=='':
        erreur("Le mot de passe n'a pas été renseigne")
        bool=False
    if mail=='':
        erreur("Le mail et/ou identifiant n'a/ont pas été renseigne")
        bool=False
    try:
        file=open("../code/"+name,'rb')
        file.close()
    except FileNotFoundError:
        try:
            file=open("../code/"+name+".txt",'rb')
            file.close()
        except FileNotFoundError:
            other=False
    if bool:
        pop=t.Tk(className="Validation")
        if not other:
            txt2=t.Label(pop,text="Le fichier n'existe pas ou n'est pas dans le dossier code",fg='red')
            txt2.grid(row=2,column=0,columnspan=1)
        txt=t.Label(pop,text="Etes vous sur de vouloir sauvegarder?")
        txt.grid(row=0,column=0,columnspan=1)
        y=t.Button(pop,padx=0, pady=0, width=25,text="Oui",command=lambda:save(PIN,code,wfor,mail,name,pop,fenetre))
        y.grid(row=1,column=0)
        n=t.Button(pop,padx=0, pady=0, width=25,text="Non",command=lambda:enleve(pop))
        n.grid(row=1,column=1)
        t.mainloop()

def erreur(msg):
    """
    Create a pop up who print the error message
    :param msg: (str) the error message
    """
    print("Une erreur est détectée: "+msg)
    pop=t.Tk(className="Erreur")
    txt=t.Label(pop,text=msg,fg='red',font=13)
    txt.pack()

def save(PIN,code,wfor,mail,file,pop,fentre):
    """
    Save all the data in the file
    :param PIN: (int) the PIN code
    :param code: (str) the code
    :param wfor: (str) the site or application
    :param mail: (str) the mail or identifiant
    :param file: (file) the name of the file
    :param pop: (tk.Tk) the pop up
    :param fentre: (tk.Tk) the current window
    """
    print("Sauvegarde des données dans le fichier"+file)
    pop.destroy()
    delete_item()
    a=c.coding(PIN,code,wfor,mail,file)
    a.encode()
    finaltest=d.decode(PIN,file)
    finaltest.decode()
    hey=final(finaltest.getres())
    pop=t.Canvas(window)
    pop.grid(column=0,row=0)
    txt=t.Label(pop,text="Mot de passe enregistre")
    txt.pack()

def use():
    """
    lit le manuel d'utilisation
    """
    res=''
    with open('lisezmoi.txt','r') as f:
        all=f.readlines()
        for i in all:
            res+=i
    return res

def helper(dyn):
    """
    Affiche l'aide dans le canvas dynamique
    """
    delete_item()
    dyn=t.Canvas(window)
    dyn.grid(column=0,row=0)
    aide=t.Label(dyn,text=use())
    aide.pack()
    
    
def menus(can):
    can.destroy()
    dyn=t.Canvas(window)
    dyn.grid(column=0,row=0)
    txt=t.Label(dyn,text="Bienvenue sur Hibiscus le gestionnaire de mot de passe",font=13)
    txt.pack()
    menu=t.Canvas(window,name='menu')
    menu.grid(column=1,row=0)
    #Ajout d'un bouton
    generate=t.Button(menu,padx=0, pady=0, width=25,text="Generer",command=lambda:generer(dyn))
    generate.pack(fill=t.X)
    decode=t.Button(menu,padx=0, pady=0, width=25,text="Obtenir",command=lambda:obtenir(dyn))
    decode.pack(fill=t.X)
    delete=t.Button(menu,padx=0, pady=0, width=25, text="Supprimer", command=lambda:deleter(dyn))
    delete.pack(fill=t.X)
    help=t.Button(menu,padx=0, pady=0, width=25,text="Aide",command=lambda:helper(dyn))
    help.pack(fill=t.X)
    
#generer obtenir helper
def makewindow():
    pageacc=t.Canvas(window,)
    pageacc.pack()
    #Ajout d'un bouton
    txt=t.Label(pageacc,text="Bienvenue sur Hibiscus le gestionnaire de mot de passe")
    txt.pack()
    menu=t.Button(pageacc,padx=0, pady=0, width=25,text="Commencer",command=lambda:menus(pageacc))
    menu.pack(fill=t.X)
    t.mainloop()
    
if __name__ == "__main__":
    makewindow()
