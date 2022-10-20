jpv= 10
jatq = 3
jdef = 2

jpv_max = 10

epv = 10
eatq = 2
edef = 0

epv_max = 10

tour = 1


def ecran_m():
	print("*====*======*====*")
	print("   °Bienvenue!°   ")
	print("voulez vous jouer?")
	print("*====*======*====*")
	print("   1.oui 2.non    ")

def ecran_m2():
	print("*======*===========*======*")
	print(" choisissez le mode de jeu")
	print("      1.Histoire(wip)")
	print("        2.infini")
	print("        3.quitter")
	print("*======*===========*======*")


def ecran_c():
	print("*=======================*")
	print("      round n°: "+str(tour))
	print("")
	print("      pv ennemi: "+str(epv))
	print("")
	print("      pv joueur: "+str(jpv))
	print(" * 1.attaque    2.soin *")
	print("*=======================*")

def ecran_i():
	print("*=================*===============================*=================*")
	print("                    Bienvenue dans le mode infini")
	print("")
	print(" Veuillez selectionner le nombre de combat que vous souhaiter faire.")
	print("       Attention à toi tu ne sera pas soigné entre les combat.")
	print("")
	print("*=================*===============================*=================*")



def combat():
	global jpv, jatq, jdef, epv, eatq, edef, tour
	while jpv > 0 and epv > 0:
		res=str(input())
		if res == "1" and "attaque":
			epv-= jatq
			jpv-= eatq
		elif res == "2" and "soin":
			jpv+= 5
			jpv-= eatq
		tour+= 1
		ecran_c()


def menu1():
	res=input() 
	if res == "1" or res == "oui":
		menu2()
	elif res == "2" or res == "non":
		print("bye bye")

	else:
		print("erreur: reponse non valide")
		menu1()

def menu2():
	ecran_m2()
	res=input()
	if res == "1":
		print("encore en travaux")
		menu2()
	elif res == "2":
		infini()
		menu2()
	elif res == "3":
		print("A la prochaine fois!")
	else:
		print("choix incomprie veuiller reéssayer")
		menu2()

def infini():
	global epv_max, epv, jpv_max, jpv
	ecran_i()
	res= int(input())
	jpv = jpv_max
	for loop in range(res):
		ecran_c()
		combat()
		epv = epv_max

def histoire():
	pass


def main():
	ecran_m()
	menu1()	
		
main()