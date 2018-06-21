# -*- coding: utf-8 -*-

import logging

from django.http import HttpResponse
import json
from crazygt.model import gt_model
from crazygt.util import pagation

logger = logging.getLogger("django")


def hobby_list(request):
    condition = request.GET['condition']
    page_size = request.GET['pageSize']
    page_num = request.GET['pageNum']
    hobby = gt_model.Hobby()
    list = hobby.select_hobby_list(condition)
    hobby.close()
    page = pagation.Pagation(page_size, page_num, list)
    total_count = page.total_count()
    entity = page.entity()
    data = {"data": entity, "totalNum": total_count}
    return HttpResponse(json.dumps(data, ensure_ascii=False))
