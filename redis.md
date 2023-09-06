To optimize your Redis configuration for high performance and utilization of system resources, you can make the following adjustments to the configuration settings:

1. **maxmemory:** To allow Redis to utilize the maximum available system memory, set `maxmemory` to 0 (no memory limit). You've already done this, but you can confirm it's set to 0:

   ```bash
   CONFIG SET maxmemory 0
   ```

2. **hash-max-ziplist-entries and hash-max-ziplist-value:** Adjust these parameters based on your specific use case. If you want to allow larger hash objects to be stored in ziplists, increase `hash-max-ziplist-entries` and `hash-max-ziplist-value` accordingly. For example:

   ```bash
   CONFIG SET hash-max-ziplist-entries 2048
   CONFIG SET hash-max-ziplist-value 256
   ```

   These values are just examples; you can fine-tune them based on your workload.

3. **activerehashing:** Ensure that `activerehashing` is set to "yes" to allow Redis to rehash the hash slots when adding or removing nodes in a Redis Cluster setup.

   ```bash
   CONFIG SET activerehashing yes
   ```

4. **save:** Adjust the save intervals based on your data persistence requirements. The default value `"3600 1 300 100 60 10000"` means that Redis will save the dataset to disk if at least one key has changed, and the save operation has not been performed in the last 3600 seconds (1 hour), or if at least 100 keys have changed, and the save operation has not been performed in the last 60 seconds. You can fine-tune these values to meet your needs.

   ```bash
   CONFIG SET save "3600 1 300 100 60 10000"
   ```

5. **maxclients:** Increase the `maxclients` value if you expect a high number of client connections. This setting determines the maximum number of concurrent client connections that Redis can handle.

   ```bash
   CONFIG SET maxclients 10000
   ```

6. **tcp-keepalive:** Adjust the `tcp-keepalive` value based on your network environment and requirements. It specifies the TCP keepalive timeout for client connections in seconds.

   ```bash
   CONFIG SET tcp-keepalive 300
   ```

7. **hz:** The `hz` (frequency of server updates) parameter controls the timer frequency in the Redis event loop. Set it to a higher value (e.g., 100) for increased responsiveness, especially if Redis is used for real-time applications.

   ```bash
   CONFIG SET hz 100
   ```

8. **loglevel:** Depending on your monitoring and debugging needs, you can set the `loglevel` to "notice" or "warning" for production environments.

   ```bash
   CONFIG SET loglevel notice
   ```

9. **appendfsync:** Adjust the `appendfsync` parameter to control how often Redis flushes data to disk. "everysec" is a good balance between data safety and performance. However, if you can tolerate some data loss in case of a crash, you can set it to "no" for better write performance.

   ```bash
   CONFIG SET appendfsync everysec
   ```

10. **daemonize:** If you're running Redis in a production environment, you may want to set `daemonize` to "yes" to run Redis as a background daemon.

   ```bash
   CONFIG SET daemonize yes
   ```

Remember to save the configuration changes and restart the Redis container for them to take effect:

```bash
SAVE
exit
sudo docker restart redis_container
```

These adjustments should help you optimize your Redis Docker container for high performance and resource utilization. However, fine-tuning Redis depends on your specific use case and system resources, so it's essential to monitor Redis's performance after making changes and adjust as needed.
