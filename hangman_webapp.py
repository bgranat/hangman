"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
		 'word_so_far':"_ _ _ _ _ _ _ _ _ _ _",
		 'numcorrect': 0,
		 'guessesleft': 6,
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word()
	state['word_so_far'] = hangman_app.dashed_word(state['word'], [])
	state['guesses'] = []
	state['guessesleft'] = 6
	state['numcorrect'] = 0
	state['done'] = False
	state['response'] = ""
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		if not state['done']:
			letter = request.form['guess'].lower()
			# check if letter has already been guessed
			# and generate a response to guess again
			if letter in state['guesses']:
				state['response'] = f"{letter} has already been guessed!\nPlease guess again."
			elif letter in state['word']:
				state['numcorrect'] += 1
				state['response'] = f"{letter} is in the word!"
				state['guesses'].append(letter)
				if state['numcorrect'] == len(set(state['word'])):
					state['response'] = '\nYou won!'
					state['done'] = True
			else:
				state['response'] = f"{letter} is not in the word."
				state['guesses'].append(letter)
				state['guessesleft'] -= 1
				if state['guessesleft'] == 0:
					state['response'] = f"You lost! The word was {state['word']}."
					state['done'] = True
			state['word_so_far'] = hangman_app.dashed_word(state['word'], state['guesses'])
		
		return render_template('play.html',state=state)

@app.route('/about',methods=['GET'])
def about():
	return render_template('about.html', state=state)


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
