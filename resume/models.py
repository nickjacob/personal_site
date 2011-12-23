from django.db import models

### RESUME INFORMATION ###
# represents a job
class Job(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    corpURL = models.URLField()
    desc = models.CharField(max_length=300)
    start = models.DateField()
    end = models.DateField()

    def __unicode__(self):
        return self.title

# subset - point that happens within job
class JobPoint(models.Model):
    point = models.CharField(max_length=300)
    job = models.ForeignKey(Job)

    def __unicode__(self):
        return self.point

# education
class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    gpa = models.DecimalField(max_digits=4,decimal_places=2)
    grad = models.DateField()

    def __unicode__(self):
        return self.school

# skills
class SkillType(models.Model):
    title = models.CharField(max_length=150)

    def __unicode__(self):
        return self.title

class Skill(models.Model):
    SKILL_LEVELS = (
        ('NOV','Novice'),
        ('INT','Intermediate'),
        ('ADV','Advanced'),
        ('EXP','Expert')
        )
    desc = models.CharField(max_length=150)
    level = models.CharField(max_length=100,choices=SKILL_LEVELS)
    years = models.IntegerField()
    sk_type = models.ForeignKey(SkillType)

    def __unicode__(self):
        return self.desc
# courses
class Department(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=150)
    dept = models.ForeignKey(Department)
    
    def __unicode__(self):
        return self.title
# projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    desc = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

class Tech(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name
# writing
class Writing(models.Model):
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=5000)
    excerpt = models.CharField(max_length=400)

    def __unicode__(self):
        return self.title

# social links
class Social(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    def __unicode__(self):
        return self.title