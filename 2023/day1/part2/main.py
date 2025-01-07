with open('input.txt', 'r') as fichero:
	 lines = fichero.read().splitlines()

total = 0
for calibration in lines:
	number = 0

	pos = 0
	while(pos < len(calibration)):
		if calibration[pos:pos+3]=='one':
			character='1'
		elif calibration[pos:pos+3]=='two':
			character='2'
		elif calibration[pos:pos+5]=='three':
			character='3'
		elif calibration[pos:pos+4]=='four':
			character='4'
		elif calibration[pos:pos+4]=='five':
			character='5'
		elif calibration[pos:pos+3]=='six':
			character='6'
		elif calibration[pos:pos+5]=='seven':
			character='7'
		elif calibration[pos:pos+5]=='eight':
			character='8'
		elif calibration[pos:pos+4]=='nine':
			character='9'
		else:
			character = calibration[pos]

		if character>='0' and character<='9':
			number += (ord(character)-48)*10
			break
		pos += 1
	
	pos = len(calibration)-1
	while(pos >=0):
		if calibration[pos:pos+3]=='one':
			character='1'
		elif calibration[pos:pos+3]=='two':
			character='2'
		elif calibration[pos:pos+5]=='three':
			character='3'
		elif calibration[pos:pos+4]=='four':
			character='4'
		elif calibration[pos:pos+4]=='five':
			character='5'
		elif calibration[pos:pos+3]=='six':
			character='6'
		elif calibration[pos:pos+5]=='seven':
			character='7'
		elif calibration[pos:pos+5]=='eight':
			character='8'
		elif calibration[pos:pos+4]=='nine':
			character='9'
		else:
			character = calibration[pos]

		if character>='0' and character<='9':
			number += (ord(character)-48)
			break
		pos -= 1

	total += number
print(total)
