{"filter":false,"title":"custom_storages.py","tooltip":"/custom_storages.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["from django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","    ","    ","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["from django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","    ","    ","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":43},"end":{"row":9,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":134,"mode":"ace/mode/python"}},"timestamp":1578675581584,"hash":"20b59ecf5168b4549c3ac68ec08ca9d1f9a84e11"}