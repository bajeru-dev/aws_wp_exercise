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
    export WP_URL='[base URL of your WordPress website]'
    export WP_USER='[your username]'
    export WP_APP_PASSWORD='[application password generated in WP user panel]'
```

### Get list of website posts
`python3 wp_ctrl.py list_posts`

### Get post content 
`python3 wp_ctrl.py get_post [post_id]`

### Create post 
`python3 wp_ctrl.py create_post '[post_title]' '[post_content]'`

### Create post 
`python3 wp_ctrl.py update_post [post_id] '[post_title]' '[post_content]'`

### Delete post 
`python3 wp_ctrl.py delete_post [post_id]`