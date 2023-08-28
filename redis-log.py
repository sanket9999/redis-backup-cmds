  GNU nano 6.2                                                                                 log3.py                                                                                          
import time
from datetime import datetime
from google.cloud import storage
import subprocess

# GCS settings
gcs_bucket_name = 'redis-backup-from-instance'

def upload_redis_logs():
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)

    timestamp = datetime.now().strftime('%d-%m-%Y-%H-%M')
    log_file_name = f'redis-logs/redis_log_{timestamp}.log'

    subprocess.run('docker exec redis_container cat /data/redis.log > ./redis.log', shell=True, check=True)
    blob = bucket.blob(log_file_name)
    blob.upload_from_filename('./redis.log')
    print(f'Uploaded Redis log file with timestamp {timestamp} to GCS')

def main():
    while True:
        upload_redis_logs()
        time.sleep(24 * 60 * 60)  # Upload logs every 24 hours

if __name__ == '__main__':
    main()

