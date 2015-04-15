from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from bgdapp.models import Story, Content, Mission, Function, JourneyStage, ContentArchetype

class ContentInlineTab(admin.TabularInline):
    model = Content
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

    
class ContentInlineStacked(admin.StackedInline):
    model = Content
    
class ContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    search_fields = ['title', 'description', 'notes']
    list_filter = ('priority', 'purpose', 'function', 'story__journeystage', 'type')
    list_display = ('title', 'description', 'priority')
    
    
class StoryAdmin(admin.ModelAdmin):
    inlines = [
        ContentInlineTab,
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    search_fields = ['title', 'description', 'notes', 'content__title', 'content__description', 'content__notes']
    list_filter = ('mission', 'journeystage', 'priority')
    list_display = ('title', 'description', 'notes', 'mission', 'priority')


admin.site.register(Story, StoryAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Mission)
admin.site.register(Function)
admin.site.register(JourneyStage)
admin.site.register(ContentArchetype)


# Register your models here.
