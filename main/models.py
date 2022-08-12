# from django.db import models

# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     content = models.TextField(default='')
#     summary = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et.dolore magna aliqua. Ut enim ad minim veniam, quis nostrud. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe ipsa illo quod veritatis, magni debitis fugiat dolore voluptates! Consequatur, aliquid. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat perferendis sint optio similique. Et amet magni facilis vero corporis quos.')

#     class Meta:
#         abstract = True
#         ordering = ['id']

#     def __str__(self):
#         return self.name

# class About(CommonInfo):
#        summary = None  

# class Blog(CommonInfo):
#     post_date = models.DateField()
#     post_read = models.IntegerField()
#     post_share = models.IntegerField()
#     post_comments = models.IntegerField()
#     heading = models.CharField(max_length=255)

# class Event(CommonInfo):
#     location = models.CharField(max_length=255)
#     event_date = models.DateField()
#     event_time = models.TimeField()
#     e_speaker = models.ManyToManyField('Teacher')
#     fee = models.IntegerField()

# class FunFact(CommonInfo):
#     about = None
#     summary = None
#     number = models.IntegerField()

# class Notice(CommonInfo):
#     notice_date = models.DateField()


# class Interest(CommonInfo):
#     summary = None

# class Teacher(CommonInfo):
#     education = models.CharField(max_length=255)
#     t_interest = models.ManyToManyField('Interest')
#     email = models.EmailField()
#     phone = models.CharField(max_length=50)
#     social_media = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     t_courses = models.ManyToManyField('Course')

# class Requirement(CommonInfo):
#     summary = None

# class Course(CommonInfo):
#     c_length = models.IntegerField()
#     c_duration = models.IntegerField()
#     c_requirement = models.ManyToManyField('Requirement')
#     c_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
#     fees = models.FloatField()
#     funding = models.TextField()

# class Research(CommonInfo):
#     about = None

# class Scholarship(CommonInfo):
#     s_course = models.ForeignKey('Course', on_delete=models.CASCADE)