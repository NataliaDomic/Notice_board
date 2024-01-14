import django_filters
from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Article, Subscription, Comment


class ArticleFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок',
    )

    categoryType = django_filters.ModelChoiceFilter(
        field_name='article.Category',
        queryset=Category.objects.all(),
        label='Категория',
    )

    dateCreation_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
