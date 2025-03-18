# aws_wp_exercise
Simple 2-tier Wordpress application using this AWS account

Template based on https://vuyisile.com/creating-two-tier-wordpress-architecture-on-aws

# Validating syntax
`aws cloudformation validate-template --template-body file://template.yaml`

# Create the stack in AWS
`aws cloudformation create-stack --stack-name WordPressStack --template-body file://template.yaml --parameters ParameterKey=DatabasePassword,ParameterValue=[password]`