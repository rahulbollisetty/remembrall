from datetime import datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
#importing the callmsg function from script.py that you have made
ist = pytz.timezone('Asia/Kolkata')
from .call import makecall
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(makecall,'cron', day_of_week='mon-sun', hour=12, minute=30, timezone=ist,args=['+918319709976'])
    scheduler.add_job(makecall,'cron', day_of_week='mon-sun', hour=19, minute=30, timezone=ist,args=['+918319709976'])
    scheduler.add_job(makecall,'cron', day_of_week='mon-sun', hour=10, minute=00, timezone=ist,args=['+919100773339'])
    scheduler.start()
    print(scheduler.print_jobs())