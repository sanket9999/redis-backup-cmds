# redis-search-on-ubantu-instanc-with-GCP-bucket-bakcup


```
sudo apt update
```
# ----------------------------------------------------------------
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
# ----------------------------------------------------------------
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
# ----------------------------------------------------------------
```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
# ----------------------------------------------------------------
```
sudo apt update
```
# ----------------------------------------------------------------
```
sudo apt install docker-ce docker-ce-cli containerd.io
```
# ----------------------------------------------------------------
```
sudo docker volume create redis_data
```
# ----------------------------------------------------------------
```
sudo docker run -d -p 6379:6379 -v redis_data:/data --name redis_container redislabs/redisearch:latest
```
# ----------------------------------------------------------------
```
sudo apt install redis-tools
```
# ----------------------------------------------------------------
```
sudo docker run -it --rm --link redis_container:redis redis redis-cli -h redis -p 6379
```
# ----------------------------------------------------------------

#Press ctrl + c

# ----------------------------------------------------------------

```
sudo docker update --restart always redis_container
```
# ----------------------------------------------------------------
```
sudo docker start redis_container
```
# ----------------------------------------------------------------
```
redis-cli
```
# ----------------------------------------------------------------
```
config set requirepass [Enter the password]
```
# ----------------------------------------------------------------

# You can now continue to use redis database with redis search & json.

# ----------------------------------------------------------------

# Using redisinsight add some data.
# ----------------------------------------------------------------
```
sudo apt install python3-pip
```
# ----------------------------------------------------------------
```
pip3 install redis google-cloud-storage
```
# ----------------------------------------------------------------
```
sudo usermod -aG docker $USER
newgrp docker  
```

# newgrp docker  # Activate the new group membership

# ----------------------------------------------------------------

# Add the Email account to bucket with storage admin access.

```
gcloud auth application-default login
```

# Copy the link provided on the console, and paste it in browser, login to you GCP Account
# Allow the access, and copy the code from browser and paste it to terminal and hit enter.

# ----------------------------------------------------------------
#Installation for pm2 server.
```
sudo apt-get install npm
```
# ----------------------------------------------------------------
```
sudo npm install -g pm2
```
# ----------------------------------------------------------------
```
nano start_redis_backup.sh
```
# ----------------------------------------------------------------

#Copy paste the below script in the file.

# ----------------------------------------------------------------
```
#!/bin/bash

pm2 start backup_redis_to_gcs.py --interpreter python3 --name redis_backup_script
```
# ----------------------------------------------------------------
```
chmod +x start_redis_backup.sh

```
# ----------------------------------------------------------------

```
nano backup_redis_to_gcs.py
```
# ----------------------------------------------------------------
```
#copy the code from the python file provided in the repository.
```
# ----------------------------------------------------------------

```
sudo apt-get install google-cloud-sdk
```
# ----------------------------------------------------------------

```
pip install google-cloud-secret-manager
```
# ----------------------------------------------------------------

# In GCP Enable Secret Manager API, In security, Go in secret manager, create secret, enter name and password in value and hit create.

# ----------------------------------------------------------------


```
sudo pm2 startup systemd

```
# ----------------------------------------------------------------

```
pm2 start start_redis_backup.sh --name redis_backup_start_script

```
# ----------------------------------------------------------------
```
pm2 save

```                                                               
# ----------------------------------------------------------------
```
sudo reboot

```
# ----------------------------------------------------------------
```
pm2 list

```
# ----------------------------------------------------------------


# Summary 
# 
# Redis Installation completed.
# Python and pip Installation completed.
# Gcloud Packages Installation completed.
# PM2 Server Installation completed.
# Python file created and cop pasted the code.
# Started the redis with GCP backup.

