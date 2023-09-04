# redis-search-on-ubantu-instanc-Backup


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
```
sudo docker stop redis_container
```
# ----------------------------------------------------------------

# Remember to change the name of file to dump.rdb

# ----------------------------------------------------------------
```
sudo cp dump.rdb /var/lib/docker/volumes/redis_data/_data/dump.rdb
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

# Give password and check it, keys * .
