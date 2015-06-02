def decrypt(encrypted):
	midle = len(encrypted) // 2
	encrypted = encrypted[midle:]+encrypted[:midle]
	len_of_alphabet, rest,  len_of_key = encrypted.split('~')
	len_of_key = int(len_of_key)
	len_of_alphabet = int(len_of_alphabet)
	alphabet = rest[:len_of_alphabet]
	key = rest[-len_of_key:]
	encrypted_message = rest[len_of_alphabet:-len_of_key]
	dic_alphabet = dict(zip(alphabet, range(len(alphabet))))
	idx_of_encrypted = [dic_alphabet[i] for i in encrypted_message]
	idx_of_key = [dic_alphabet[i] for i in key]
	idx_of_encrypted = [(idx_of_encrypted[i] - idx_of_key[i%len_of_key]+len_of_alphabet)%len_of_alphabet  for i in range(len(idx_of_encrypted))] 
	message = ""
	message = message.join([alphabet[x] for x in idx_of_encrypted])
	return message

if __name__ == "__main__":
	message = input()
	print(decrypt(message))