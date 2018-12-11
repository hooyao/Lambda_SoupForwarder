# Lambda_SoupForwarder

## Setup

```bash
export AWS_ACCESS_KEY_ID=${your_aws_access_key_id}
export AWS_SECRET_ACCESS_KEY=${your_aws_secret_key}
```

**Switch your python env to python 3.6, it doesn't matter how, conda or virtualenv, you pick**

```bash
npm install # install serverless framework
sls deploy  # use serverless framework to deploy
```

if everthing goes as we expected, you will see following output. Of course you need a working AWS account.
```
Service Information
service: stapletest
stage: dev
region: ap-northeast-1
stack: stapletest-dev
api keys:
  None
endpoints:
  POST - https://xxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/tswsqlforwarder
functions:
  hello: stapletest-dev-hello
layers:
  None
```