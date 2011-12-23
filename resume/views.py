## index view -- setup the page
# going to use jquery to pull information down for the specific pages
#
# layout: index
#       - projects
#       - courses
#       - skills
from django.http import HttpResponse
from django.shortcuts import render_to_response
from resume.models import Department,SkillType,Job,Project,Education,Social

# index creates the initial page
def index(request):
    # just as a trial, list all of the resume information
    menu = ['home','work','projects','courses','skills']
    social = Social.objects.all()
    educations = Education.objects.all()[0]
    return render_to_response('index.html', locals())

# work experience
def work(request):
    jobs = Job.objects.order_by('-start').all()
    return render_to_response('jobs.html',locals())

def projects(request):
    projects = Project.objects.all()
    return render_to_response('projects.html',locals())
def courses(request):
    departments = Department.objects.all()
    return render_to_response('courses.html',locals())
def skills(request):
    categories = SkillType.objects.all()
    return render_to_response('skills.html',locals())
def home(request):
    return render_to_response('home.html')