# hbust_3d -- 湖北科技学院三维模型展示系统 - 后端

## python脚本

### 创建数据库

- reate database hbust_3d DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

### 更新数据库

- py manage.py makemigrations

- py manage.py migrate 

### 开始运行

- python manage.py runserver 127.0.0.1:8001

### 下载依赖

1. pip install requests
2. pip install mysqlclient
3. pip install django-cors-headers

## 代码

- hbust_3d/setting.py  -- DATABASES  数据库名称,账号,密码,地址,端口

