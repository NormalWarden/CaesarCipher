string = list(input("Enter the line: ").lower())
solve = input("Decode or Encode? D/E: ").upper()

def decode(string):
	print('Variants of the decoding:\n')
	string1 = []
	for i in  range(0, 26):
		for j in range(len(string)):
			if string[j] == ' ':
				string1.append(' ')
			elif ord(string[j]) - i < 97:
				string1.append(chr(ord(string[j]) - i + 26))
			else:
				string1.append(chr(ord(string[j]) - i))
		print(''.join(string1))
		string1.clear()

def encode(string):
	key = int(input("Enter the key (0-25): "))

	if key >= 26 or key < 0:
		print("Invalid key")
		exit()

	for i in range(len(string)):
		if string[i] == ' ':
			pass
		elif ord(string[i]) + key > 122:
			string[i] = chr(ord(string[i]) + key - 26)
		else:
			string[i] = chr(ord(string[i]) + key)

	print("Ciphertext: " + ''.join(string))


if solve == 'D':
	decode(string)
elif solve == 'E':
	encode(string)