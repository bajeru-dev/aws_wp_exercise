# Simple 2-tier Wordpress application using provided AWS account

## Use AWS template (template.yaml)
Note: Template is based on guide from: https://vuyisile.com/creating-two-tier-wordpress-architecture-on-aws

### Configure AWS
* Execute: `aws configure`
* Provide credentials

### Validating syntax
`aws cloudformation validate-template --template-body file://template.yaml`

### Create the stack in AWS
`aws cloudformation create-stack --stack-name WordPressStack --template-body file://template.yaml --parameters ParameterKey=DatabasePassword,ParameterValue=[password]`

### Debug deployment
`aws cloudformation describe-stack-events --stack-name [stack ID] (or WordPressStack)`

### Delete stack
`aws cloudformation delete-stack --stack-name WordPressStack`

## Use of wp_ctrl.py

### Set evironment variables
```bash
    export WP_URL=''
    export WP_USER=''
    export WP_PASSWORD=''
```

### Get website posts
`python3 wp_ctrl.py get_posts`

