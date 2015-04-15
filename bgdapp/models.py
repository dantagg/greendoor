from django.db import models

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    notes =  models.TextField(blank=True)
    mission = models.ForeignKey('Mission')
    journeystage = models.ForeignKey('JourneyStage', blank=True, null=True)
    priority = models.CharField(max_length=256, choices=[('3', 'high'), ('2', 'medium'), ('1', 'low')])
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "stories"
    
class Mission(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    notes =  models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
    
class Function(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    notes =  models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
    
class JourneyStage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    notes =  models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
  
   
class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    notes =  models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=256, choices=[('3', 'high'), ('2', 'medium'), ('1', 'low')])
    type = models.ForeignKey('ContentArchetype', null=True)
    
    purpose = models.CharField(max_length=256, choices=[('1', 'immediate'), ('2', 'longterm'), ('3', 'green doors')])
    story = models.ForeignKey('Story')
    function = models.ForeignKey('Function')

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority', 'function']
        
class ContentArchetype(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    notes =  models.TextField(blank=True, null=True)
   
   
