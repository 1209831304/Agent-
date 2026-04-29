
import schedule,time
from main import pipeline

schedule.every().day.at("10:00").do(pipeline)

while True:
    schedule.run_pending()
    time.sleep(60)
