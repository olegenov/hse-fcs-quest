from django.contrib import admin

from .models import Puzzle, Letter, Team

class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text') 

class LetterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'letter') 

class TeamAdmin(admin.ModelAdmin):
    list_display = ('pk', 'session') 


admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Letter, LetterAdmin)
admin.site.register(Team, TeamAdmin)
