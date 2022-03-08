# On importe le module pandas et le tableau sous forme de texte

import pandas as pd

data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")


#On affiche le nombre de personnes qui ont répondu par catégorie pour "fréquence utilisation avion"

def disposition_frequence_reponse () :

    df = data["Frequence utilisation avion ?"].value_counts () 

    print (df)


# Once year or less = 1 

# Once month or less = 2 

# Never = 3 

# A few times per week = 4 

# Every day = 5 


# Moyenne d'âge par rapport à la frequence d'utiisation de l'avion qui est "once a year or less"

def moyenne_age_1 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a year or less"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport a la frequence d'utiisation de l'avion ,qui est once a year or less, est de : " \

           + str (moyenne_df))

    
# Moyenne d'âge par rapport à la frequence d'utiisation de l'avion qui est "never"

def moyenne_age_2 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Never"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport a la frequence d'utiisation de l'avion ,qui est Never, est de : " \

           + str (moyenne_df))

    

# Moyenne d'âge par rapport à la frequence d'utiisation de l'avion qui est "A few times per week"

def moyenne_age_3 () :

    data = pd.read_csv(r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "A few times per week"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport a la frequence d'utiisation de l'avion ,qui est A few times per week, est : " \

           + str (moyenne_df) + ". Il n'y a donc aucune donnée pour ce rapport" )

    
# Moyenne d'âge par rapport à la frequence d'utiisation de l'avion qui est "Every day"   

def moyenne_age_4 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Every day"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport a la frequence d'utiisation de l'avion ,qui est Every day, est de : " \

           + str (moyenne_df))


# Moyenne d'âge par rapport à la frequence d'utiisation de l'avion qui est "Once a month or less" 

def moyenne_age_5 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a month or less"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport a la frequence d'utiisation de l'avion ,qui est Once a month or less, est de : " \

           + str (moyenne_df))


#On affiche le nombre de personnes qui ont répondu par catégorie pour "Revenu du menage"

def disposition_revenu () :

    df = data["Revenu du menage "].value_counts () 

    print (df)



# Moyenne de revenue du ménage par rapport à la frequence d'utiisation de l'avion qui est
#"once a year or less"

def moyenne_revenue_1 () : 

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a year or less"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenu du menage par rapport a la frequence d'utiisation de l'avion ,"\

           +"qui est Once a year or less, est de : " \

           + str (moyenne_df))


# moyenne de revenue du ménage par rapport à la frequence d'utiisation de l'avion qui est
#"Never"

def moyenne_revenue_2 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Never"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenu du menage par rapport a la frequence d'utiisation de l'avion ,"\

           +"qui est Never, est de : " \

           + str (moyenne_df))


# Moyenne de revenue du ménage par rapport à la frequence d'utiisation de l'avion qui est
#"A few times per week"

def moyenne_revenue_3 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "A few times per week"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenu du menage par rapport a la frequence d'utiisation de l'avion ,"\

           +"qui est A few times per week, est : " \

           + str (moyenne_df) + ". Il n'y a donc aucune donnée pour ce rapport")



# Moyenne de revenue du ménage par rapport à la frequence d'utiisation de l'avion qui est
#"Every day"

def moyenne_revenue_4 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Every day"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenu du menage par rapport a la frequence d'utiisation de l'avion ,"\

           +"qui est Every day, est de : " \

           + str (moyenne_df))



# Moyenne de revenue du ménage par rapport à la frequence d'utiisation de l'avion qui est
#"Once a month or less"

def moyenne_revenue_5 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a month or less"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenu du menage par rapport a la frequence d'utiisation de l'avion ,"\

           +"qui est Once a month or less, est de : " \

           + str (moyenne_df)) 









#On affiche le nombre de personnes qui ont répondu par catégorie pour "Diplome"

def disposition_diplome () :

    df = data["Diplome "].value_counts () 

    print (df)



#Disposition des diplomes en fonction de la frequence d'utilisation de l'avion qui est:
#"Once a year or less"           

def diplome_rapport_frequence1 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a year or less"

    filtered_df = data[df_mask]

    disposition_diplome_frequence = filtered_df["Diplome "].value_counts ()

    print (disposition_diplome_frequence)



#Disposition des diplomes en fonction de la frequence d'utilisation de l'avion qui est:
#"Never"

def diplome_rapport_frequence2 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Never"

    filtered_df = data[df_mask]

    disposition_diplome_frequence = filtered_df["Diplome "].value_counts ()

    print (disposition_diplome_frequence)



#Disposition des diplomes en fonction de la frequence d'utilisation de l'avion qui est:
#A few times per week"

def diplome_rapport_frequence3 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "A few times per week"

    filtered_df = data[df_mask]

    disposition_diplome_frequence = filtered_df["Diplome "].value_counts ()

    print (disposition_diplome_frequence)

    print  ("Il n'y a donc aucune valeur pour ce rapport ci-contre")



#Disposition des diplomes en fonction de la frequence d'utilisation de l'avion qui est:
#"Every day"  

def diplome_rapport_frequence4 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Every day"

    filtered_df = data[df_mask]

    disposition_diplome_frequence = filtered_df["Diplome "].value_counts ()

    print (disposition_diplome_frequence)



#Disposition des diplomes en fonction de la frequence d'utilisation de l'avion qui est:
#"Once a month or less"

def diplome_rapport_frequence5 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a month or less"

    filtered_df = data[df_mask]

    disposition_diplome_frequence = filtered_df["Diplome "].value_counts ()

    print (disposition_diplome_frequence)




#On affiche le nombre de personnes qui ont répondu par catégorie pour Emplacement (region de recensement)

def disposition_emplacement () :

    df = data["Emplacement (region de recensement)"].value_counts () 

    print (df)



#Emplacement des personnes qui une utilise l'avion une fois ou moins souvent dans l'année. 

def emplacement_rapport_frequence1 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a year or less"

    filtered_df = data[df_mask]

    disposition_emplacement_frequence = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print (disposition_emplacement_frequence)    



#Emplacement des personnes qui n'utilisent jamais l'avion 

def emplacement_rapport_frequence2 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Never"

    filtered_df = data[df_mask]

    disposition_emplacement_frequence = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print (disposition_emplacement_frequence) 

 

#Emplacement des personnes qui utilisent l'avion quelques fois par semaine. 

def emplacement_rapport_frequence3 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "A few times per week"

    filtered_df = data[df_mask]

    disposition_emplacement_frequence = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print (disposition_emplacement_frequence)

    print  ("Il n'y a donc aucune valeur pour ce rapport ci-contre")



#Emplacement des personnes qui utilisent l'avion tout les jours. 

def emplacement_rapport_frequence4 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Every day"

    filtered_df = data[df_mask]

    disposition_emplacement_frequence = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print (disposition_emplacement_frequence) 



#Emplacement des personnes qui utilisent l'avion une fois ou moins par mois. 

def emplacement_rapport_frequence5 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Frequence utilisation avion ?"] == "Once a month or less"

    filtered_df = data[df_mask]

    disposition_emplacement_frequence = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print (disposition_emplacement_frequence)


# Moyenne d'âg de cuex qui n'utilisent pas leurs appreils éléctroniques lors des phases critiques du vol   

def moyenne_age_rapport_appareil_electronique1 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Have you ever used personal electronics during take off or landing in violation of a flight " \

                   + "attendant's direction ?"] == "No"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport aux personnes qui n'ont jamais utilisé leur telephone dans l'avion est de : " \

           + str (moyenne_df)) 

    

# moyenne d'âge de ceux qui utilisent leurs appareils éléctroniques lors des phases critiques du vol

def moyenne_age_rapport_appareil_electronique2 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Have you ever used personal electronics during take off or landing in violation of a flight " \

                   + "attendant's direction ?"] == "Yes"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport aux personnes qui ont jamais deja utilisé leur telephone dans l'avion est de : " \

           + str (moyenne_df))   


#On regarde l'emplacement des personnes qui ont répondu "No" à la question : 
#Avez vous déjà utilisé un appareil éléctronique lors des phases critique de vol 

def etude_appareil_electronique1 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Have you ever used personal electronics during take off or landing in violation of "\

                   + "a flight attendant's direction ?"] == "No"

    filtered_df = data[df_mask]

    disposition_origine_etranger = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print ("La disposition des études des gens qui n'ont jamais utilisé un appareil electronique durant un vol est :" 

           + str (disposition_origine_etranger)) 



#Emplacement des personnes qui ont répondu "Yes" à la question : 
#Avez vous déjà utilisé un appareil éléctronique lors des phases critique de vol 

def etude_appareil_electronique2 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Have you ever used personal electronics during take off or landing in violation of "\

                   + "a flight attendant's direction ?"] == "Yes"

    filtered_df = data[df_mask]

    disposition_origine_etranger = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print ("La disposition des études des gens qui ont deja utilisé un appareil electronique durant un vol est :" 

           + str (disposition_origine_etranger)) 



# Moyenne du revenue du ménage pour les personnes qui ont répondu "No" à la question : 
# Avez vous déjà utilisé un appareil éléctronique lors des phases critique de vol

def moyenne_revenue_appareil_electronique1 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Have you ever used personal electronics during take off or landing in violation of a flight " \

                       + "attendant's direction ?"] == "No"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne de revenue de menage par rapport aux personnes qui n'ont jamais utilisé leur telephone dans l'avion est de : " \

               + str (moyenne_df)) 



# Moyenne du revenue du ménage pour les personnes qui ont répondu "Yes" à la question : 
#Avez vous déjà utilisé un appareil éléctronique lors des phases critique de vol        

def moyenne_revenue_appareil_electronique2 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Have you ever used personal electronics during take off or landing in violation of a flight " \

                       + "attendant's direction ?"] == "Yes"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenue du manage par rapport aux personnes qui ont deja utilisé leur telephone dans"\

           + " l'avion est de : " \

               + str (moyenne_df)) 


# Moyenne du revenue par rapport au controle du hublot 
#pour ceux qui pense que les deux personnes assises devraient avoir le controle du hublot 


def moyenne_revenue_rapport_hublot1 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Qui devrait avoir le controle du hublot ?"] == "Everyone in the row should have some say"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenue du menage par rapport aux personnes qui pensent que les deux personnes" \

           + " devraient avoir le controle du hublot est de : "

           + str (moyenne_df))   



# Moyenne de revenue par rapport au controle du hublot
# pour ceux qui pensent que seulement la personne assise près du hublot devrait en avoir le controle 

def moyenne_revenue_rapport_hublot2 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Qui devrait avoir le controle du hublot ?"] == "The person in the window seat should have exclusive control"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenue d par rapport aux personnes qui pensent qu'une seule personne" \

           + " devrait avoir le controle du hublot est de "

           + str (moyenne_df))



# Moyenne de revenue de ceux qui pensent qu'il est impoli de s'installer sur des siège invendus 

def moyenne_revenue_rapport_sieges_invendus1 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Est-il imprudent de s'installer sur des sieges invendus dans les avions ?"] == "Yes  very rude"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenue d par rapport aux personnes qui pensent qu'il est possible de s'assoir" \

           + " sur des sièges invendus est de : "

           + str (moyenne_df))

        

# Moyenne de revenue des personnes qui pensent qu'il n'est pas imoli de s'installer sur des sièges invendus 

def moyenne_revenue_rapport_sieges_invendus2 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Est-il imprudent de s'installer sur des sieges"\

                   + " invendus dans les avions ?"] == "No  not rude at all"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Revenu du menage "].mean ()

    print ("La moyenne du revenue d par rapport aux personnes qui pensent qu'il n'est pas possible de s'assoir" \

           + " sur des sièges invendus est de : "

           + str (moyenne_df))





# Avis des personnes qui ont répondu qu'il était impoli d'incliner son siège en avion en fonction de leur taille

def disposition_taille_inclinaison_siege1 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Est-il impoli d'incliner votre siege dans un avion ?"] == "Yes  somewhat rude"

    filtered_df = data[df_mask]

    disposition_taille_sieges = filtered_df["Quelle taille mesurez-vous?"].value_counts ()

    print ("La disposition de la taille des gens qui pensent qu'il est impoli d'incliner son siège est de : " + "" \

           + str (disposition_taille_sieges))



# Avis des personnes qui ont répondu qu'il n'était pas impoli d'incliner son siège en avion en fonction de leur taille

def disposition_taille_inclinaison_siege2 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Est-il impoli d'incliner votre siege dans un avion ?"] == "No  not rude at all"

    filtered_df = data[df_mask]

    disposition_taille_sieges = filtered_df["Quelle taille mesurez-vous?"].value_counts ()

    print ("La disposition de la taille des gens qui pensent qu'il est poli d'incliner son siège est de : " + "" \

           + str (disposition_taille_sieges))





# Origine (emplacement) des personnes qui pensent qu'il est impoli de parler à l'inconnu assis a coté de soi en avion 

def origine_conversation_etranger1 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Est-il impoli de parler dans une conversation a l'etranger a cote de vous ?"] == "Yes  somewhat rude"

    filtered_df = data[df_mask]

    disposition_origine_etranger = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print ("La disposition des emplacements des gens qui pensent qu'il est impoli de parler dans une conversation" \

           + " à l'étranger a coté de vous est "

           + str (disposition_origine_etranger))



# Origine (emplacement) des personnes qui pensent qu'il n'est pas impoli de parler à l'inconnu assis a coté de soi en avion 

def origine_conversation_etranger2 ():

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["Est-il impoli de parler dans une conversation a l'etranger a cote de vous ?"] == "No  not at all rude"

    filtered_df = data[df_mask]

    disposition_origine_etranger = filtered_df["Emplacement (region de recensement)"].value_counts ()

    print ("La disposition des emplacements des gens qui pensent qu'il est poli de parler dans une conversation" \

           + " à l'étranger a coté de vous est "

           + str (disposition_origine_etranger)) 





# Moyenne d'age de ceux qui pensent qu'il est impoli d'amener un enfant en bas age   

def moyenne_age_bebe1 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["En general  est-il impoli d'amener un bebe dans un avion ?"] == "Yes  somewhat rude"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport aux personnes qui pensent qu'il est impoli de ramaner" \

           + " un bébé dans un avions est de : " \

           + str (moyenne_df))



# Moyenne d'age de ceux qui pensnet qu'il n'est pas impoli d'amener un enfant en bas age en avion 
def moyenne_age_bebe2 () :

    data = pd.read_csv (r"D:\lucas\programmation\Lucas\Python2.0/Tableau_source_vf2.txt")

    df_mask = data["En general  est-il impoli d'amener un bebe dans un avion ?"] == "No  not at all rude"

    filtered_df = data[df_mask]

    moyenne_df = filtered_df["Age "].mean ()

    print ("La moyenne d'age par rapport aux personnes qui pensent qu'il est poli de ramaner" \

           + " un bébé dans un avions est de : " \

           + str (moyenne_df))





        

        

















