def convertisseur(nombreAconvertir,baseDuNombre,baseVoulu):
    
    """
    Cette fonction permet de convertir de base 10 en n'importe qu'elle base.
    Si le nombre de base n'est pas en base 10, alors une autre fonction se charge de le transformer.
    -----------------
    paramètre : 
        nombreAconvertir : un int 
        baseDuNombre : un int 
        baseVoulu : un int
    -----------------
    renvoie le nombre initial, puis ce qu'il donne dans une autre base
    """
    
    if baseDuNombre!=10:
        décimal(nombreAconvertir,baseDuNombre)
    
    résultat=[]
    nombre=nombreAconvertir
    
    while nombre!=0:
        résultat.append(nombre%baseVoulu)
        nombre=nombre//baseVoulu
    
    résultat.reverse()
    réponse = ''.join(str(elem)for elem in résultat)#permet de transformer la liste en texte compact
    
    return print (" le nombre de base était", nombreAconvertir,"de base", baseDuNombre,
                 ".Il est égal à ",réponse,"en base ", baseVoulu )

def décimal (nombreAconvertir,baseDuNombre):
    
    """
    ce programme permet de convertir un nombre de n'importe qu'elle base en base 10. 
    Si vous utilisez une base supérieur à  la base 10,
    mettez des "" lorsque vous écrivez le nombre à convertir.
    -----------------
    paramètre : 
        nombreAconvertir : un int 
        baseDuNombre : un int 
    -----------------
    renvoie le nombre initial et sa base, et sa valeur en base 10
    """
    
    compteur=x=puissance=résultat=0
    nombreCaractère=len(str(nombreAconvertir))#compte le nombre de caractère du nombre
    liste=list(str(nombreAconvertir))#transforme un nombre compact en liste
    liste.reverse()#inverse les valeurs de la liste
    
    if baseDuNombre>10:
        while compteur!=nombreCaractère:
            if liste[x]=="A":
                liste[x]=10
            if liste[x]=="B":
                liste[x]=11
            if liste[x]=="C":
                liste[x]=12
            if liste[x]=="D":
                liste[x]=13
            if liste[x]=="E":
                liste[x]=14
            if liste[x]=="F":
                liste[x]=15
            compteur=compteur+1
            x=x+1

    compteur=x=0
    
    while compteur!=nombreCaractère:
        résultat=résultat+int(liste[x])*baseDuNombre**puissance
        compteur=compteur+1
        x=x+1
        puissance=puissance+1
    return print( " le nombre de base était", nombreAconvertir,"de base", baseDuNombre,
                 ".Il est égal à ",résultat,"en base 10")