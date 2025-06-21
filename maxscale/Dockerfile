FROM mariadb/maxscale:latest

USER root

RUN apt-get update && \
    apt-get install -y net-tools procps iputils-ping curl gnupg lsb-release && \
    curl -sS https://downloads.mariadb.com/MaxScale/maxscale-release.sh | bash && \
    apt-get update && \
    apt-get install -y maxscale && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN id -u maxscale 2>/dev/null || useradd -ms /bin/bash maxscale

USER maxscale

ENTRYPOINT ["/usr/bin/maxscale"]
