import qiskit, pyfiglet,random

qiskit.IBMQ.load_accounts()
backend = qiskit.providers.ibmq.least_busy(qiskit.IBMQ.backends(simulator=False))

num = 3
qr = qiskit.QuantumRegister(num)
cr = qiskit.ClassicalRegister(num)

checkStatus = True

myList = ['Jorah', 'Death', 'Jon Snow', 'Love', 'White Walkers'];
humanScore = 0
robotScore = 0

asciiBanner = pyfiglet.figlet_format("Game Of Thrones")
asciiBanner2 = pyfiglet.figlet_format("Duel")
print(asciiBanner)
print(asciiBanner2)
#print("So You Want To Play the Game of Thrones Duel!\n");
print("**************Beware There are Spoilers Ahead!***************\n")
print("You Will Be Facing Off Against A Quantum Robot in NY.\n\n")
print("Here Are The Instructions:")
print("Jon Snow *Beats* Death")
print("Death *Caught Up To* Jorah")
print("Jorah *Killed* White Walkers")
print("White Walkers *DISINTEGRATES* Love")
print("Love *Fogs Up* Jon Snow")
print("Jon Snow *Decapitated* White Walkers")
print("White Walker *IS* Death")
print("Death *Destroys* Love")
print("Love *Dodged* Jorah")
print("Jorah *Disproves of* Jon Snow\n")
print("\nLoading...")
def getName(value):
	return myList[value]

def getNum(name):
	if name in myList:
		return myList.index(name)
	else:
		print(name + " Is Not Available in This Duel.\n")
	return -1

def getChoice():
	superposition = qiskit.QuantumCircuit(qr,cr)
	superposition.h(qr)
	superposition.s(qr[0])
	superposition.measure(qr[0], cr[0])
	superposition.measure(qr[1], cr[1])
	superposition.measure(qr[2], cr[2])
	#Used to run real test with Quantum Comp in NY
	#job = qiskit.execute(superposition, backend,seed_simulator=random.randint(1,100), shots=1000, max_credits=5)
	#**Used for Testing: Runs on Simulator**
	job = qiskit.execute(superposition, qiskit.BasicAer.get_backend('qasm_simulator'),seed_simulator=(random.randint(1,100)), shots=1000, max_credits=5)
	tempValue = job.result().get_counts()
	robotAns = max(tempValue, key=tempValue.get)
	listMap = {'101': myList[0], '010': myList[1], '110': myList[2], '001': myList[3], '011': myList[4], '111': myList[0], '100': myList[1], '000': myList[2]}
	return listMap[robotAns]

def duel(guess):
	global humanScore, robotScore
	humanValue = getNum(guess)
	robotValue = getNum(getChoice())
	endGame = (5 + humanValue - robotValue) % 5
	robotChoice = getName(robotValue)
	print("\nHuman Chooses: " + guess)
	print("Quantom Robot Chooses: " + robotChoice +"\n")
	if humanValue == -1:
		print("**Quantum Robot Wins!**\n")
		robotScore += 1
	elif endGame == 0:
		print("**Human and Quantum Robot Ties**\n")
	elif endGame == 1 or endGame == 3:
		print("**Human Wins!**\n")
		humanScore += 1
	elif endGame == 2 or endGame == 4:
		print("**Quantum Robot wins!**\n")
		robotScore += 1
	print("Current Score ---  Human: "+str(humanScore)+" vs. Quantum Robot: " + str(robotScore) )

input("Hit Enter to Enter the Duel")

while (checkStatus):
	choice = input('What is your Pick?\nYour Options Are: Jon Snow, Death, Jorah, White Walkers, Love , or quit to quit\n')
	if str(choice) == "quit":
		checkStatus = False
		print("Quiting..\n")
	else:
		duel(str(choice))
