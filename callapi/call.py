# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


def makecall():
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = 'AC256d608ef4ca633250dc030288f03ae6'
    auth_token = '77e8eb5e01a7d2690d36208094a02bc2'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='https://89170e04ae0a.ngrok.io/voice',
                            to='+919630880741',
                            from_='+18477449594'
                        )

    print(call.sid)
makecall()
# scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)
# def start():
#     if settings.DEBUG:
#       	# Hook into the apscheduler logger
#         logging.basicConfig()
#         logging.getLogger('apscheduler').setLevel(logging.DEBUG)

#     scheduler.add_jobstore(DjangoJobStore(), "default")
#     # run this job every 24 hours
#     scheduler.add_job(makecall,'cron', day_of_week='mon-sat', hour=14, minute=55, timezone=ist)
#     register_events(scheduler)
#     scheduler.start()
#     print("Scheduler started...", file=sys.stdout)