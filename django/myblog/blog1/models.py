# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50, default='Untitled')
    content = models.TextField()
    
    def __unicode__(self):
	return self.title
