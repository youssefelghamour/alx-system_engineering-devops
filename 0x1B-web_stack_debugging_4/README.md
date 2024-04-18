# 0x1B. Web stack debugging #4

## Overview
This project involves debugging issues in a web server setup featuring Nginx under pressure. The task is to identify and resolve errors causing a significant number of failed requests.

## Files

| File                  | Description                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------|
| `0-the_sky_is_the_limit_not.pp` | Puppet manifest to optimize Nginx configuration to handle high traffic and eliminate failed requests. |
| `1-user_limit.pp`     | Puppet manifest to adjust OS configuration allowing login with the `holberton` user without file open errors. |
