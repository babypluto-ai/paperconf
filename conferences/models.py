from django.db import models
from django.conf import settings
from django.urls import reverse

from user_app.consts_ import COUNTRY_CHOICES
from .const_ import TOPICS_CHOICES

class Conference(models.Model):
    title = models.CharField(max_length=255)
    acronym = models.CharField(max_length=100, unique=True)
    web_page = models.URLField()
    submission_link = models.URLField(blank=True)
    description = models.TextField()
    venue = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    abstract_reg_deadline = models.DateField()
    submission_deadline = models.DateField()
    topic = models.CharField(max_length=200, choices=TOPICS_CHOICES)

    def save(self, *args, **kwargs):
        self.acronym = self.acronym.lower()
        domain = 'http://127.0.0.1:8000'
        if not self.submission_link:
            self.submission_link = f"{domain}{reverse('paper-create', kwargs={'conf': self.acronym})}"
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.acronym} | {self.title}'