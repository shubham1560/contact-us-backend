from .base import *

DEBUG = config('DEBUG') == 'TRUE'

ALLOWED_HOSTS = ['127.0.0.1', ]

AWS_STORAGE_BUCKET_NAME = 'contact-us-storage'
