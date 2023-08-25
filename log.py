import time
from google.cloud import storage
import subprocess

# GCS settings
gcs_bucket_name = 'redis-backup-from-instance'

def upload_redis_logs():
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)

    subprocess.run('docker cp redis_container:/data/redis.log ./redis.log', shell=True, check=True)
    blob = bucket.blob('redis-logs/redis.log')  # Upload logs in 'redis-logs' folder
    blob.upload_from_filename('./redis.log')
    print('Uploaded Redis log file to GCS')

def main():
    while True:
        upload_redis_logs()
        time.sleep(24 * 60 * 60)  # Upload logs every 24 hours

if __name__ == '__main__':
    main()
