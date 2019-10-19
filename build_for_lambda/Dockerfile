FROM amazonlinux:latest

#RUN yum install python37 -y
#RUN pip3 install --upgrade pip setuptools
#RUN yum install python-devel python3-devel mysql-devel mysql-libs mysql-community-devel libmysqlclient-dev -y
#RUN yum install gcc -y

#ADD ../ /build_src/
COPY C:/Users/yamazakim/.aws /root/.aws

WORKDIR /build_src/build_for_lambda
CMD ./build.sh