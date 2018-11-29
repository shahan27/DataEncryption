# Assignment Ceasar Cipher (Shahan Rahman) Afternoon 113 Class
from random import randint
#Encrypting Phase
with open('text.txt', 'r') as file:
    text=file.read()

alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = ""
two_Letters = "The special characters are "
key= randint(-1, 25)
special_char = randint(0, 25)
two_Letters += cap_Alphabet[special_char] + alphabet[special_char]
key_Str = "and the key is " + str(key)
for c in text:
	if ((c in alphabet) and (c in alphabet[special_char])):
		cipher+=alphabet[special_char]+"^"
	if (c in alphabet) and (c not in alphabet[special_char]):
		cipher+=alphabet[(alphabet.index(c)+key)%(len(alphabet))]	
	if (c in cap_Alphabet) and (c in cap_Alphabet[special_char]):
		cipher+=cap_Alphabet[special_char]+"^"
	if (c in cap_Alphabet) and (c not in cap_Alphabet[special_char]):
		cipher+=cap_Alphabet[(cap_Alphabet.index(c)+key)%(len(cap_Alphabet))]
	if (c not in alphabet) and (c not in cap_Alphabet):
		cipher+=c
key_file = open("key_text.txt", "w")
print(two_Letters, key_Str, file = key_file, flush = True)
encryptic_file = open("encrytic_text.txt", "w")
print(cipher, file = encryptic_file, flush = True)

#Decryption phase
with open('encrytic_text.txt', 'r') as textEn:
    read_textEn=textEn.read()
with open('key_text.txt', 'r') as keyEn:
    read_keyEn=keyEn.read()
if((read_keyEn[45].isdigit()) and read_keyEn[46].isdigit()):
	key_Code = read_keyEn[45] + read_keyEn[46]
	key_Code = int(key_Code)
else:
	key_Code = read_keyEn[45]
	key_Code = int(key_Code)
decipher = ""
i = 0
def decrypt(a):
	if(a == a.upper()):
		return cap_Alphabet[(cap_Alphabet.index(a)-key_Code)%(len(cap_Alphabet))]
	else:
		return alphabet[(alphabet.index(a)-key_Code)%(len(alphabet))]	

while(i<len(read_textEn)):

	if ((read_textEn[i] in alphabet) and (read_textEn[i+1] == "^")):
		decipher+=read_textEn[i]
	if ((read_textEn[i] in alphabet) and (read_textEn[i+1] != "^")):
		decipher+=decrypt(read_textEn[i])
	if ((read_textEn[i] in cap_Alphabet) and (read_textEn[i+1] == "^")):
		decipher+=read_textEn[i]
	if((read_textEn[i] in cap_Alphabet) and (read_textEn[i+1] != "^")):
		decipher+=decrypt(read_textEn[i])
	if ((read_textEn[i] not in alphabet) and (read_textEn[i] not in cap_Alphabet) and (read_textEn[i] == "^")):
		decipher+=""
	if ((read_textEn[i] not in alphabet) and (read_textEn[i] not in cap_Alphabet) and (read_textEn[i] != "^")):
		decipher+=read_textEn[i]
	i+=1
#print (special_rev + " " + reverse_key)
decryption_file = open("decryption_text.txt", "w")
print(decipher, file = decryption_file, flush = True)