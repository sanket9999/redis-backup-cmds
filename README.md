```
    1  sudo apt update
    2  sudo apt install apt-transport-https ca-certificates curl software-properties-common
    3  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    4  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    5  sudo apt update
    6  sudo apt install docker-ce docker-ce-cli containerd.io
    7  sudo docker volume create redis_data
    8  sudo docker run -d -p 6379:6379 -v redis_data:/data --name redis_container redislabs/redisearch:latest
    9  sudo apt install redis-tools
   10  sudo docker run -it --rm --link redis_container:redis redis redis-cli -h redis -p 6379
   11  sudo docker update --restart always redis_container
   12  sudo docker start redis_container
   13  redis-cli
   14  sudo docker ps
   15  python3 backup_redis_to_gcs3.py
   16  gcloud auth application-default login
   17  python3 backup_redis_to_gcs3.py
   18  gsutil config -e
   19  sudo gsutil config -e
   20  gcloud auth application-default login
   21  python3 backup_redis_to_gcs3.py
   22  nano backup_redis_to_gcs4.py
   23  python3 backup_redis_to_gcs4.py
   24  cat backup_redis_to_gcs4.py
   25  history
   ```
```
sudo usermod -aG docker $USER
newgrp docker  # Activate the new group membership
```
```
gcloud auth application-default login
```
```
sudo apt install python3-pip
```
```
pip3 install redis google-cloud-storage
```


