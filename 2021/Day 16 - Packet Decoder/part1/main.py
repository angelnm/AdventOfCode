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
	global total_version
	print()
	print(message)
	version, type_id, message = read_head(message)
	total_version += version
	print('Packet Version [{}] of type [{}]'.format(version, type_id))
	if type_id == 4:
		literal_number, message = read_literal_number(message)
		print('Literal Number [{}]'.format(literal_number))
	else:
		length_type_id, message = read_length_type_id(message)
		print('Length Type ID [{}]'.format(length_type_id))
		if length_type_id == 0:
			total_length, message = read_number(15, message)
			print('Length of SubPacket [{}]'.format(total_length))
			sub_message = message[0:total_length]
			while len(sub_message)!=0:
				sub_message = read_packet(sub_message)
			message = message[total_length:]
		elif length_type_id == 1:
			number_subp, message = read_number(11, message)
			print('Number of Packets [{}]'.format(number_subp))
			for i in range(number_subp):
				message = read_packet(message)
	return message

total_version = 0
if __name__ == '__main__':
	with open('input.txt') as file:
		message = file.read().splitlines()
		message = message[0]
	print(message)
	message = hex2bin(message)
	print(message)

	read_packet(message)
	print(total_version)
