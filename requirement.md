GCP

1. Service account -> Storage Admin Access. (If error give EDITOR access.).
2. Download json key of service account.
3. create bucket with by default name.
4. Give service account access IAM and permission as Storage Admin Access.
5. Create Secret Manager from security, give name and in value pass the password.
6. copy the name of Secret Manager and paste in python code.

7. Files Required for the operations.
```
7.1. Readme.md
7.2. Backup.md
7.3. redis-backup-secret-key.py
```
