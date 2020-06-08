import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

# Utilizo json porque si quisiera trabajar con los datos guardados, lo puedo hacer facilmente
# con un load del archivo, que me devuelve la misma estructura que guarde originalmente, en este
# caso, un diccionario.
def x(a,b):
	print(a+b)
def InterfazUsuario():
	layout = [[sg.Text('Usuario: ')],
	          [sg.Input(key='usuario')],
			  [sg.Text('Fecha de hoy:')],
			  [sg.Input(key='fecha')],
			  [sg.Button('Jugar!')]]
	window = sg.Window('Ingrese sus datos', layout)
	while True:
		event,values = window.Read()
		if event == 'Jugar!' and values['usuario'] and values['fecha']: #entra a jugar solo si se llena usuario y fecha con algun valor
			break
		if event == None:
			break

	window.Close()

	return values

def GuardoDatos(jugados) :
	with open("datos_usuario.json", 'a') as archivo:
		json.dump(jugados,archivo)
		archivo.close()


def main(args):	
	datos_jugador = InterfazUsuario()
	lista_juegos = []
	jugados= {} # voy a usar un diccionario que utilice como clave el nombre de usuario.
				# el valor de esta clave va a ser otro diccionario con dos claves: 'juegos' y 'fecha'.
				# juegos contiene una lista con los juegos jugados. 
				# utilice el diccionario de esta forma porque si se quiere agregar mas datos al usuario,
				# se puede hacer facilmente agregando una clave mas, manteniendo una estructura organizada.

	layout = [[sg.Button('Ta-Te-Ti',size = (20,10)), sg.Button('Ahorcado',size = (20,10))],
			  [sg.Button('Otello', size = (20,10)), sg.Button('Salir', size = (20,10))]]

	window = sg.Window('Elegir juego', layout)	

	while True:
		event, values = window.Read()

		if event == 'Ahorcado':
			window.Disappear()
			hangman.main()		
		elif event == 'Ta-Te-Ti':
			window.Disappear()
			tictactoeModificado.main()
		elif event == 'Otello':
			window.Disappear()
			reversegam.main()
		elif event in (None, 'Salir'):
			break
		if not(event in lista_juegos):
		  lista_juegos.append(event) # guardo el juego jugado en la lista.
		window.Reappear()
		print('Puede elegir jugar otro juego o salir en el menu!')

	jugados[datos_jugador['usuario']] = {}
	jugados[datos_jugador['usuario']]['juegos'] = lista_juegos
	jugados[datos_jugador['usuario']]['fecha'] = datos_jugador['fecha']
	print(jugados)
	GuardoDatos(jugados)
	print (x(10,10))
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
