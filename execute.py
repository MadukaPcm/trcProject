from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)

#jobs
import scheduler_jobs

scheduler.add_job(scheduler_jobs.MyFunc, 'interval', seconds=10)
scheduler.add_job(scheduler_jobs.MyFuncView, 'interval', seconds=15)
scheduler.start()