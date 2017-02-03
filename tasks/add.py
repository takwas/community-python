from app import celery


@celery.task
def add(x, y):
    print('print')
    return x + y
