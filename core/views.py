from django import views
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import date
from django.db.models import Q
from django.views.generic import (
    ListView, 
    DetailView
)
from core.models import (
    About,
    Blog, 
    Course,  
    Event,
    FunFact, 
    Notice, 
    Research, 
    Scholarship,
    Teacher 
)


"""------------------------------------------------------------

                    FUNCTION BASED VIEWS
                    
------------------------------------------------------------"""

def base_view(request):
    title = About.objects.get(id=2)
    return title

def home_view(request):
    course_list = Course.objects.filter(id__lt=7)
    course_detail = get_object_or_404(course_list, pk=1)
    teacher_list = Teacher.objects.filter(id__lt=4)
    teacher_detail = get_object_or_404(teacher_list, pk=1)
    blog_reccommend = Blog.objects.filter(post_date__lt=date(2022,4,21))
    context = {
        'course_list': course_list,
        'course_detail': course_detail,
        'teacher_list': teacher_list,
        'teacher_detail': teacher_detail,
        'blog_reccommend': blog_reccommend,
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    about = About.objects.all()
    fun_facts = FunFact.objects.all()
    about = get_object_or_404(about, pk=1)
    teacher_list = Teacher.objects.filter(id__lt=4)
    teacher_detail = get_object_or_404(teacher_list, pk=1)
    context = {
        'about': about,
        'head': 'About Us',
        'title': base_view(request),
        'fun_facts': fun_facts,
        'about': about,
        'teacher_list': teacher_list,
        'teacher_detail': teacher_detail,
    }
    return render(request, 'core/about.html', context)

def contact_view(request, li):
    title = {
            'name':'Contact Us',
            'content': """Do you have other questions? Don't worry, there aren't any dumb questions. Just fill out the form below and we'll get back to you as soon as possible.
            """
        }
    context = {
        'title': title,
    }
    return render(request, 'core/'+li, context)



# def blog_view(request, li, pk=1):
#     blog_list = Blog.objects.all()
#     blog_details = get_object_or_404(blog_list, pk=pk)
#     blog_reccommend = Blog.objects.filter(post_date__lt=date(2022,4,21))
#     context = {
#         'head': 'Our Blog',
#         'title': base_view(request),
#         'blog_details': blog_details,
#         'blog_list': blog_list,
#         'blog_reccommend': blog_reccommend,
#     }
#     return render(request, 'core/'+li , context)

# def course_view(request, li, pk=1):
#     course_list = Course.objects.all()
#     course_detail = get_object_or_404(course_list, pk=pk) 
#     school = course_detail.c_school   
#     req = course_detail.c_requirement.all()
#     req1 = req[:4]
#     req2 = req[4:]
#     course_reccommend = Course.objects.filter(Q(c_school=school)&~Q(id=pk))
#     context = {
#         'head': 'Our Courses',
#         'title': base_view(request),
#         'course_detail': course_detail,
#         'req': req,
#         'req1': req1,
#         'req2': req2,
#         'course_list': course_list,
#         'course_reccommend': course_reccommend
#     }
#     return render(request, 'core/'+li, context)

# def teacher_view(request, li, pk=1):
#     teacher_list = Teacher.objects.all()
#     teacher_detail = get_object_or_404(teacher_list, pk=pk)
#     courses = teacher_detail.t_courses.all() 
#     context = {
#         'head': 'Our Teachers',
#         'title': base_view(request),
#         'teacher_detail': teacher_detail,
#         'teacher_list': teacher_list,
#         'courses': courses,
#     }
#     return render(request, 'core/'+li, context)

# def event_view(request, li, pk=1):
#     event_list = Event.objects.all()
#     event_detail = get_object_or_404(event_list, pk=pk)
#     speakers = event_detail.e_speaker.all()
#     event_reccommend = Event.objects.filter(id__lt=4)
#     context = {
#         'head': 'Upcoming Events',
#         'title': base_view(request),
#         'event_detail': event_detail,
#         'event_list': event_list,
#         'event_reccommend': event_reccommend,
#         'speakers': speakers,
#     }
#     return render(request, 'core/'+li, context)

# def notice_view(request, li):
#     notice_list = Notice.objects.all()
#     notice_detail = get_object_or_404(notice_list, pk=1)
#     context = {
#         'head': 'Notice',
#         'title': base_view(request),
#         'notice_detail': notice_detail,
#         'notice_list': notice_list
#     }
#     return render(request, 'core/'+li, context)

# def research_view(request, li):
#     # research_detail = Research.objects.get(id=1)
#     research = Research.objects.all()
#     context = {
#         'head': 'Research',
#         'title': base_view(request),
#         'research': research,
#         # 'research_list': research_list
#     }
#     return render(request, 'core/'+li, context)

# def scholarship_view(request, li):
#     # scholarship_detail = Scholarship.objects.get(id=1)
#     scholarship = Scholarship.objects.all()
#     context = {
#         'head': 'Scholarship',
#         'title': base_view(request),
#         'scholarship': scholarship,
#         # 'scholarship_list': scholarship_list
#     }
#     return render(request, 'core/'+li, context)



"""------------------------------------------------------------

                    CLASS BASED VIEWS

------------------------------------------------------------"""

class CustomList(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        m = self.object_list.get(id=1)
        context['title'] = m.header_about
        return context

class CustomDetail(DetailView):
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['blog_reccommend'] = Blog.objects.filter(post_date__lt=date(2022,4,21))
            context['event_reccommend'] = Event.objects.filter(id__lt=4)
            context['title'] = self.object.header_about            
            context['course_reccommend'] = Course.objects.filter(Q(c_school=self.object.c_school)&~Q(id=self.object.id))
        except AttributeError:
            pass
        return context

