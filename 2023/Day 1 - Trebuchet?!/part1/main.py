with open('input.txt', 'r') as fichero:
	 lines = fichero.read().splitlines()

total = 0
for calibration in lines:
	number = 0

	for character in calibration:
		if character>='0' and character<='9':
			number += (ord(character)-48)*10
			break
	
	for character in calibration[::-1]:
		if character>='0' and character<='9':
			number += (ord(character)-48)
			break

	total += number
print(total)
