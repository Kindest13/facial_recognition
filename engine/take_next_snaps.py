import threading
import multiprocessing
import time
import schedule

from utils_faces.take_snapshot import takeSnapshot
from analytics import analytics

def run_concurrently(job_func):
    analytic_process = multiprocessing.Process(target=job_func)
    analytic_process.start()
    # analytic_process.join()

def main():
    # schedule.every(5).to(30).seconds.do(takeSnapshot)
    schedule.every(3).seconds.do(takeSnapshot)

    # schedule.every(10).minutes.do(analytics)
    schedule.every(30).seconds.do(run_concurrently, analytics)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
