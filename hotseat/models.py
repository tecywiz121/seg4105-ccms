from django.db import models
from random import choice
import string


def generate_password(size=5, chars=string.digits):
    return ''.join(choice(chars) for x in range(size))


class Terminal(models.Model):
    """A computer terminal at which a person may be assigned."""
    name = models.CharField(max_length=255, primary_key=True)

    @property
    def is_available(self):
        return not self.assignments.filter(active=True).exists()

    def assign(self):
        assignment = Assignment()
        assignment.password = generate_password()
        assignment.terminal = self
        return assignment

class Assignment(models.Model):
    """Stores the information related to a client."""
    password = models.CharField(max_length=10)      # TODO: Encrypt this
    terminal = models.ForeignKey(Terminal, related_name='assignments')
    active = models.BooleanField(default=True)
    time_remaining = models.IntegerField()
