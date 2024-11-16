import pandas as pd
import os

class Eleve:
    def __init__(self, id, nom, post_nom, prenom, sexe, date_de_naissance, lieu_de_naissance, nom_du_pere, numero_du_pere, nom_de_la_mere, numero_de_la_mere, nom_du_tuteur):
        self.id = id
        self.nom = nom
        self.post_nom = post_nom
        self.prenom = prenom
        self.sexe = sexe 
        self.date_de_naissance = date_de_naissance
        self.lieu_de_naissance = lieu_de_naissance
        self.nom_du_pere = nom_du_pere
        self.numero_du_pere = numero_du_pere
        self.nom_de_la_mere = nom_de_la_mere
        self.numero_de_la_mere = numero_de_la_mere
        self.nom_du_tuteur = nom_du_tuteur 

    def afficher_informations(self):
        print(f"ID: {self.id}, Nom: {self.nom}, Post-nom: {self.post_nom}, Prénom: {self.prenom}, Sexe: {self.sexe}, Date de Naissance: {self.date_de_naissance}, Lieu de Naissance: {self.lieu_de_naissance}, Nom du Père: {self.nom_du_pere}, Numéro du Père: {self.numero_du_pere}, Nom de la Mère: {self.nom_de_la_mere}, Numéro de la Mère: {self.numero_de_la_mere}, Nom du Tuteur: {self.nom_du_tuteur}")

    def modifier_information(self, champ, nouvelle_valeur):
        if hasattr(self, champ):
            setattr(self, champ, nouvelle_valeur)
            print(f"{champ} mis à jour avec succès.")
        else:
            print("Champ non valide.")

class Classe:
    def __init__(self, nom_classe):
        self.nom_classe = nom_classe
        self.eleves = []
        self.charger_donnees()

    def ajouter_eleve(self, eleve):
        self.eleves.append(eleve)
        self.eleves.sort(key=lambda e: (e.nom, e.post_nom, e.prenom))
        self.sauvegarder_donnees()
        print(f"{eleve.nom} {eleve.post_nom} {eleve.prenom} a été ajouté(e) à la classe {self.nom_classe}.")

    def retirer_eleve(self, id):
        self.eleves = [eleve for eleve in self.eleves if eleve.id != id]
        self.sauvegarder_donnees()
        print(f"L'élève avec l'ID {id} a été retiré de la classe {self.nom_classe}.")

    def afficher_eleves(self):
        print(f"Élèves dans la classe {self.nom_classe}:")
        for eleve in self.eleves:
            eleve.afficher_informations()

    def rechercher_eleve(self, critere, valeur):
        resultats = [eleve for eleve in self.eleves if getattr(eleve, critere) == valeur]
        if resultats:
            for eleve in resultats:
                eleve.afficher_informations()
        else:
            print(f"Aucun élève trouvé avec {critere} = {valeur}.")

    def sauvegarder_donnees(self):
        data = [{
            "ID": eleve.id,
            "Nom": eleve.nom,
            "Post-nom": eleve.post_nom,
            "Prénom": eleve.prenom,
            "Sexe": eleve.sexe,
            "Date de Naissance": eleve.date_de_naissance,
            "Lieu de Naissance": eleve.lieu_de_naissance,
            "Nom du Père": eleve.nom_du_pere,
            "Numéro du Père": eleve.numero_du_pere,
            "Nom de la Mère": eleve.nom_de_la_mere,
            "Numéro de la Mère": eleve.numero_de_la_mere,
            "Nom du Tuteur": eleve.nom_du_tuteur
        } for eleve in self.eleves]
        
        df = pd.DataFrame(data)
        df.to_excel(f"{self.nom_classe}.xlsx", index=False)
        print(f"Données sauvegardées dans le fichier {self.nom_classe}.xlsx")

    def charger_donnees(self):
        if os.path.exists(f"{self.nom_classe}.xlsx"):
            df = pd.read_excel(f"{self.nom_classe}.xlsx")
            for _, row in df.iterrows():
                eleve = Eleve(
                    id=row["ID"],
                    nom=row["Nom"],
                    post_nom=row["Post-nom"],
                    prenom=row["Prénom"],
                    sexe=row["Sexe"],
                    date_de_naissance=row["Date de Naissance"],
                    lieu_de_naissance=row["Lieu de Naissance"],
                    nom_du_pere=row["Nom du Père"],
                    numero_du_pere=row["Numéro du Père"],
                    nom_de_la_mere=row["Nom de la Mère"],
                    numero_de_la_mere=row["Numéro de la Mère"],
                    nom_du_tuteur=row["Nom du Tuteur"]
                )
                self.eleves.append(eleve)

class Ecole:
    def __init__(self, nom_ecole):
        self.nom_ecole = nom_ecole
        self.classes = {}

    def ajouter_classe(self, classe):
        self.classes[classe.nom_classe] = classe

    def choisir_classe(self, nom_classe):
        return self.classes.get(nom_classe, None)

ecole = Ecole("Lycée Étoile Brillante")
for i in ["1ère", "2e", "3e", "4e", "5e", "6e"]:
    ecole.ajouter_classe(Classe(i))

def ajouter_eleve_dans_classe():
    nom_classe = input("Dans quelle classe souhaitez-vous ajouter un élève ? (ex: '1ère', '2e', ... , '6e') : ")
    classe = ecole.choisir_classe(nom_classe)
    if classe:
        id = input("ID : ")
        nom = input("Nom : ")
        post_nom = input("Post-nom : ")
        prenom = input("Prénom : ")
        sexe = input("Sexe : ")
        date_de_naissance = input("Date de naissance : ")
        lieu_de_naissance = input("Lieu de naissance : ")
        nom_du_pere = input("Nom du père : ")
        numero_du_pere = input("Numéro du père : ")
        nom_de_la_mere = input("Nom de la mère : ")
        numero_de_la_mere = input("Numéro de la mère : ")
        nom_du_tuteur = input("Nom du tuteur : ")

        eleve = Eleve(id, nom, post_nom, prenom, sexe, date_de_naissance, lieu_de_naissance, nom_du_pere, numero_du_pere, nom_de_la_mere, numero_de_la_mere, nom_du_tuteur)
        classe.ajouter_eleve(eleve)
    else:
        print("Classe non trouvée.")

def rechercher_eleve_dans_classe():
    nom_classe = input("Dans quelle classe souhaitez-vous rechercher un élève ? : ")
    classe = ecole.choisir_classe(nom_classe)
    if classe:
        critere = input("Voulez-vous rechercher par (id, nom, post_nom, prenom) : ")
        valeur = input(f"Entrez la valeur pour {critere} : ")
        classe.rechercher_eleve(critere, valeur)
    else:
        print("Classe non trouvée.")

# Menu principal
while True:
    print("\nOptions :")
    print("1: Ajouter un élève dans une classe")
    print("2: Retirer un élève d'une classe")
    print("3: Afficher la liste des élèves dans une classe")
    print("4: Rechercher un élève dans une classe")
    print("5: Modifier les informations d'un élève")
    print("6: Générer un fichier Excel pour une classe")
    print("7: Quitter")
    
    choix = input(" Quelle est Votre choix : ")
    
    if choix == "1":
        ajouter_eleve_dans_classe()
    elif choix == "2":
        nom_classe = input("Dans quelle classe souhaitez-vous retirer un élève ? : ")
        classe = ecole.choisir_classe(nom_classe)
        if classe:
            id = input("ID de l'élève à retirer : ")
            classe.retirer_eleve(id)
        else:
            print("Classe non trouvée.")
    elif choix == "3":
        nom_classe = input("Quelle classe afficher ? : ")
        classe = ecole.choisir_classe(nom_classe)
        if classe:
            classe.afficher_eleves()
        else:
            print("Classe non trouvée.")
    elif choix == "4":
        rechercher_eleve_dans_classe()
    elif choix == "5":
        nom_classe = input("Dans quelle classe se trouve l'élève ? : ")
        classe = ecole.choisir_classe(nom_classe)
        if classe:
            id = input("ID de l'élève à modifier : ")
            eleve = next((e for e in classe.eleves if e.id == id), None)
            if eleve:
                champ = input("Champ à modifier : ")
                nouvelle_valeur = input("Nouvelle valeur : ")
                eleve.modifier_information(champ, nouvelle_valeur)
                classe.sauvegarder_donnees()
            else:
                print("Élève non trouvé.")
        else:
            print("Classe non trouvée.")
    elif choix == "6":
        nom_classe = input("Classe à sauvegarder en fichier Excel : ")
        classe = ecole.choisir_classe(nom_classe)
        if classe:
            classe.sauvegarder_donnees()
        else:
            print("Classe non trouvée.")
    elif choix == "7":
        print("Programme terminé.")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
