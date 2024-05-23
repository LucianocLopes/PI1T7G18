from django.views import View
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from school.models import School

from .forms import GroupForm
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from group.models import DayWeek_Choice, Group, GridGroup
from .models import GridGroup, Group
from .forms import GridGroupForm, GroupForm


class GridGroupDetailView(DetailView):
    model = Group
    template_name = "group/gridgroup.html"
    
    def get_context_data(self, **kwargs):
        context = super(GridGroupDetailView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        context['grid_group'] = GridGroup.objects.select_related().all()
        return context

class GroupBaseView(PermissionRequiredMixin, View):
    model = Group
    success_url = reverse_lazy('group_all')
    permission_required = 'group.view_group'

    def get_context_data(self, **kwargs):
        context = super(GroupBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context

class GroupListView(GroupBaseView, ListView):
    "list view"
    paginate_by = 10
    form_class = GroupForm


class GroupDetailView(GroupBaseView, DetailView):
    'detailview'
    permission_required = 'group.view_group'
    form_class = GroupForm


class GroupCreateView(GroupBaseView, CreateView):
    'createview'
    form_class = GroupForm
    permission_required = 'group.add_group'


class GroupUpdateView(GroupBaseView, UpdateView):
    'updadeview'
    form_class = GroupForm
    permission_required = 'group.add_group'        

class GroupDeleteView(GroupBaseView, DeleteView):
    'deleteview'
    permission_required = 'group.delete_group'
