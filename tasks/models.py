from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Task1Play(models.Model):
    
    user    = models.ForeignKey(User,related_name="plays", editable=False, on_delete=models.CASCADE)
    start   = models.DateTimeField(auto_now_add=True,editable = False)
    right   = models.PositiveIntegerField(verbose_name="Number of right answers",default=0)
    wrong   = models.PositiveIntegerField(verbose_name="Number of wrong answers",default=0)
    end     = models.DateTimeField(editable = False, null=True, blank=True)
    finished = models.BooleanField(default=False)
    duration = models.DurationField(null=True)

    """
    def duration(self):
        "The duration of the experiment"
        delta = self.end - self.start
        days = delta.days
        hours = delta.seconds//3600
        minutes = (delta.seconds/3600.0 - hours)*60
        seconds = (minutes - int(minutes))*60
        return "%d days  %02d h : %02d min : %02d,%02d sec" %(days,hours,int(minutes),int(seconds), delta.microseconds//10000)
    """
    def __unicode__(self):
        return "%s" %(self.user)
    
    class Meta:
        ordering = ['duration','-wrong']

