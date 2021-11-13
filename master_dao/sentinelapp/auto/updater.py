from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from sentinelapp.auto import tasks


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.test, "interval", seconds=10)

    scheduler.start()
