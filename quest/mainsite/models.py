from django.db import models

class Letter(models.Model):
    letter = models.CharField(max_length=1)

    def __str__(self):
        return self.letter

class Puzzle(models.Model):
    puzzle_id = models.IntegerField()
    text = models.TextField()
    answer = models.CharField(max_length=12)
    letter = models.ForeignKey(
        Letter,
        related_name="puzzle",
        on_delete=models.CASCADE
    )
    tip = models.TextField(null=True)
    tip_this = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.puzzle_id)

class Team(models.Model):
    session = models.TextField()
    letters = models.ManyToManyField(
        Letter,
        related_name="team",
    )
    position = models.IntegerField()

    def __str__(self):
        return self.session