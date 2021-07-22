print("Press 1 to play sudoko and press 2 to play SpaceInvader, Press E to exit")
while True:
	a = input()
	if a == '1':
		exec(open('sudoko.py').read())
	elif a=='2':
		exec(open('SpaceInvader.py').read())
	elif a=='E':
		break
	else:
		print("Invalid Input")
		print("Press 1 to play sudoko and press 2 to play SpaceInvader, Press E to exit")