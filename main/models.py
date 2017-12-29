from django.db import models

# Create your models here.


class Exam(models.Model):
	timestamp = models.DateField(auto_now=False)


class QuestionInstruction(models.Model):
	instruction = models.TextField()

	def __str__(self):
		return self.instruction[:30]


class QuestionParagaraph(models.Model):
	paragraph = models.TextField()

	def __str__(self):
		return self.paragraph[:30]


class Sentence(models.Model):
	exam= models.ForeignKey(Exam, on_delete=models.CASCADE)

	questionNumber = models.PositiveSmallIntegerField(default=0)

	answer = models.CharField(max_length=1, 
		choices = (('A','A'),('B','B'),('C','C'),
			('D','D'),('E','E')),
		default='A',
		)

	question = models.TextField()

	instruction = models.ForeignKey(QuestionInstruction, models.SET_NULL,
		blank=True, null=True)
	paragraph = models.ForeignKey(QuestionParagaraph, models.SET_NULL,
		blank=True, null=True)


	def __str__(self):
		return str(self.questionNumber)


class AnswerSelection(models.Model):
	answer = models.CharField(max_length=200)
	choice = models.CharField(max_length=1, 
		choices = (('A','A'),('B','B'),('C','C'),
			('D','D'),('E','E')),
		default='A',
		)

	question = models.ForeignKey(Sentence, on_delete=models.CASCADE)

	def __str__(self):
		return self.choice+') '+self.answer





