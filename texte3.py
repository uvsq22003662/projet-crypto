# projet crypto texte 3

#texte 3 :dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht.
#  kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?

#texte 2 décodé: le prochain fichier est code par un mot de passse de taille inconnue et contient l'indice. les lettres du 
# mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a ??? sont chiffrees.

#avec les indices du texte 2 décodé, je sais que ce texte est codé par un mot de passe et contient le mot "l'indice"
# pour ce texte, il est inutil de calculer la frequence des lettres comme le texte est chiffré par un mot de passe, et donc que chaque caractere 
# sera chiffré differement.
# en regardant le texte, je peux voir qu'il y a des lettres correspondant à des a comme le e du deuxieme mot et je peux egalement 
# deviner grace à l'apostrophe ainsi qu'a la taille du mot que "l'indice" correspond au mot "p'kyhhep".
# pour reussir a trouver le mot de passe, j'ai commencé en cherchant un mot de passe de taille 3 mais je n'ai rien trouvé. Puis en découpant le texte
# tout les 4 caracteres, je me suis apercue que les 2 a des 2 premiers mots etaient placés au meme niveau, c'est à dire à la position du 3e caractere 
# du mot de passe. En utilisant un découpage de 4 caracteres, j'ai pu trouver que le 3e caractere du mdp etait un w car e + w modulo26 = a et que le 
# 1er est un y car le n' de "n'ehfp" correspond forcement à un l. Donc en additionant les positions de n et y modulo 26 on trouve l. j'ai donc commencé 
# à décoder le texte grace à y en 1ere position du mot de passe et w en 3eme position.
#puis arrivé au mot "l'indice" qui etait codé en "p'kyhhep" j'ai pu trouver que k + y = i, y + p modulo 26 = n, h + w modulo 26 = w et h + b modulo 26 = i
# ce qui m'a permis d'en deduire que la deuxieme lettre du mot de passe est p et la derniere lettre du mot de passe est un b.

#le mot de passe est donc ypwb. Grace a ce mot de passe j'ai pu dechiffrer tout le texte. le mot de passe est de taille 4 et se repete ainsi tous les 
# 4 caracteres (espaces, points, virgules et apostrophe compris).

# le texte 3 dechiffré = bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez 
# vous dans un miroir, en etes vous un?


#pour faire un programme qui decode le texte 3 par un mot de passe j'avais pour idée de faire une liste 
# avec le mot de passe. Puis de faire une boucle qui tous les 4 caracteres va additionner la lettre du 
# mot de passe à la position correspodante modulo 26 et va renvoyer la lettre de l'alphabet correspondant.

message_code = input("entrer le message à décoder")

liste_mot_de_passe = ["y", "p", "w", "b"]

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

def dechiffrer(message_code, liste_mot_de_passe):
    for i in rangel(len(message_code)):
        pass
