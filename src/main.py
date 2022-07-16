from datetime import datetime, timezone

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from ProcessingService import ProcessingService

scheduler: BlockingScheduler = BlockingScheduler()
processing_svc: ProcessingService = ProcessingService()


@scheduler.scheduled_job(IntervalTrigger(seconds=20))
def scheduled_task():
    print(datetime.now(timezone.utc).astimezone().isoformat())
    processing_svc.process()


try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
