import django_filters
from .models import Post, Category
import django.forms


class PostFilter(django_filters.FilterSet):
    """ Набор фильтров для модели Post. """

    title = django_filters.CharFilter(
        field_name='title', label='Заголовок содержит', lookup_expr='icontains',
        widget=django.forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "Ведите текст..."}))

    category = django_filters.ModelMultipleChoiceFilter(
        field_name='category', label='Искать в категориях', lookup_expr='exact', queryset=Category.objects.all(),
        widget=django.forms.CheckboxSelectMultiple(
            attrs={'type': 'checkbox', 'class': "form-check-inline"}))

    date__gt = django_filters.DateFilter(
        field_name="date", label="От даты", lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={'type': 'date', 'class': "form-control"}))

    date__lt = django_filters.DateFilter(
        field_name="date", label="До даты", lookup_expr='lt',
        widget=django.forms.DateInput(
            attrs={'type': 'date', 'class': "form-control"}))

    class Meta:
        model = Post
        fields = ['title', 'category', 'date__gt', 'date__lt']
