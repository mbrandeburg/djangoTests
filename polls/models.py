from django.db import models

# Create your models here.

# you can link models together, can have parent and child models, its OOP for your application
# i.e., a polls app will require what? a question and choices.

# Question:
# Question_text
# Publish_date

# Choice:
# Choice_text
# Number_of_votes
# Link #need to link your choices to the right questions

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # now we give choice class a new parameter - pass in question, has to be a foreign key of this q object and on delete, intiiatlize cascade (for 1 to 1 relationship)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
