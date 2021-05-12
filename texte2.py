#projet crypto TEXTE 2 
#texte 2 : gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx 
# qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi.
#RESULTAT DECRYPTAGE TEXTE 1 :le prochain fichier aura un code par substitution alphabetique: chaque lettre est remplacee 
# par une autre. utiliser la frequence des lettres pour decoder le message.

#grace au texte decrypté 1, je sais que le texte 2 est codé par substitution. Pour pouvoir décoder le message, 
#j'ai utilisé la frequence de chaque lettre pour voir quelles sont les lettres les plus redondentes et les comparer avec la 
#frequence d'apparition des lettres en francais.

def frequence(message_chiffre):
    resultat = []
    for c in message_chiffre :
        if 97 <= ord(c) <= 122:
            exist = True
            for i in range(len(resultat)) :
                if resultat[i][0] == c :
                    exist = False
            if exist :
                resultat.append([c, round(message_chiffre.count(c)/len(message_chiffre)*100,2)])
    return resultat
print(frequence("gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."))


#apres avoir trouvé la frequence de chaque lettre, la plus frequente est le x donc je peux en deduire que le x correspond au e.
#en regardant les autres lettres les plus frequentes, il y a le i, comme dans le mot xiu, or le s est une des lettres les plus frequentes
#  de la langue francaise, donc j'en deduis que xiu correspond au mot est.
#de plus le debut de phrase(gx qosvlnkd wkvlkxo) comporte des mots de taille similaire au premier texte, j'essaie donc de remplacer chaque 
# mot codé par les mots du premier texte décodé.
#et ainsi de suite j'arrive a décoder lettre par lettre le texte.
#j'obtients : x=e , i=s , u=t , g=l , c=d , k=i , d=n , n=a , o=r , s=o , v=c , y=u , q=p , f=m , l=h , w=f , m=g, a= ???
#je n'arrive seulement pas a décoder la lettre a comme elle n'apparait qu'une seule fois dans le texte et les lettres b,j,k,q,w,x,y,z ne sont pas codées.

#le texte 2 décodé par substitution est donc : le prochain fichier est code par un mot de passse de taille inconnue et contient l'indice. les lettres du 
# mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a ??? sont chiffrees.

# je n'ai pas reusi à créer un programme codant ce decryptage. Pour coder ce message j'ai pour idee de creer une liste qui prend les valeurs en code ascii des
# lettres de a à z. Je voulais également créer une boucle qui va parcourir les caracteres du message codé 1 par 1 

message_code = input("entrer le message à décoder")

liste_caracteres_substitue: ["z", "", "d", "n", "", "m", "l", "", "s", "", "i", "h", "g", "a", "r", "", "p", "a", "o", "", "t", "c", "f", "e", "u", ""]

def rang(lettre):
    return ord(lettre)-97


def decalage(lettre_message,lettre_cle):
    if 97 <= ord(lettre_message) <= 122 :
        return chr((rang(lettre_message) + rang(lettre_cle))%26 + 97)
    else :
        return lettre_message

def dec_texte(texte,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(texte)):
        res += decalage(texte[i],cle[i%taille_cle])
    return res

def dechiffrer(message_code, liste_position_caracteres_substitue):
#boucle for qui permettrait de remplacer la veleur d'un caractere du texte par celui de la liste des caracteres substitués. Pour cela j'avais pour idée de prendre 
# la valeur ascii du caractere a decoder et de soustraire 97 puis de prendre la lettre correspondante à cette position dans la liste, ce qui nous permettrait de 
# remplacer les caracteres 1 par 1. Pour remplacer les caracteres on peut utiliser la fonction enumerate() dans une boucle qui renvoie 2 listes.
    for i in range(len(message_code)):
        pass


# je pense que la lettre a correspond à z.
