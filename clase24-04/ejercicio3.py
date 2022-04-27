#Realizar el juego PIEDRA, PAPEL O TIJERA. El usuario deberá competir contra la PC. 
#El triunfador será quien gane 3 partidas.
import random

ppt = ["piedra", "papel", "tijera"]
puntos_pc = 0
puntos_usuario = 0

while puntos_pc < 3 and puntos_usuario < 3:
	try:
		opcion = str(input("Piedra, papel o tijera?: "))
	except opcion.lower != "piedra" or opcion.lower != "papel" or opcion.lower != "tijera":
		print("Ups, hubo un error. Ingrese de nuevo su opción.")
	
	pc = random.choiche(ppt)

if opcion.lower == pc:
			print("Empataron, va de nuevo.")
	
		
			if opcion.lower == "piedra" and pc == "papel" :
				print(f"Vos elegiste {opcion} y la pc eligió {pc}./nUps, te envolvieron.")
				puntos_pc += 1
			if opcion.lower == "piedra" and pc == "tijera" :
				print(f"Vos elegiste {opcion} y la pc eligió {pc}./nBien! Rompiste la tijera. ")
				puntos_usuario += 1
			if opcion.lower == "papel" and pc == "tijera" :
				print(f"Vos elegiste {opcion} y la pc eligió {pc}./nUps, te cortaron.")
				puntos_pc += 1
			if opcion.lower == "papel" and pc == "piedra" :
				print(f"Vos elegiste {opcion} y la pc eligió {pc}./nBien, envolviste la piedra.")
				puntos_usuario += 1
			if opcion.lower == "tijera" and pc == "piedra" :
				print(f"Vos elegiste {opcion} y la pc eligió {pc}./nUps, te rompieron.")
				puntos_pc += 1
			if opcion.lower == "tijera" and pc == "papel" :
				print(f"Vos elegiste {opcion} y la pc eligió {pc}./nBien, cortaste el papel.")
				puntos_usuario += 1
		while puntos_usuario = 3:
			print("Muy bien, ganaste!")
				break

		while puntos_pc = 3:
			print("Sos de madera, perdiste!")
				break

	vadenuevo = input("Queres jugar de nuevo? si/no")	
	if vadenuevo.lower =! "si":
			break
	