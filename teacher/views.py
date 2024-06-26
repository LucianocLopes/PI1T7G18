from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import PermissionRequiredMixin

from group.models import DayWeek_Choice, Group, GridGroup
from .models import Teacher
from .forms import TeacherForm

from school.models import School

class TeacherGroupView(PermissionRequiredMixin, DetailView):
    model = Teacher
    template_name = "teacher/teacher_group.html"
    permission_required = 'teacher.change_teacher'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super(TeacherGroupView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().first()
        context['group'] = Group.objects.select_related().all().first()
        context['grid_group'] = GridGroup.objects.select_related().all()
        
        return context


class TeacherListView(PermissionRequiredMixin, ListView):
    model = Teacher
    template_name = "teacher/teacher_list.html"
    form_class = TeacherForm
    permission_required = 'teacher.view_teacher'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().first()
        
        return context

class TeacherCreateView(PermissionRequiredMixin, CreateView):
    model = Teacher
    template_name = "teacher/teacher_form.html"
    form_class = TeacherForm
    permission_required = 'teacher.add_teacher'

