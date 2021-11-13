from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from sentinelapp.auto import tasks


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.get_sentinel_datad, "interval", seconds=15)

    scheduler.start()
