def hex2bin(value):
	number = ''
	for val in value:
		if val=='0':
			number+='0000'
		elif val=='1':
			number+='0001'
		elif val=='2':
			number+='0010'
		elif val=='3':
			number+='0011'
		elif val=='4':
			number+='0100'
		elif val=='5':
			number+='0101'
		elif val=='6':
			number+='0110'
		elif val=='7':
			number+='0111'
		elif val=='8':
			number+='1000'
		elif val=='9':
			number+='1001'
		elif val=='A':
			number+='1010'
		elif val=='B':
			number+='1011'
		elif val=='C':
			number+='1100'
		elif val=='D':
			number+='1101'
		elif val=='E':
			number+='1110'
		elif val=='F':
			number+='1111'
	return number

def read_head(message):
	version = message[0:3]
	version = int(version,2)
	type_id = message[3:6]
	type_id = int(type_id,2)
	return version, type_id, message[6:]

def read_length_type_id(message):
	length_type_id = message[0:1]
	length_type_id = int(length_type_id,2)
	return length_type_id, message[1:]

def read_number(length, message):
	number = message[0:length]
	number = int(number, 2)
	return number, message[length:]

def read_literal_number(message):
	number = ''
	while message[0]!='0':
		number += message[1:5]
		message = message[5:]
	number += message[1:5]
	message = message[5:]
	return int(number, 2), message

def read_packet(message):
	literal_number = 0

	version, type_id, message = read_head(message)
	if type_id == 4:
		literal_number, message = read_literal_number(message)
	else:
		length_type_id, message = read_length_type_id(message)
		list_numbers = []
		if length_type_id == 0:
			total_length, message = read_number(15, message)
			sub_message = message[0:total_length]
			while len(sub_message)!=0:
				number, sub_message = read_packet(sub_message)
				list_numbers.append(number)
			message = message[total_length:]
		elif length_type_id == 1:
			number_subp, message = read_number(11, message)
			for i in range(number_subp):
				number, message = read_packet(message)
				list_numbers.append(number)

		if type_id==0:
			for n in list_numbers:
				literal_number += n
		elif type_id==1:
			number=1
			for n in list_numbers:
				number*=n
			literal_number=number
		elif type_id==2:
			list_numbers.sort()
			literal_number=list_numbers[0]
		elif type_id==3:
			list_numbers.sort()
			literal_number=list_numbers[-1]
		elif type_id==5:
			literal_number=0
			if list_numbers[0]>list_numbers[1]:
				literal_number=1
		elif type_id==6:
			literal_number=0
			if list_numbers[0]<list_numbers[1]:
				literal_number=1
		elif type_id==7:
			literal_number=0
			if list_numbers[0]==list_numbers[1]:
				literal_number=1

	return literal_number, message

if __name__ == '__main__':
	with open('input.txt') as file:
		message = file.read().splitlines()
		message = message[0]
	message = hex2bin(message)
	number, message = read_packet(message)
	print(number)
