import random
from polls.question_generators.tools import *
def discrete_or_continuous():
	data = {'continuous':[' the height of buildings', " peoples weight", ' the temperature of a cup of tea', ' the time spent waiting in line at Alton Towers', ' the amount of liquid in different cans of coke', ' the price of a drink', ' the speed of different cars', ' the amount of carpet needed for a house'],
			'discrete':[' how old people are', ' what shoe size people are', ' the number shown when rolling a dice', ' the number of likes on an Instagram post', ' the number of votes in an election', ' students marks on a test']}


	question = random.choice(data['continuous'] + data['discrete'])

	if question in data['continuous']:
		answer = 'Continuous'
	else:
		answer = 'Discrete'


	question = name_chooser() + ' is collecting data on ' + question + '.\nIs this discrete or continuous data?'

	return question, answer

def qual_or_quant():
	data = {'qualitative':[' the colour of your favourite mug ', ' a persons favourite band ', ' a persons gender ', ' the names of pets ', ' what someone thought of their Amazon purchase ', ' a persons religion ', ' the native language of a country ', ' a persons eye colour '],
			'quantitative':[' height of a building ', " a person's weight ", ' the temperature of a cup of tea ', ' time spent waiting in line at Alton Towers ', ' the amount of liquid in a can of coke ', ' the price of a drink ', ' the speed of a car ', ' the amount of carpet needed for a house ']}


	question = random.choice(data['qualitative'] + data['quantitative'])

	if question in data['qualitative']:
		answer = 'Qualitative'
	else:
		answer = 'Quantitative'


	question = 'Is ' + question + ' qualitative or quanitative data?'

	return question, answer