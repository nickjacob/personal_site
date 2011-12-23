__author__ = 'nbjacob'
# file to register classes with admin
from resume.models import Course, Job, JobPoint, Department,Skill,SkillType,Project,Tech,Writing,Education,Social
from django.contrib import admin
from django import forms

class JobDescForm(forms.ModelForm ):
    desc = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Job
# create the admin class for a job
class JPInline(admin.StackedInline):
    model = JobPoint
    extra = 3

class JobAdmin(admin.ModelAdmin):
    inlines = [JPInline]
    form = JobDescForm

# department class
class CourseInline(admin.StackedInline):
    model = Course
    extra = 3

class DeptAdmin(admin.ModelAdmin):
    inlines = [CourseInline]


# skill class
class SkillInline(admin.StackedInline):
    model = Skill
    extra = 5
class SkillTypeAdmin(admin.ModelAdmin):
    inlines = [SkillInline]

# project class
class TechInline(admin.StackedInline):
    model = Tech
    extra = 3
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechInline]

admin.site.register(Job,JobAdmin)
admin.site.register(Department,DeptAdmin)
admin.site.register(SkillType,SkillTypeAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register([Writing,Education,Social])

# register with the admin site