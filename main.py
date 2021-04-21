from text_functions import greeting, get_answer
from database import init_database, execute_query

good = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sad = [10, 11, 12, 13, 14, 15, 16, 17, 18]
angry = [19, 20, 21, 22, 23, 24, 25, 26, 27]
states = {"current":None, "previous":None}

def check_state(message):
	result = ""
	try:
		message = int(message)
		if message in good:
			result = "good"
		elif message in sad:
			result = "sad"
		elif message in angry:
			result = "angry"
		else:
			result = "undefined"
	except:
		result = "undefined"
	return (result)

def conversation():
	message = input("")
	states['previous'] = states['current']
	states['current'] = check_state(message)
	get_answer(states)
	conversation()

def start_conversation():
	message = input("")
	states['current'] = check_state(message)
	connection = init_database()
	greeting(states)
	conversation()

if __name__ == '__main__':
	start_conversation()