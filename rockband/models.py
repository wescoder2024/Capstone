from django.db import models

# Create your models here.
class Post(models.Model):
    # Default behaviour - Django creates primary keys for you
    """This class describes all properties and methods of each blog post object"""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    body = models.TextField()
    signature = models.CharField(max_length=140, default = "Wesley")
    date = models.DateTimeField()

def __str__(self):
    return self.title

class Question(models.Model):
    """This class shows each question with a corresponding publishing date """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """This class show each each question with a list of corresponding choices"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text