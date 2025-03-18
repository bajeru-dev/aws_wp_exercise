# Simple 2-tier Wordpress application using provided AWS account

Template based on https://vuyisile.com/creating-two-tier-wordpress-architecture-on-aws

## Configure AWS
* Execute: `aws configure`
* Provide credentials

## Validating syntax
`aws cloudformation validate-template --template-body file://template.yaml`

## Create the stack in AWS
`aws cloudformation create-stack --stack-name WordPressStack --template-body file://template.yaml --parameters ParameterKey=DatabasePassword,ParameterValue=[password]`