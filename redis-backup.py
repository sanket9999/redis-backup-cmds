import time
import subprocess
from google.cloud import storage

# GCS settings
gcs_bucket_name = 'redis-backup-from-instance'
gcs_backup_prefix = 'redis_backups/'

def get_formatted_timestamp():
    current_time = time.localtime()
    formatted_time = time.strftime('%Y-%m-%d-%I-%M-%p', current_time)
    return formatted_time

def main():
    # Connect to GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)

    while True:
        try:
            # Authenticate with Redis using redis-cli and perform BGSAVE
            auth_command = ['redis-cli', '-h', '127.0.0.1', '-p', '6379', '-a', 'qwertyuiop', 'BGSAVE']
            subprocess.run(auth_command, check=True)

            # Wait for the backup to complete
            time.sleep(5)

            # Copy Redis data file from the container to the local filesystem
            docker_cp_command = ['docker', 'cp', 'redis_container:/data/dump.rdb', './dump.rdb']
            subprocess.run(docker_cp_command, check=True)

            # Create a backup timestamp
            backup_timestamp = get_formatted_timestamp()
            backup_file_name = f'{gcs_backup_prefix}redis_backup_{backup_timestamp}.rdb'

            # Upload the backup file to GCS
            blob = bucket.blob(backup_file_name)
            blob.upload_from_filename('./dump.rdb')
            print(f'Successfully backed up to GCS: {backup_file_name}')

            # Wait for 30 minutes before the next backup
            time.sleep(30 * 60)
        except Exception as e:
            print(f'Error: {e}')
            time.sleep(10)  # Wait for 10 seconds before retrying

if __name__ == '__main__':
    main()
