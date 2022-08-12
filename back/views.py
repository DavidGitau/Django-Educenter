from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from core.models import (
    About, 
    Blog, 
    Course
)
from .forms import (
    AboutForm, 
    BlogForm, 
    CourseForm, 
    EventForm,
    NoticeForm, 
    ResearchForm, 
    ScholarshipForm, 
    TeacherForm
)


def home(request):
    return render(request, 'be/home.html', {})

"""-------------------------------------------------------

            FUNCTION BASED VIEWS

-------------------------------------------------------"""

# def about(request):
#     form = AboutForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         print('////////////////////////')
#         form = AboutForm()
#     context = {
#         'form':form, 
#         'title': 'About',
#         }
#     return render(request, 'be/about.html', context)

# def blog(request):
#     form = BlogForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         print('////////////////////////')
#         form = BlogForm()
#     context = {
#         'form':form, 
#         'title': 'Blog',
#         }
#     return render(request, 'be/blog.html', context)

# def course(request):
#     form = CourseForm(request.POST or None)
#     context = {
#         'form':form, 
#         'title': 'Course',
#         }
#     return render(request, 'be/course.html', context)

# def event(request):
#     username = 'Dave'
#     form = EventForm(request.POST or None)
#     context = {
#         'form':form, 
#         'username':username,
#         'title': 'Event',
#         }
#     return render(request, 'be/event.html', context)

# def notice(request):
#     form = NoticeForm(request.POST or None)
#     context = {
#         'form':form, 
#         'title': 'Notice',
#         }
#     return render(request, 'be/notice.html', context)

# def research(request):
#     form = ResearchForm(request.POST or None)
#     context = {
#         'form':form, 
#         'title': 'Research',
#         }
#     return render(request, 'be/research.html', context)

# def scholarship(request):
#     form = ScholarshipForm(request.POST or None)
#     context = {
#         'form':form, 
#         'title': 'Scholarship',
#         }
#     return render(request, 'be/scholarship.html', context)

# def teacher(request):
#     form = TeacherForm(request.POST or None)
#     context = {
#         'form':form, 
#         'title': 'Teacher',
#         }
#     return render(request, 'be/teacher.html', context)


"""-------------------------------------------------------

            CLASS BASED VIEWS

-------------------------------------------------------"""

class CustomCreate(CreateView, ListView):
    # model = AboutForm
    # form_class = AboutForm
    # template_name = 'be/about.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plat'] = 'be'

        return context

class CustomDetail(DetailView):
    pass

