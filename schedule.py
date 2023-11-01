import time

def backup_task():
    # Your backup logic here
    print("Backup task executed")

# Schedule a daily backup task
while True:
    current_time = time.localtime()
    if current_time.tm_hour == 2 and current_time.tm_min == 0:
        backup_task()
    time.sleep(60)  # Sleep for 60 seconds (adjust as needed)