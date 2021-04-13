import schedule
import time

from utils_faces.take_snapshot import takeSnapshot
from analytics import analytics

# schedule.every(5).to(30).seconds.do(takeSnapshot)
schedule.every(3).seconds.do(takeSnapshot)

# schedule.every(10).minutes.do(analytics)
schedule.every(30).seconds.do(analytics)

while True:
    schedule.run_pending()
    time.sleep(1)
