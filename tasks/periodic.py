from app import celery


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    celery.conf.beat_schedule = {
        # Executes every Monday morning at 7:30 a.m.
        # 'test-schedule-task': {
        #     'task': 'test.print',
        #     'schedule': 10
        # },
    }


@celery.task(name='test.print')
def test_print():
    print('hoi task')

