import datetime
import bleach
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404, HttpResponse
from django.template import loader
from django.utils.safestring import mark_safe
from markdown import markdown as markdown_func

def object_list(request, queryset, paginate_by=None, page=None,
                allow_empty=True, template_name=None, template_object_name='object',
                content_type=None):
    queryset =  queryset._clone()

    if paginate_by:
        paginator = Paginator(queryset, paginate_by,
                              allow_empty_first_page=allow_empty)

        if not page:
            page = request.GET.get('page', 1)
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404
        try:
            page_obj = paginator.page(page_number)
        except InvalidPage:
            raise Http404

        c = {
            '{}_list'.format(template_object_name): page_obj.object_list,
            'paginator': paginator,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
        }
    else:
        c = {
            '{}_list'.format(template_object_name): queryset,
            'paginator': None,
            'page_obj': None,
            'is_paginated': False
        }
        if not allow_empty and len(queryset) == 0:
            raise Http404

    if not template_name:
        model = queryset.model
        template_name = '{app}/{object}_list.html'.format(app=model._meta.app_label,
                                                          object=model._meta.object_name.lower())
    t = loader.get_template(template_name)
    return HttpResponse(t.render(c, request=request), content_type=content_type)

def object_detail(request, queryset, object_id=None, template_name=None,
                  template_object_name='object', content_type=None):
    model = queryset.model
    if object_id:
        queryset = queryset.filter(pk=object_id)
    try:
        obj = queryset.get()
    except ObjectDoesNotExist:
        raise Http404('No {} found matching the query'.format(model._meta.verbose_name))
    if template_name is None:
        template_name = '{app}/{object}_detail.html'.format(app=model._meta.app_label,
                                                    object=model._meta.object_name.lower())
    try:
        comments = obj.comment_set.all()
        t = loader.get_template(template_name)
        c = {
            template_object_name: obj,
            'nodes': comments,
        }
        response = HttpResponse(t.render(c, request=request), content_type=content_type)
    except:
        t = loader.get_template(template_name)
        c = {
            template_object_name: obj,
        }
        response = HttpResponse(t.render(c, request=request), content_type=content_type)
    return response

def sanitize_markdown(value):
    return mark_safe(
            bleach.clean(
                bleach.linkify(markdown_func(value, extensions=['gfm'], tab_length=2)),
                tags = [
                    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em',
                    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                    'i', 'li', 'ol', 'p', 'pre', 'strong', 'ul',
                    'table', 'thead', 'tr', 'th', 'tbody', 'td',
                    'div', 'br', 'span',
                ],
            )
    )
