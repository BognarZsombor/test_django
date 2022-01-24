import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    end_date = models.DateTimeField('ending date', default=timezone.now)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Status of Question',
    )

    def total_votes(self):
        return sum(self.choice_set.all())

    def status(self):
        now = timezone.now()
        if (self.end_date - now).days == 0:
            return "Ending today"
        elif (now - self.pub_date).days == 0:
            return "Added today"
        elif (self.end_date - now).days < 10:
            return "Ending soon"
        elif (now - self.pub_date).days > -10:
            return "Added recently"
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __radd__(self, other):
        return self.votes + other
