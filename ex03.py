import socket
import sys


HOST = sys.argv[1]
PORTmin = sys.argv[2]
portOuvert = []
portFerme = []
PORT = []

if len(sys.argv) == 4:
	try:
		PORTmax = int(sys.argv[3])
	except:
		print("[-] Port invalide")

try:
	PORTmin = int(PORTmin)
	if len(sys.argv) == 4:
		for n in range(PORTmin, PORTmax):
			PORT.append(n)
			n += 1
	else:
		PORT.append(PORTmin)
except ValueError:
	print("[-] Port invalide")

i = 0
while i < len(PORT[:]):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as e:
		print("[-] Une erreur est survenue lors de la creation du socket ! {}".format(e))
		sys.exit()

	try:
		scan = sock.connect_ex((HOST, PORT[i]))
		if scan == 0:
			sock.shutdown(socket.SHUT_RDWR)
			sock.close()
			portOuvert.append(PORT[i])
		else:
			portFerme.append(PORT[i])
		i += 1
	except socket.gaierror as e:
		print("[-] Erreur d'adresse de connexion au serveur: {}".format(e))
		sys.exit()
	except socket.error as e:
		print("[-] Erreur de connexion : {}".format(e))
		sys.exit()

if len(portOuvert) == 0:
	print("[-] Tous les ports sont fermes !")
else:
	for port in portOuvert:
		print("[+] Port {} ouvert".format(port))
	for port in portFerme:
		print("[-] Port {} ferme".format(port))



