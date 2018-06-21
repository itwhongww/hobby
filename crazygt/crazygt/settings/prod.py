from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'weiax',  # 你要存储数据的库名，事先要创建之
        'USER': 'hongww',  # 数据库用户名
        'PASSWORD': '198954',  # 密码
        'HOST': 'localhost',  # 主机
        'PORT': '3306',  # 数据库使用的端口
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }, # 针对 DEBUG = True 的情况
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
        }, # 对日志信息进行格式化，每个字段对应了日志格式中的一个字段，更多字段参考官网文档，我认为这些字段比较合适，输出类似于下面的内容
        # INFO 2016-09-03 16:25:20,067 /home/ubuntu/mysite/views.py views.py views get 29: some info...
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
             'formatter':'standard'
        },
        'file_handler': {
             'level': 'DEBUG',
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': '/home/weiax/crazygt.log',
             'formatter':'standard'
        }, # 用于文件输出
        'console':{
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers' :['file_handler', 'console'],
            'level':'DEBUG',
            'propagate': True # 是否继承父类的log信息
        }, # handlers 来自于上面的 handlers 定义的内容
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}