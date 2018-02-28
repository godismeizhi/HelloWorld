from django.http import HttpResponse
import json

'''
我是注释
'''


def hello(request):
    dict = {'aaa': 'bbb', 'ccc': 'dddddddddd'}
    return HttpResponse(json.dumps(dict), content_type="application/json")


def world(request):
    param = request.GET.get("param")
    if (param != None):
        print(param)
    else:
        param = '参数为空'
    return HttpResponse(param)
