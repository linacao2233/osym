# functions to call for file processing
from .models import *

import re

def readfile(filename):
	file = open(filename,'r')

	
def parseQuestions(questions,exam):
	"""
	parse the input question to questions
	input: 
	questions:  string
	"""

	pattern = re.compile(r'([0-9]+)\.')

	questions = re.split(pattern,questions)

	#  get the instruction part 

	instruction = questions[0]

	instruction = re.sub(r'-\n','',instruction)

	instruction = instruction.strip().split('\n\n')
	if len(instruction)>1:
		questionparagraph = QuestionParagaraph(paragraph=instruction[1])
		questionparagraph.save()
	else:
		questionparagraph = False

	questioninstruction, created = QuestionInstruction.objects.get_or_create(
		instruction=instruction[0])

	if created:
		questioninstruction.save()

#   parse single questions
	i = 1
	while i<len(questions)-1:
		if re.match(r'[0-9]+', questions[i]):
			number = int(questions[i])
			sentence = questions[i+1]
			parseSentences(sentence, exam,number,questioninstruction, questionparagraph)
		i = i+1


def parseSentences(sentence, exam,number, instruction,paragraph):
	"""
	parse the input sentence to save to the database
	input:
	sentence: string
	instruction: QestionInstruction, instruction for the question
	paragraph: Qestionparagraph or False
	if False, no paragraph
	"""

	pattern = re.compile(r'\n\n[A-E]\)')

	splitted = re.split(pattern,sentence)

	if paragraph:
		sentencetosave,created = Sentence.objects.get_or_create(exam=exam,
		questionNumber=number,
		question=re.sub(r'\n','',splitted[0]),
		instruction=instruction,
		paragraph=paragraph
			)
		if created:
			sentencetosave.save()
	else:
		sentencetosave,created = Sentence.objects.get_or_create(exam=exam,
		questionNumber=number,
		question=re.sub(r'\n','',splitted[0]),
		instruction=instruction,
			)
		if created:
			sentencetosave.save()		



