from django.contrib import admin
from .models import Testimonial, Client, Contact, PortfolioCategory, PortfolioItem, Skill, Language, PostCategory, PostItem


class SkillAdmin(admin.ModelAdmin):
    ordering = ['index']
    list_display = ['name', 'percentage', 'index']

class LanguageAdmin(admin.ModelAdmin):
    ordering = ['index']
    list_display = ['name', 'percentage', 'index']



admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(PortfolioCategory)
admin.site.register(PortfolioItem)
admin.site.register(Contact)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(PostCategory)
admin.site.register(PostItem)
