#! /bin/bash

yum install python37 -y
pip3 install --upgrade pip setuptools
yum install python-devel python3-devel mysql-devel mysql-libs mysql-community-devel libmysqlclient-dev -y
yum install gcc -y

#rm -rf /build_src/venv/Lib/site-packages/
rm -rf /build_src/build_for_lambda/lib_layer/python/lib/python3.7/site-packages/
# requirements.txtは環境毎に共通、requirements_dev.txtをローカル用として使用する
#pip install -r /build_src/requirements.txt -t /build_src/venv/Lib/site-packages/
pip install -r /build_src/requirements.txt -t /build_src/build_for_lambda/lib_layer/python/lib/python3.7/site-packages/
#pip install awscli --upgrade --user

# フォルダが増えるとシェルを直す必要があるので何とかしたい。。
cp /usr/lib64/mysql/libmysqlclient.so.18 /build_src/src/controller/sample_api_1/
#cp -r ./.aws /root/.aws
#
#aws cloudformation package --template-file template.yaml --s3-bucket ${S3BucketName} --output-template output.yaml
#aws cloudformation deploy --template-file output.yaml --stack-name ${EnvName}-lambda-functions --capabilities CAPABILITY_IAM --parameter-overrides EnvName=${EnvName}
#tail -f /dev/null
