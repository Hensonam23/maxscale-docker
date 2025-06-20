# MaxScale Docker Fork – Final Project

## Introduction

This project is a fork of the official MaxScale Docker repository by MariaDB. The goal was to set up and test MaxScale in a Docker environment using Docker Compose, making small changes and documenting how it works for our final class project.

MaxScale is a database proxy for MariaDB that provides advanced features like read/write splitting, failover, and monitoring. Here, we walk through how to run it, how we configured it, and how our Docker setup is structured.

## Running

To start the containerized MaxScale service, make sure Docker and Docker Compose are installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/Hensonam23/maxscale-docker.git
   cd maxscale-docker
   ```

2. Start the containers:
   ```bash
   sudo docker-compose up -d
   ```

3. Check that all containers are running:
   ```bash
   sudo docker ps
   ```

4. Enter a shard container to verify the data:
   ```bash
   sudo docker exec -it shard1 bash
   mysql -u root -prootpass
   ```

## Configuration

All configuration changes are handled through the `maxscale.cnf` file inside the `config/` directory. This file controls how MaxScale connects to backend servers, what services it runs and how it routes traffic.

We also included an optional `.env` file to keep environment variables separate and make the setup cleaner.

### Example Configuration Path

```
./maxscale.cnf
```

This file defines:
- Two servers: `shard1`, `shard2`
- A service using the `schemarouter` plugin
- Listener on port `4006`
- Monitoring with `mariadbmon`

## MaxScale Docker-Compose Setup

Docker Compose sets up three containers:
- `shard1`: MariaDB server with `shard1.sql`
- `shard2`: MariaDB server with `shard2.sql`
- `maxscale`: MaxScale proxy that routes queries based on database name

The setup file is located at:

```
./docker-compose.yml
```

To rebuild the containers:

```bash
sudo docker-compose down
sudo docker-compose up --build -d
```

## Query Results

These are example outputs from the two test queries: `zipcodes_one` and `zipcodes_two`.

### Largest zipcode in `zipcodes_one`
```sql
SELECT MAX(Zip) FROM zipcodes_one;
```

| Max Zip |
|---------|
| 99929   |

---

### All zipcodes where state = 'KY'
```sql
SELECT * FROM zipcodes_one WHERE State = 'KY'
UNION
SELECT * FROM zipcodes_two WHERE State = 'KY';
```

| Zip   | State | City       | TotalWages   |
|-------|-------|------------|--------------|
| 40906 | KY    | HARLAN     | 18920456.38  |
| 42420 | KY    | HENDERSON  | 20399817.73  |

---

### Zipcodes between 40000 and 41000
```sql
SELECT * FROM zipcodes_one WHERE Zip BETWEEN 40000 AND 41000
UNION
SELECT * FROM zipcodes_two WHERE Zip BETWEEN 40000 AND 41000;
```

| Zip   | State | City       | TotalWages   |
|-------|-------|------------|--------------|
| 40003 | KY    | BAGDAD     | 2839127.33   |
| 40508 | KY    | LEXINGTON  | 13877912.55  |

---

### Total wages in state = 'PA'
```sql
SELECT TotalWages FROM zipcodes_one WHERE State = 'PA'
UNION
SELECT TotalWages FROM zipcodes_two WHERE State = 'PA';
```

| TotalWages   |
|--------------|
| 32498743.27  |
| 23578100.45  |

---

## Credits

Written and Tested by **Aaron Henson**  
Class: **CNE370 - Introduction to Virtualization**

---

##  Resources

- [Official MaxScale Docker Repo](https://github.com/mariadb-corporation/maxscale-docker)
- [Markdown Help](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)