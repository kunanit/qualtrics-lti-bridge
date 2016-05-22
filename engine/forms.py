from django import forms
from .models import *

# class SelectQualtricsForm(forms.Form):
# 	qualtrics_url = forms.CharField(label='Qualtrics URL', max_length=100)

class QualtricsUrlQuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ['name','url']

class QuizForm(forms.ModelForm):
	'''
	Create new Quiz
	Used in "create_quiz" view
	'''
	use_qualtrics = forms.BooleanField(required=False)
	class Meta:
		model = Quiz
		fields = ['name']

class QuestionForm(forms.ModelForm):
	'''
	Create new Question
	Used in "create_quiz" view
	'''
	class Meta:
		model = Question
		fields = ['text']

class AnswerForm(forms.ModelForm):
	'''
	Create new explanation
	Used in "create_quiz" view
	'''
	class Meta:
		model = Answer
		fields = ['text', 'correct', 'order']


class ExplanationForm(forms.ModelForm):
	'''
	Create new explanation
	Used in "create_quiz" view
	'''
	class Meta:
		model = Explanation
		fields = ['text']

class SelectQuizForm(forms.Form):
	'''
	Select existing quiz for embedding
	'''
	quiz = forms.ModelChoiceField(queryset=Quiz.objects.all())

