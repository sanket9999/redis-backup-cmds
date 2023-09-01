import subprocess
import time
from google.cloud import storage

# GCS settings
gcs_bucket_name = 'redis-backup-from-instance'
backup_file_name = 'redis_backups/redis_backup_2023-09-01-09-57-AM.rdb'  # Replace with the correct file name
local_file_path = 'dump.rdb'

def download_backup_from_gcs():
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)
    blob = bucket.blob(backup_file_name)

    try:
        # Download the backup file from GCS to the local filesystem
        blob.download_to_filename(local_file_path)
        print(f'Successfully downloaded backup from GCS to {local_file_path}')
    except Exception as e:
        print(f'Error downloading backup from GCS: {e}')

def load_backup_to_redis():
    # Replace 'your-redis-container-name' with the name of your Redis Docker container
    redis_container_name = 'redis_container'

    try:
        # Copy the downloaded backup file to the Redis Docker container
        docker_cp_command = ['docker', 'cp', local_file_path, f'{redis_container_name}:/data/dump.rdb']
        subprocess.run(docker_cp_command, check=True)
        print('Backup file copied to Redis container successfully')

        # Restart the Redis server to load the new data
        redis_restart_command = ['docker', 'restart', redis_container_name]
        subprocess.run(redis_restart_command, check=True)
        print('Backup loaded into Redis successfully')
    except Exception as e:
        print(f'Error loading backup to Redis: {e}')

if __name__ == '__main__':
    download_backup_from_gcs()
    load_backup_to_redis()
