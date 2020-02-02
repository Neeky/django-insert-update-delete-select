import logging

from django.http import response
from django.http import JsonResponse
from django.views.generic import base, edit, detail, list

from .. import models


logger = logging.getLogger('mysite').getChild(__name__)


class AritcleDetailView(detail.BaseDetailView):
    model = models.Article

    logger = logger.getChild("AritcleDetailView")

    def get(self, request, *args, **kwargs):
        """
        """
        logger = self.logger.getChild("get")
        logger.info("begin")
        try:
            self.object = self.get_object()
            logger.info("end")
            return JsonResponse({'pk': self.object.id, 'title': self.object.title})
        except response.Http404 as err:
            logger.warning(f"error '{str(err)}' ")
            return JsonResponse({'error-message': str(err)})


class ArticleCreateView(edit.BaseCreateView):
    """
    """
    model = models.Article
    fields = ['title']

    logger = logger.getChild("ArticleCreateView")

    def get(self, request, *args, **kwargs):
        """
        """
        logger = self.logger.getChild("get")
        logger.info("begin")
        logger.info("end")
        return JsonResponse({'error-message': 'please use post'})

    def form_valid(self, form):
        logger = self.logger.getChild("form_valid")
        logger.info("begin")

        # 查询出 Person 的 id 是多少
        person_id = self.request.POST.get('person_id', -1)
        if person_id == -1:
            logger.warning(" 'person_id' args not in request.POST")
            return JsonResponse({'error-message': "'person_id'  args must in request.POST"})

        # 如果可以执行到这里说明 person_id 至少已经上报了
        try:
            author = models.Person.objects.get(pk=person_id)
            form.instance.author = author
            self.object = form.save()
            logger.info("end")
            return JsonResponse({'pk': self.object.id})
        except Exception as err:
            logger.warning(f"error '{str(err)}' ")
            return JsonResponse({'error-message': str(err)})

    def form_invalid(self, form):
        logger = self.logger.getChild("form_invalid")
        logger.info("begin")
        logger.info("end")
        return JsonResponse({'error-message': str(form.erros)})
