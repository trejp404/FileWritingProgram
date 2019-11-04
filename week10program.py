# Prepedigna Trejo
# Assignment 10.1

import os #imports OS library
import time #imports time

# print() for cleaner output
print()
# welcome message
print("---Welcome---")
# print() for cleaner output
print()
# sleep for 2 seconds
time.sleep(2)
print("---To create and store a new file, follow the directions below.---")
# print() for cleaner output
print()
# sleep for 2 seconds
time.sleep(2)

flag1 = 0
# targeted statement (directoryName) will be executed repeatedly as long as the given condition is true
while flag1 == 0:
	# Ask user for directory name
	directoryName = input("Please enter the name of the directory where you would like to save your \nfile (Ex:'/Users/Alice/Desktop/python_work/'): ")
	# print() for cleaner output
	print()
	print("Verifying directory exists...")
	# sleep for 2 seconds
	time.sleep(2)
	# print() for cleaner output
	print()
	# if directory exists program will then ask user for file name
	if os.path.isdir(directoryName):
		flag1 = 1
		print("Success! Directory found.")
	# loop iterates if directory is not found
	else:
		flag1 = 0
		print("Oops...that directory does not exist. ")

# print() for cleaner output
print()
# sleep for 2 seconds
time.sleep(2)
# user inputs their preferred file name
fileName = input("Please enter the name of your file (Ex: test.txt): ")
# print() for cleaner output
print()
# user inputs their name
name = input ("Please enter your name (Ex: Alice): ")
# print() for cleaner output
print()
# user inputs their address
address = input( "Please enter your home address (Ex: 111 Home Ave): ")
# print() for cleaner output
print()
# user inputs their phone number
phone = input ("Please enter your phone number (Ex: 123-456-7890): ")

# main program
def main():
	try:
		# open file for writing
		with open(fileName, 'w') as fileHandle:
			# write data to file
			fileHandle.write(name + ","  + address + ","  + phone)
			# print() for cleaner output
			print()
			# sleep for 2 seconds
			time.sleep(2)
			# confirmation statement that file was saved and stored in requested directory
			print("Success! The file, "+ fileName + ", is now stored in the requested directory.")
	except:
		# Handle unexpected error
		print("Oops...we seem to have run into a problem while attempting to store the file in the requested directory.")

	try:
		# print() for cleaner output
		print()
		# sleep for 3 seconds
		time.sleep(3)
		print("Loading file contents...")
		# print() for cleaner output
		print()
		# sleep for 3 seconds
		time.sleep(3)
		# open file for reading
		with open(fileName, 'r') as fileHandle:
			# read data from file
			data = fileHandle.read()
		# prints data saved to file
		print(data)
		# print() for cleaner output
		print()
	except:
		# Handle unexpected error
		print("Oops...we seem to have run into a problem while trying to read the stored file.")
main()