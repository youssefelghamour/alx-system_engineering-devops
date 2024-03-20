# 0x14. MySQL

## Overview

The project involves setting up MySQL replication between two servers, web-01 and web-02, ensuring data redundancy and high availability. We configure replication and implement a backup strategy for disaster recovery. The goal is to ensure the reliability, availability, and security of the MySQL database across both servers.

## Files
| File Name                       | Description                                               |
|--------------------------------|-----------------------------------------------------------|
| `4-mysql_configuration_primary` | Answer file containing MySQL primary (web-01) configuration.       |
| `4-mysql_configuration_replica` | Answer file containing MySQL replica (web-02) configuration.       |
| `5-mysql_backup`                | Bash script to generate MySQL dump and compress it.       |

## Tasks
### Task #1: Setting up MySQL database

On web-01:
```bash
# Connect to MySQL
mysql -u root -p

# Create MySQL user and grant privileges
mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
mysql> GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit
```

On web-02:
```bash
# Connect to MySQL
mysql -u root -p

# Create MySQL user and grant privileges
mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
mysql> GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit
```

### Task #2: Create a database and table

On web-01:
```bash
# Connect to MySQL
mysql -u root -p

# Create database tyrell_corp
mysql> CREATE DATABASE tyrell_corp;

# Use the tyrell_corp database
mysql> USE tyrell_corp;

# Create table nexus6
mysql> CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

# Insert at least one entry into the nexus6 table
mysql> INSERT INTO nexus6 (name) VALUES ('Leon');

# Grant SELECT permissions to holberton_user on the nexus6 table
mysql> GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

# Flush privileges to apply changes
mysql> FLUSH PRIVILEGES;

# Exit MySQL
mysql> exit
```

On web-02:
```bash
# Connect to MySQL
mysql -u root -p

# Create database tyrell_corp
mysql> CREATE DATABASE tyrell_corp;

# Create the same database and table, since replication hasn't been set
# They won't be created, so we have to do that manually
# Missing databases and tables on the slave before setting up replication can cause errors
# After replication is set, all changes will be automatically replicated
mysql> USE tyrell_corp;
mysql> CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

mysql> exit
```

### Task #3: Configuring MySQL replication

On web-01:
```bash
# Connect to MySQL
mysql -u root -p

# Create a MySQL user for replication
mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';
mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
mysql> FLUSH PRIVILEGES;
mysql> SHOW MASTER STATUS;
```


### Task #4: Setup a Primary-Replica infrastructure using MySQL

On web-01:
```bash
# Edit MySQL configuration file
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

# Modify configuration to enable binlog replication
# Add the following lines under [mysqld] section:
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp

# comment out the bind-addres line: 
# bind-address  = 127.0.0.1
# Save and exit the editor
# Restart MySQL service
sudo systemctl restart mysql
```

On web-02:
```bash
# Edit MySQL configuration file
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

# Modify configuration to enable binlog replication
# Add the following lines under [mysqld] section:
server-id       = 2
relay_log       = /var/log/mysql/mysql-relay-bin.log
log_bin         = /var/log/mysql/mysql-bin.log
binlog_do_db    = tyrell_corp

# Save and exit the editor
# Restart MySQL service
sudo systemctl restart mysql

# Connect to MySQL on web-02
mysql -u root -p

# Configure replication settings
mysql> CHANGE MASTER TO MASTER_HOST='18.204.9.11', MASTER_USER='replica_user', MASTER_PASSWORD='projectcorrection280hbtn', MASTER_LOG_FILE='mysql-bin.000019', MASTER_LOG_POS=154;

# Start slave
mysql> START SLAVE;

# Check MySQL replication status
mysql> SHOW SLAVE STATUS\G
```

### Task #5: MySQL backup

On web-01:
```bash
# Run the Bash script to generate MySQL dump and create a compressed archive
./5-mysql_backup root
```

