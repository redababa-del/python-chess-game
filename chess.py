from qtido import *

# ─── fcts init ──────#
def dessiner_case_vide(f, ligne, colonne):
    if (ligne + colonne) % 2 == 0:
        couleur(f, 0.5, 0.5, 0.5)
    else:
        couleur(f, 1, 1, 1)
    rectangle(f, ligne * 100, colonne * 100, (ligne + 1) * 100, (colonne + 1) * 100)

def tracer_plateau(f):
    for i in range(8):
        for j in range(8):
            dessiner_case_vide(f, i, j)

def afficher_code_cases(f):
    i = 0
    for j in range(8):
        couleur(f, 1, 1, 1)
        y = j * 100 + 50
        texte(f, 850, y, 20, str(j + 1))
    for j in range(8):
        abc = "ABCDEFGH"
        couleur(f, 1, 1, 1)
        y = j * 100 + 50
        texte(f, y, 850, 20, abc[i])
        i += 1

# ─── Dessin pieces ───────────────#
def tracer_tour(f, i, j, cp):
    cp
    rectangle(f, (i*100)+20, (j*100)+80, (i*100)+80, (j*100)+100)
    rectangle(f, (i*100)+30, (j*100)+30, (i*100)+70, (j*100)+80)
    rectangle(f, (i*100)+20, (j*100)+20, (i*100)+80, (j*100)+30)
    rectangle(f, (i*100)+20, (j*100)+10, (i*100)+30, (j*100)+20)
    rectangle(f, (i*100)+40, (j*100)+10, (i*100)+60, (j*100)+20)
    rectangle(f, (i*100)+70, (j*100)+10, (i*100)+80, (j*100)+20)
def tracer_fou(f, i, j, cp):
    im = i * 100
    jm = j * 100
    cp
    rectangle(f, im+20, jm+80, im+80, jm+100)
    rectangle(f, im+35, jm+40, im+65, jm+80)
    rectangle(f, im+40, jm+30, im+60, jm+40)
    disque(f, im+50, jm+20, 10)
def tracer_pion(f, i, j, cp):
    im = i * 100
    jm = j * 100
    cp
    rectangle(f, im+30, jm+80, im+70, jm+100)
    rectangle(f, im+40, jm+50, im+60, jm+80)
    disque(f, im+50, jm+40, 10)
def tracer_reine(f, i, j, cp):
    im = i * 100
    jm = j * 100
    cp
    rectangle(f, im+20, jm+80, im+80, jm+100)
    rectangle(f, im+30, jm+40, im+70, jm+80)
    rectangle(f, im+25, jm+30, im+75, jm+40)
    disque(f, im+30, jm+20, 5)
    disque(f, im+50, jm+15, 7)
    disque(f, im+70, jm+20, 5)
def tracer_roi(f, i, j, cp):
    im = i * 100
    jm = j * 100
    cp
    rectangle(f, im+20, jm+80, im+80, jm+100)
    rectangle(f, im+30, jm+35, im+70, jm+80)
    rectangle(f, im+35, jm+25, im+65, jm+35)
    rectangle(f, im+48, jm+10, im+52, jm+25)
    rectangle(f, im+42, jm+15, im+58, jm+20)
def tracer_cheval(f, i, j, cp):
    im = i * 100
    jm = j * 100
    cp
    rectangle(f, im+20, jm+80, im+80, jm+100)
    rectangle(f, im+30, jm+50, im+70, jm+80)
    rectangle(f, im+40, jm+30, im+60, jm+50)
    rectangle(f, im+50, jm+20, im+70, jm+30)
    rectangle(f, im+60, jm+10, im+65, jm+20)

# ─── affichage de lechiquier ──────#

def initialiser_echiquier():
    echiquier = []
    echiquier.append(["tour-N", "chevalier-N", "fou-N", "reine-N", "roi-N", "fou-N", "chevalier-N", "tour-N"])
    echiquier.append(["pion-N"] * 8)
    for i in range(4):
        echiquier.append([""] * 8)
    echiquier.append(["pion-B"] * 8)
    echiquier.append(["tour-B", "chevalier-B", "fou-B", "reine-B", "roi-B", "fou-B", "chevalier-B", "tour-B"])
    return echiquier

def remplir_et_tracer_echiquier(f, echiquier):
    for i in range(8):
        for j in range(8):
            piece = echiquier[j][i]
            if piece != "":
                if piece[-1] == "B":
                    cp = couleur(f, 1, 0.7, 0)
                else:
                    cp = couleur(f, 0, 0, 0)
                nom = piece[:-2]
                if   nom == "tour":      tracer_tour(f, i, j, cp)
                elif nom == "fou":       tracer_fou(f, i, j, cp)
                elif nom == "chevalier": tracer_cheval(f, i, j, cp)
                elif nom == "reine":     tracer_reine(f, i, j, cp)
                elif nom == "roi":       tracer_roi(f, i, j, cp)
                elif nom == "pion":      tracer_pion(f, i, j, cp)

# ───code a num ───────────────#

def de_code_a_num_case(code):
    lettres = "ABCDEFGH"
    num = []
    num.append(int(code[1]) - 1)
    for i in range(8):
        if code[0] == lettres[i]:
            num.append(i)
    return num

def mise_a_jour_echiquier(echiquier, case_a_bouger, nouvelle_case):
    code_i = de_code_a_num_case(case_a_bouger)
    code_f = de_code_a_num_case(nouvelle_case)
    echiquier[code_f[0]][code_f[1]] = echiquier[code_i[0]][code_i[1]]
    echiquier[code_i[0]][code_i[1]] = ""
    return echiquier




# ───verif code case ─────--──"
def verifier_code_case(code):
    alph = "ABCDEFGH"
    if len(code) != 2:
        return False
    if code[0] not in lettres:
        return False
    if not (1 <= int(code[1]) <= 8):
        return False
    return True

def saisir_case_valide(code):
    code = input("entrer le code de la case")
    while not verifier_code_case(code):
        print("Code pas valide")
        code = input("entrer le code de la case")
    return code







#
# ─── regles de deplcment───────────────#
#
def chemin_libre(echiquier, x1, y1, x2, y2):
    if x2 == x1:
        pas_x = 0
    elif x2 > x1:
        pas_x = 1
    else:
        pas_x = -1
    if y2 == y1:
        pas_y = 0
    elif y2 > y1:
        pas_y = 1
    else:
        pas_y = -1
    cx = x1 + pas_x
    cy = y1 + pas_y
    while (cx, cy) != (x2, y2):
        if echiquier[cx][cy] != "":
            return False
        cx += pas_x
        cy += pas_y
    return True

def verif_tour(echiquier, x1, y1, x2, y2, dx, dy):
    if dx != 0 and dy != 0:
        return False
    return chemin_libre(echiquier, x1, y1, x2, y2)

def verif_fou(echiquier, x1, y1, x2, y2, dx, dy):
    if abs(dx) != abs(dy):
        return False
    return chemin_libre(echiquier, x1, y1, x2, y2)

def verif_chevalier(dx, dy):
    return (abs(dx), abs(dy)) in [(1, 2), (2, 1)]

def verif_reine(echiquier, x1, y1, x2, y2, dx, dy):
    if dx != 0 and dy != 0 and abs(dx) != abs(dy):
        return False
    return chemin_libre(echiquier, x1, y1, x2, y2)

def verif_roi(dx, dy):
    if abs(dx) <= 1 and abs(dy) <= 1 and (dx, dy) != (0, 0):
        return True
    else:
        return False

def verif_pion(echiquier, x1, y1, x2, y2, dx, dy, couleur_joueur):
    if couleur_joueur == "N":
        direction = 1
        ligne_depart = 1
    else:
        direction = -1
        ligne_depart = 6
    if dy == 0:
        if dx == direction and echiquier[x2][y2] == "":
            return True
        else:
            if dx == 2 * direction:
                if x1 == ligne_depart:
                    if echiquier[x2][y2] == "":
                        if echiquier[x1 + direction][y1] == "":
                            return True
    else:
        if abs(dy) == 1 and dx == direction:
            if echiquier[x2][y2] != "":
                return True
    return False

def verifier_deplacement(echiquier, case_depart, case_arrivee, couleur_joueur):
    x1, y1 = de_code_a_num_case(case_depart)
    x2, y2 = de_code_a_num_case(case_arrivee)
    piece = echiquier[x1][y1]
    print(f"piece={piece}, couleur_joueur={couleur_joueur}, x1={x1}, y1={y1}")
    if piece == "":
        print("case vide")
        return False
    else:
        if piece[-1] != couleur_joueur:
            print("Cette piece nest pas a vous")
            return False

    cible = echiquier[x2][y2]
    if cible != "":
        if cible[-1] == couleur_joueur:
            print("case occupé")
            return False
    if case_depart == case_arrivee:
        print("vous vous deplacer en meme case")
        return False
    
    dx = x2 - x1
    dy = y2 - y1
    nom = piece[:-2]
    valide = False
    if nom == "tour":
        valide = verif_tour(echiquier, x1, y1, x2, y2, dx, dy)
    else:
        if nom == "fou":
            valide = verif_fou(echiquier, x1, y1, x2, y2, dx, dy)
        else:
            if nom == "chevalier":
                valide = verif_chevalier(dx, dy)
            else:
                if nom == "reine":
                    valide = verif_reine(echiquier, x1, y1, x2, y2, dx, dy)
                else:
                    if nom == "roi":
                        valide = verif_roi(dx, dy)
                    else:
                        if nom == "pion":
                            valide = verif_pion(echiquier, x1, y1, x2, y2, dx, dy, couleur_joueur)
    if not valide:
        print("Déplacement non autorisé")
    return valide

#----------------fcts souris---------------#
def cor_to_pos(x, y):
    num_colonne = x//100
    num_ligne = y//100
    return [num_ligne, num_colonne]

def num_case_a_code(l, c):
    lettres = "ABCDEFGH"
    return lettres[c] + str(l + 1)

#
# ──----------------─------- Lancement du jeu ------------------------─────────────#
f = creer(900, 900)
tracer_plateau(f)
echiquier = initialiser_echiquier()
remplir_et_tracer_echiquier(f, echiquier)
re_afficher(f)

#------------choix utulisation terminal/souris--------------#
utulisation = input("vous voulez utuliser [terminal] ou [souris]: ")
if utulisation == "terminal" :
    rep = "oui"
    while rep == "oui":
        # ── Joueur 1 ──
        print("C’est au tour du joueur 1 : ")
        valide_j1 = False
        while not valide_j1:
            case_a_bouger_j1 = input("Quel est le code de la pièce à déplacer ?")
            nouvelle_case_j1 = input("Quel est le code de la case destinataire ?")
            if verifier_deplacement(echiquier, case_a_bouger_j1, nouvelle_case_j1, "N"):
                valide_j1 = True
            else:
                print("Déplacement invalide pour le joueur 1, réessayez.")

            mise_a_jour_echiquier(echiquier, case_a_bouger_j1, nouvelle_case_j1)
            tracer_plateau(f)
            remplir_et_tracer_echiquier(f, echiquier)
            re_afficher(f)

        # ── Joueur 2 ──
        print("C’est au tour du joueur 2 : ")
        valide_j2 = False
        while not valide_j2:
            case_a_bouger_j2 = input("Quel est le code de la pièce à déplacer ?")
            nouvelle_case_j2 = input("Quel est le code de la case destinataire ?")
            if verifier_deplacement(echiquier, case_a_bouger_j2, nouvelle_case_j2, "B"):
                valide_j2 = True
            else:
                print("Déplacement invalide pour le joueur 2, réessayez.")
            
            mise_a_jour_echiquier(echiquier, case_a_bouger_j2, nouvelle_case_j2)
            tracer_plateau(f)
            remplir_et_tracer_echiquier(f, echiquier)
            re_afficher(f)

            rep = input("Souhaitez-vous continuer ? Tapper oui pour continuer, et non pour quitter ")

else :
    case_selectionnee = None
    joueur = "B"
    while not est_fermee(f):
        attendre_evenement(f, 100)
        e = dernier_evenement(f)
        if est_souris(f, e, "PRESS"):
            x, y = coordonnees_souris(f, e)
            print(x, y, "→", cor_to_pos(x, y))
            l, c = cor_to_pos(x, y)
            if case_selectionnee is None:
                if echiquier[l][c] != "":
                    case_selectionnee = (l, c)
            else:
                l_dep, c_dep = case_selectionnee
                l_arr, c_arr = l, c
                case_dep = num_case_a_code(l_dep, c_dep)
                case_arr = num_case_a_code(l_arr, c_arr)
                    
                if verifier_deplacement(echiquier, case_dep, case_arr, joueur):
                    mise_a_jour_echiquier(echiquier, case_dep, case_arr)
                    tracer_plateau(f)
                    remplir_et_tracer_echiquier(f, echiquier)
                    re_afficher(f)
                    joueur = "B" if joueur == "N" else "N"
                case_selectionnee = None
attendre_fermeture(f)