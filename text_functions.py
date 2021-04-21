def greeting(states):
	state = states['current']
	if state == 'good':
		print("Привет! Мне нравится, когда ты в хорошем настроении ;)")
	if state == 'sad':
		print("Привет! Ты сегодня не в духе. Расскажешь?")
	if state == 'angry':
		print("Привет! Я вижу, ты злишься. Можешь помолчать минуту, если не хочешь разговаривать, я не буду писать")
	if state == 'undefined':
		print("Привет. Попробуй написать что-нибудь ещё, я не понял!")

def get_answer(states):
	state = states['current']
	state_previous = states['previous']
	if state == 'good':
		if state_previous == 'good':
			print("Всегда радуюсь, когда ты в порядке! :)")
		if state_previous == 'sad':
			print("Я рад, что тебе лучше!")
		if state_previous == 'angry':
			print("Ты молодец, что так легко справляешься с негативом!")
		elif state_previous == 'undefined':
			print("Мы нашли общий язык! Ура!")

	if state == 'sad':
		if state_previous == 'good':
			print("Что тебя расстроило?")
		elif state_previous == 'sad':
			print("Можешь поделиться своими проблемами со мной, я поддержу!")
		elif state_previous == 'angry':
			print("Тебе уже лучше! Ты молодец!")
		elif state_previous == 'undefined':
			print("Ты молодец! Вот мы и снова говорим на понятном нам языке :)")

	if state == 'angry':
		if state_previous == 'good':
			print("Скажи мне, кто тебя разозлил и мы вместе разберёмся с ним!")
		elif state_previous == 'sad':
			print("Что случилось, почему тебе стало хуже?")
		elif state_previous == 'angry':
			print("Давай я помогу тебе справиться со злостью?")
		elif state_previous == 'undefined':
			print("Я тебя понял, не злись, пожалуйста")
	
	if state == 'undefined':
		if state_previous == 'undefined':
			print("Я ещё не освоил этот сложный язык, попробуй ещё раз!")
		elif state_previous == 'good':
			print("Прости, но я пока не умею обрабатывать такие сложные предложения :(")
		elif state_previous == 'sad':
			print("Можешь повторить ещё раз, а я постараюсь помочь?")
		elif state_previous == 'angry':
			print("Мне пока тяжело полностью осознать, что ты хочешь сказать, но я правда стараюсь!")