from django.db import models

# Create your models here.

class Finch:
    def _init_(self, name, height, vertical):
        self.name = name
        self.height = height
        self.vertical = vertical

        finchs = [
            Finch('Reek', '6 foot 1', '89 inches'),
            Finch('John Snow', '3 foot 9', '27 inches'),
            Finch('Agent 47', '11 foot 6', '289 inches')
        ]
