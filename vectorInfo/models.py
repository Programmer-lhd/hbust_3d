from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户信息管理"""
    userName = models.CharField(verbose_name="用户账号", max_length=64)
    password = models.CharField(verbose_name="用户密码", max_length=64)
    phone = models.CharField(verbose_name="手机号", max_length=64)
    role = models.SmallIntegerField(verbose_name="角色", max_length=32)


class VectorInfo(models.Model):
    """矢量数据信息表"""
    name = models.CharField(verbose_name="楼栋名称", max_length=32)
    describe = models.CharField(verbose_name="楼栋描述", max_length=64, null=True)
    # 经度
    longitude = models.DecimalField(verbose_name="经度", max_digits=28, decimal_places=25, null=True)
    # 纬度
    latitude = models.DecimalField(verbose_name="纬度", max_digits=28, decimal_places=26, null=True)
    # 笛卡尔坐标X
    cartX = models.DecimalField(verbose_name="笛卡尔坐标X", max_digits=17, decimal_places=10, null=True)
    # 笛卡尔坐标Y
    cartY = models.DecimalField(verbose_name="笛卡尔坐标Y", max_digits=16, decimal_places=9, null=True)
    # 笛卡尔坐标Z
    cartZ = models.DecimalField(verbose_name="笛卡尔坐标Y", max_digits=17, decimal_places=10, null=True)
    minHeight = models.DecimalField(verbose_name="最小高度", max_digits=5, decimal_places=3)
    maxHeight = models.DecimalField(verbose_name="最大高度", max_digits=5, decimal_places=3)


class MonitorInfo(models.Model):
    """监控视频融合信息"""
    name = models.CharField(verbose_name="监控名称", max_length=32)
    describe = models.CharField(verbose_name="监控描述", max_length=64, null=True)
    url = models.CharField(verbose_name="监控地址", max_length=64)
    # 相机笛卡尔坐标
    cameraCartX = models.CharField(verbose_name="相机笛卡尔坐标X", max_length=64)
    cameraCartY = models.CharField(verbose_name="相机笛卡尔坐标Y", max_length=64)
    cameraCartZ = models.CharField(verbose_name="相机笛卡尔坐标Y", max_length=64)
    # 目标点笛卡尔坐标
    positionCartX = models.CharField(verbose_name="目标点笛卡尔坐标X", max_length=64)
    positionCartY = models.CharField(verbose_name="目标点笛卡尔坐标Y", max_length=64)
    positionCartZ = models.CharField(verbose_name="目标点笛卡尔坐标Y", max_length=64)
    # 视角大小
    fov = models.IntegerField(verbose_name="视角大小")
    # 最大视距
    far = models.IntegerField(verbose_name="视角大小", default=100)
    # 视角比例
    aspectRatio = models.DecimalField(verbose_name="视角比例", max_digits=3, decimal_places=2)
    # 透明度
    alpha = models.DecimalField(verbose_name="透明度", max_digits=3, decimal_places=2)


class Room(models.Model):
    """
    温泉 教二 507
    校区,区域,楼栋,层级,房间
    楼栋id,roomId,摄像头组id
    """
    build = models.ForeignKey(verbose_name="楼栋id", to="VectorInfo", to_field="id", null=True, blank=True,
                              on_delete=models.SET_NULL)
    name = models.CharField(verbose_name="房间名称", max_length=32)
    storey = models.IntegerField(verbose_name="楼层")
    # camera = models.IntegerField(verbose_name="摄像头组")
