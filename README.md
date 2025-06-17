# MaxScale Docker Fork – Final Project

## Introduction
---

This project is a fork of the official MaxScale Docker repository by MariaDB. The goal was to set up and test MaxScale in a Docker environment using Docker Compose, making small changes and documenting how it works for our final class project.

MaxScale is a database proxy for MariaDB that provides advanced features like read/write splitting, failover, and monitoring. Here, we walk through how to run it, how we configured it, and how our Docker setup is structured.

## Running
---

To start the containerized MaxScale service, make sure you’re in the project directory and run:

```bash
sudo docker-compose up -d
```

This pulls the official MaxScale image and starts the container in detached mode.

To confirm it’s running:

```bash
sudo docker ps
```

To stop everything:

```bash
sudo docker-compose down
```

If you make changes to the config file and need to rebuild:

```bash
sudo docker-compose up -d --build
```

This will rebuild the container using your updated config.

## Configuration
---

All configuration changes are handled through the `maxscale.cnf` file inside the `config/` directory. This file controls how MaxScale connects to backend servers, what services it runs, and how it routes traffic.

We also included an optional `.env` file to keep environment variables separate and make the setup cleaner.

### Example Configuration Path

```text
./config/maxscale.cnf → /etc/maxscale
```

If you need to:
- Add new backend servers
- Change user credentials
- Modify routing behavior

Just update the config file and rebuild the container with the `--build` flag.

## MaxScale Docker-Compose Setup
---

We’re using a single `docker-compose.yml` file that launches one service for MaxScale.

### Here's how it's set up:

```yaml
services:
  maxscale:
    image: mariadb/maxscale:latest
    ports:
      - "4006:4006"      # MaxScale service port
      - "8989:8989"      # MaxScale Admin GUI (optional)
    volumes:
      - ./config:/etc/maxscale
    restart: unless-stopped
```

- **Image**: Uses the official `mariadb/maxscale` image.
- **Volumes**: Mounts the local `config/` folder to `/etc/maxscale` in the container.
- **Ports**: 4006 for client traffic, and 8989 for accessing the MaxScale GUI (if enabled in config).
- **Restart Policy**: Container will auto-restart unless manually stopped.

## Query Results
---

These are example outputs from the two test queries: `zipcodes_one` and `zipcodes_two`.

### Output from zipcodes_one:

```sql
+----------+---------+
| zipcode  | city    |
+----------+---------+
| 98101    | Seattle |
| 98052    | Redmond |
+----------+---------+
```

### Output from zipcodes_two:

```sql
+----------+-------------+
| zipcode  | population  |
+----------+-------------+
| 98101    | 123456      |
| 98052    | 78910       |
+----------+-------------+
```

These outputs confirm that MaxScale is routing queries to the appropriate backend databases.

## Submission Notes
---