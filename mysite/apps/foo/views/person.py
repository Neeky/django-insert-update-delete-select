import logging

from django.http import response
from django.http import JsonResponse
from django.views.generic import base, edit, detail, list

from apps.foo import models


#logger = logging.getLogger("mysite").getChild('foo').getChild('view')
logger = logging.getLogger("mysite").getChild(__name__)


class PersonDetailView(detail.BaseDetailView):
    """
    detail-view 一次只返回一行数据
    """

    # model 作为 detail-view 的一个必要属性
    model = models.Person

    logger = logger.getChild("PersonDetailView")

    def get(self, request, *args, **kwargs):
        """
        查询给定的数据，如果不存在就报错
        """
        logger = self.logger.getChild("get")

        # 当对应的行找不到时会报 Http404 异常
        try:
            self.object = self.get_object()
        except response.Http404 as err:
            logger.warning(f"Exception occure '{str(err)}' ")
            return JsonResponse({'error-message': str(err)})

        # 如果可以执行到这时，说明没有异常产生
        return JsonResponse({'pk': self.object.id,
                             'name': self.object.name,
                             'age': self.object.age})


class PersonListView(list.BaseListView):
    queryset = models.Person.objects.all().values('id', 'name')

    logger = logger.getChild('PersonListView')

    def get(self, request, *args, **kwargs):
        logger = self.logger.getChild("post")
        logger.info("begin")
        queryset = self.get_queryset()
        datas = []
        for person in queryset:
            datas.append(person)
        logger.info("end")
        return JsonResponse({'data': datas})


class PersonListLastView(list.BaseListView):
    """
    """
    queryset = models.Person.objects.all().values('id', 'name')
    ordering = "id"
    logger = logger.getChild('PersonListLastView')

    def get(self, request, lmt, *args, **kwargs):
        logger = self.logger.getChild("post")
        logger.info("begin")
        logger.info(f"lmt = {lmt}")
        queryset = self.get_queryset()
        total = queryset.count()
        logger.info(f"count = {total}")
        start_index = total - lmt
        if start_index < 0:
            start_index = 0
        datas = []
        for person in queryset[start_index:]:
            datas.append(person)
        logger.info("end")
        return JsonResponse({'data': datas})


class PersonCreateView(edit.BaseCreateView):
    """
    创建 person 对象
    """
    model = models.Person
    fields = ['name', 'age']
    logger = logger.getChild("PersonCreateView")

    def form_valid(self, form):
        """
        在 form 校验成功后会调用这个方法
        """
        logger = self.logger.getChild("form_valid")
        logger.info(f"form = {form}")

        # 保存到数据库
        try:
            self.object = form.save()
            return JsonResponse({'pk': self.object.id, 'name': self.object.name})
        except Exception as err:
            logger.warning(
                f"exception occure {err.message}")

            return JsonResponse({'message': "Exception occur"})

    def form_invalid(self, form):
        """
        表单没有通过校验时会执行到这里
        """
        logger = self.logger.getChild("form_invalid")
        logger.warning(f"form = {form}")
        return JsonResponse({'message': form.errors})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'error-message': 'please use post.'})


class PersonUpdateView(edit.BaseUpdateView):
    """
    """
    model = models.Person
    fields = ['name']

    logger = logger.getChild('PersonUpdateView')

    def post(self, request, *args, **kwargs):
        """
        更新对应的行
        """
        logger = self.logger.getChild("post")
        logger.info('begin')
        try:
            # django 会对所有列做 update 操作
            response = super().post(request, args, kwargs)
            logger.info('end')
            return response
        except Exception as err:
            logger.warning(err)
            logger.info('error')
            return JsonResponse({'error-message': str(err)})

    def get(self, request, *args, **kwargs):
        logger = self.logger.getChild("get")
        logger.info("begin")
        logger.warning("invalide http method get")
        logger.info("end")
        return JsonResponse({'error-message': 'please use post method'})


class PersonDeleteView(edit.BaseDeleteView):
    """
    """
    model = models.Person
    fields = ['name']

    logger = logger.getChild("PersonDeleteView")

    def get(self, request, *args, **kwargs):
        logger = self.logger.getChild("get")
        logger.info('begin')
        logger.info('end')
        return JsonResponse({'error-message': 'please use post'})

    def post(self, request, *args, **kwargs):
        """
        """
        logger = self.logger.getChild("post")
        logger.info("begin")
        try:
            self.object = self.get_object()
            id = self.object.id
            self.object.delete()
            logger.info("end")
            return JsonResponse({'pk': id})
        except response.Http404 as err:
            logger.warning(f"error '{str(err)}'  ")
            return JsonResponse({'error-message': str(err)})
