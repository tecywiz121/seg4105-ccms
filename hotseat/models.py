from django.db import models
from random import choice
import string
from datetime import datetime

def generate_password(size=5, chars=string.digits):
    """Generates a random string of size characters from the list chars"""
    return ''.join(choice(chars) for x in range(size)) # TODO: Make secure with better random (os.urandom)


class Terminal(models.Model):
    """A computer terminal at which a person may be assigned."""
    name = models.CharField(max_length=255, primary_key=True)

    @property
    def is_available(self):
        return not self.assignments.filter(active=True).exists()

    @property
    def current_assignment(self):
        return self.assignments.get(active=True)

    def assign(self):
        assignment = Assignment()
        assignment.password = generate_password()
        assignment.terminal = self
        assignment.generate_token()
        return assignment

    def check_password(self, other_password):
        test = 0
        my_password = self.current_assignment.password
        for mine, other in zip(my_password, other_password):
            test |= ord(mine) ^ ord(other)
        return not test

    def __unicode__(self):
        return self.name

class Assignment(models.Model):
    """Stores the information related to a client."""
    password = models.CharField(max_length=10,
                                blank=True,
                                default=generate_password)      # TODO: Encrypt this

    terminal = models.ForeignKey(Terminal, related_name='assignments')
    active = models.BooleanField(default=True)

    keepalive_token = models.CharField(max_length=10,
                                       blank=True,
                                       default=lambda: generate_password(10, string.ascii_letters + string.digits))

    keepalive_last = models.IntegerField()

    time_remaining = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True, default=datetime.now)
    last_updated = models.DateTimeField(auto_now=True, default=datetime.now)

    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def keepalive(self, token, timestamp):
        if token == self.keepalive_token:
            delta_t = timestamp - self.keepalive_last
            assert(delta_t >= 0)
            self.time_remaining -= delta_t
        else:
            # The token is wrong, which means there are probably two active logins. BAD!
            raise Exception('Incorrect token, probably two active terminals')

        if self.time_remaining <= 0:
            self.active = False


        self.keepalive_last = timestamp

    def generate_token(self):
        self.keepalive_token = generate_password(10, string.ascii_lowercase + string.ascii_uppercase + string.digits)

    def __unicode__(self):
        return ': '.join([unicode(self.terminal), self.password])
