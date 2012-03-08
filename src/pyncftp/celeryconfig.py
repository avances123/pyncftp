BROKER_URL = "amqp://fabio:fabio@fa-work:5672/myvhost"
CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("tasks", )

