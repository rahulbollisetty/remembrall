from datetime import datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
#importing the callmsg function from script.py that you have made
ist = pytz.timezone('Asia/Kolkata')
from .call import makecall
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(makecall,'cron', day_of_week='mon-sun', hour=19, minute=30, timezone=ist)
    # scheduler.add_job(makecall,'cron', day_of_week='mon-sun', hour=17, minute=42, timezone=ist)
    # scheduler.add_job(makecall,'cron', day_of_week='mon-sun', hour=17, minute=42, timezone=ist)
    scheduler.start()
    print(scheduler.print_jobs())