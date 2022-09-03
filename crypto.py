import os
import cryptocode

# Constants
file_name = 'file.txt'
decrypt_file_name = 'decrypt_file.txt'
key = '$$_sucessful_$$'

# Registration
if not os.path.isfile(file_name):
	try:
		while True:
			password = input('Create password: ')
			if password == input('Retype password: '):
				break
			else:
				print('Passwords is not same!\n')
	except KeyboardInterrupt:
		print('Password creation canceled!\n')
		exit(1)

	file = open(file_name, 'w')
	file.write(cryptocode.encrypt(key, password))
	file.close()

	print('Sucessful')

# Body
else:
	# Reading encrypted key
	file = open(file_name, 'r')
	encrypted_key = file.read()
	file.close()

	# Getting password from user and match keys
	try:
		while True:
			password = input('Password: ')
			if cryptocode.decrypt(encrypted_key, password) == False:
				print('Wrong password!\n')
			else:
				print('Succesful\n')
				break
	except KeyboardInterrupt:
		exit(1)

	# Decrypting file
	file = open(file_name, 'r')
	encrypted_info = file.read()
	decrypted_info = cryptocode.decrypt(encrypted_info, password)

	# Writing decrypted file
	decrypt_file = open(decrypt_file_name, 'w')
	decrypt_file.write(decrypted_info)
	decrypt_file.close()

	# Instructions waiting
	while True:
		try:
			instruction = input('>>> ').lower()
		
		except KeyboardInterrupt:
			decrypt_file = open(decrypt_file_name, 'r')
			encrypted_info = cryptocode.encrypt(decrypt_file.read(), password)

			file = open(file_name, 'w')
			file.write(encrypted_info)
			file.close()

			os.remove(decrypt_file_name)

			break

		else:
			if instruction == 'help':
				print('Instructions:',
					'help      - view this page;',
					'exit (^C) - exit with appling changes from decoded file to encoded and delete decoded;',
					'zexit     - exit without appling changes;',
					'passwd    - change password;',
					'reset     - delete decoded and encoded files. WARNING: Your data will lost!',
					sep='\n', end='\n\n')

			elif instruction == 'exit':
				decrypt_file = open(decrypt_file_name, 'r')
				decrypted_info = decrypt_file.read()
				encrypted_info = cryptocode.encrypt(decrypted_info, password)

				file = open(file_name, 'w')
				file.write(encrypted_info)
				file.close()

				os.remove(decrypt_file_name)

				break

			elif instruction == 'zexit':
				os.remove(decrypt_file_name)
				
				break

			elif instruction == 'passwd':
				try:
					while True:
						new_password = input('Create password: ')
						if new_password == input('Retype password: '):
							password = new_password
							print('Password changed Sucessfully')
							break
						else:
							print('Passwords is not same!\n')
				except KeyboardInterrupt:
					print('Password changing canceled!\n')

			elif instruction == 'reset':
				try:
					if not input('Type \'yes\' to continue: ') == 'yes':
						print('Reset canceled!\n')
					else:
						os.remove(file_name)
						os.remove(decrypt_file_name)

						break
				except KeyboardInterrupt:
					print('Reset canceled!\n')

			else:
				print(f'Instuction named \n{instruction}\n is not exists!')

exit(0)
