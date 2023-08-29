  GNU nano 6.2                                                                                redis1.py                                                                                         
import os
import subprocess
from google.cloud import storage

# GCS settings
gcs_bucket_name = 'redis-backup-from-instance'
rdb_file_name = 'redis_backups/redis_backup_2023-08-29-02-53-PM.rdb'

# Docker container name running Redis
redis_container_name = 'redis_container'

# Redis settings
redis_password = 'qwertyuiopasdfghjklzxcvbnm'

def download_rdb_file():
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)
    blob = bucket.blob(rdb_file_name)

    local_path = './downloaded.rdb'
    blob.download_to_filename(local_path)
    return local_path

def load_rdb_to_redis(rdb_path):
    subprocess.run(['docker', 'exec', '-it', redis_container_name, 'redis-cli', '-a', redis_password, 'BGSAVE'], check=True)
    subprocess.run(['docker', 'exec', '-it', redis_container_name, 'redis-cli', '-a', redis_password, 'FLUSHALL'], check=True)
    subprocess.run(['docker', 'cp', rdb_path, f'{redis_container_name}:/data/dump.rdb'], check=True)
    subprocess.run(['docker', 'exec', '-it', redis_container_name, 'redis-cli', '-a', redis_password, 'DEBUG', 'RELOAD'], check=True)
    print('Data loaded into Redis from the .rdb file.')

if __name__ == '__main__':
    downloaded_rdb_path = download_rdb_file()
    load_rdb_to_redis(downloaded_rdb_path)
    os.remove(downloaded_rdb_path)  # Remove the downloaded .rdb file
