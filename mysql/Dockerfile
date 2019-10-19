FROM mysql:5.7

ADD ./conf.d /etc/mysql/conf.d
ADD ./initdb.d /docker-entrypoint-initdb.d

RUN touch /var/log/mysql/mysqld.log