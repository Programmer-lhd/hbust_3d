from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from vectorInfo import models


# Create your views here.

def login(request):
    userName = request.POST.get('userName')
    password = request.POST.get('password')
    userInfo = models.UserInfo.objects.all().values()
    msg = '登录失败,无账号'
    code = 400
    for item in userInfo:
        if userName == item['userName'] and password == item['password']:
            msg = '登录成功'
            code = 200
    data = {
        'msg': msg,
        'code': code,
    }
    return JsonResponse(data)


def register(request):
    userInfo = models.UserInfo.objects.all().values()
    msg = '注册成功'
    code = 200
    for item in userInfo:
        if request.POST.get('userName') == item['userName'] or request.POST.get('phone') == item['phone']:
            msg = '账号手机号已注册'
            code = 400
    if code != 400:
        models.UserInfo.objects.create(
            userName=request.POST.get('userName'),
            password=request.POST.get('password'),
            phone=request.POST.get('phone'),
            role=request.POST.get('role')
        )
    data = {
        'msg': msg,
        'code': code,
    }
    return JsonResponse(data)


def getVector(request):
    """
    :param:
    id:楼栋id

    :return:
    对应id的楼栋信息
    """
    id = request.GET.get('id')
    if id:
        vectorInfo = list(models.VectorInfo.objects.filter(id=id).values())
    else:
        vectorInfo = list(models.VectorInfo.objects.exclude(cartX=None).values())
    data = {
        'msg': '请求成功',
        'code': 200,
        'data': vectorInfo
    }
    return JsonResponse(data)


def editVector(request):
    """
    :param
    id:楼栋id,
    name:楼栋名称,
    describe:楼栋描述,
    :return:
    """
    id = request.POST.get('id')
    describe = request.POST.get('describe')
    name = request.POST.get('name')
    longitude = request.POST.get('longitude')
    latitude = request.POST.get('latitude')

    models.VectorInfo.objects.filter(id=id).update(describe=describe, name=name, longitude=longitude, latitude=latitude)
    data = {
        'msg': f'成功修改了id为{id}的描述为{describe},经度为{longitude},纬度为{latitude}',
        'code': '200'
    }
    return JsonResponse(data)


def editPosition(request):
    id = request.POST.get('id');
    name = request.POST.get('name')
    longitude = request.POST.get('longitude')
    latitude = request.POST.get('latitude')
    cartX = request.POST.get('cartX')
    cartY = request.POST.get('cartY')
    cartZ = request.POST.get('cartZ')

    models.VectorInfo.objects.filter(id=id).update(longitude=longitude, latitude=latitude, cartX=cartX, cartY=cartY,
                                                   cartZ=cartZ)
    data = {
        'msg': f'成功修改了{name}的位置',
        'code': '200'
    }
    return JsonResponse(data)


def getRoom(request):
    buildId = request.GET.get("buildId")
    storey = request.GET.get("storey")
    buildData = models.Room.objects.filter(build_id=buildId)
    storeyArr = sorted(set(buildData.values_list('storey', flat=True).distinct()), reverse=True)
    dataArr = []
    for (index, item) in enumerate(storeyArr):
        roomList = buildData.filter(storey=item)

        storeyObj = {
            'storey': item,
            'roomList': list(roomList.values())
        }
        dataArr.append(storeyObj)
    data = {
        'msg': '请求成功',
        'code': 200,
        'data': dataArr
    }
    return JsonResponse(data)


def createMonitor(request):
    print('发了')

    models.MonitorInfo.objects.create(
        name=request.POST.get('name'),
        describe=request.POST.get('describe'),
        url=request.POST.get('url'),
        cameraCartX=request.POST.get('cameraCartX'),
        cameraCartY=request.POST.get('cameraCartY'),
        cameraCartZ=request.POST.get('cameraCartZ'),
        positionCartX=request.POST.get('positionCartX'),
        positionCartY=request.POST.get('positionCartY'),
        positionCartZ=request.POST.get('positionCartZ'),
        fov=request.POST.get('fov'),
        far=request.POST.get('far'),
        aspectRatio=request.POST.get('aspectRatio'),
        alpha=request.POST.get('alpha')
    )
    data = {
        'msg': '添加成功的位置',
        'code': '200'
    }
    return JsonResponse(data)


def getMonitor(request):
    id = request.GET.get('id')
    if id:
        monitorInfo = models.MonitorInfo.objects.filter(id=id).values()
    else:
        monitorInfo = models.MonitorInfo.objects.all().values()
    data = {
        'msg': '请求成功',
        'code': 200,
        'data': list(monitorInfo)
    }
    return JsonResponse(data)
