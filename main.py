import os

DATA_DIRECTORY = 'data'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_twitter_keys():
	consumer_key = raw_input('\nPlease enter consumer key: ')
	consumer_secret = raw_input('Please enter consumer secret: ')
	access_token = raw_input('Please enter access token: ')
	access_token_secret = raw_input('Please enter access token secret: ')
	key_file = open('keys.txt','w')
	key_file.write(consumer_key + ',' + consumer_secret + ',' + access_token + ',' + access_token_secret)
	key_file.close()
	print bcolors.OKGREEN + "\n[1] Message: Keys are saved.\n" + bcolors.ENDC
	
def main_screen():
	print('1. Enter twitter keys')
	print('2. Make a profile')
	print('3. Select a profile')
	print('4. Grab tweets')
	print('5. Live graph')
	print('6. Word cloud')
	print('7. Exit')
	choice = raw_input('Enter your choice: ')
	if choice == '1':
		get_twitter_keys()
	if choice == '7':
		quit()

if os.path.exists(DATA_DIRECTORY) == False:
	os.makedirs(DATA_DIRECTORY)
while True:
	main_screen()
