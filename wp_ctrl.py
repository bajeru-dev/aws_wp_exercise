import argparse
import base64
import os
import requests


class Wordpress:
    def __init__(self, url):
        '''Get url and initialize arument parser '''
        self.url = url + '/wp-json/wp/v2/'
        self.init_parser()

    def login(self, username, password):
        '''Digest credentials and prepare header'''
        credentials = username + ':' + password
        token = base64.b64encode(credentials.encode())
        self.header = {'Authorization': 'Basic ' + token.decode('utf-8')}

    def init_parser(self):
        '''Initialize arguments'''
        # Map of functions to commands and their arguments
        function_map = {
            'list_posts' : {'cmd': self.list_posts, 'args': []},
            'get_post' : {'cmd': self.get_post, 'args': ['post_id']},
            'create_post' : {'cmd': self.create_post,'args': ['title', 'content']},
            'update_post' : {'cmd': self.update_post, 'args': ['post_id', 'title', 'content']},
            'delete_post' : {'cmd': self.delete_post, 'args': ['post_id']},
        }
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest='cmd', required=True)
        # Loop over cmds and add parsers
        for name, info in function_map.items():
            info['parser'] = subparsers.add_parser(name)
            for argument in info['args']:
                # Loop over args and add arguments
                info['parser'].add_argument(argument, type=str)
            info['parser'].set_defaults(func=info['cmd'])
        self.args = parser.parse_args()

    def wp_request(self, method, request, **kwargs):
        '''Wrapper function for requests.request'''
        response = requests.request(method, self.url + request, headers=self.header, json=kwargs.get('json'))
        if  response.status_code in [200, 201]:
            return response.json()
        else:
            raise Exception(f"Failed {method} to ({self.url + request}):\n{response.status_code} {response.reason}")

    def list_posts(self):
        '''List all posts and their IDs'''
        posts = self.wp_request('GET', 'posts')
        print("id\tTitle")
        print('-'*30)
        for post in posts:
            print(f"{post['id']}\t{post['title']['rendered']}")

    def get_post(self):
        '''Get post by ID'''
        post = self.wp_request('GET', 'posts'+ '/' + self.args.post_id)
        print(f"Title: {post['title']['rendered']}")
        print(f"Content: {post['content']['rendered']}\n")


    def create_post(self):
        '''Create new post with title and content'''
        post_data = {
            'title': self.args.title,
            'content': self.args.content,
            'status': 'publish'
        }
        self.wp_request('POST', 'posts', json=post_data)
        print("Post created successfully")

    def update_post(self):
        '''Update post by ID, new title and new content'''
        post_data = {
            'title': self.args.title,
            'content': self.args.content
        }
        self.wp_request('POST', f'posts/{self.args.post_id}', json=post_data)
        print("Post updated successfully")

    def delete_post(self):
        '''Delete post by ID'''
        self.wp_request('DELETE', f'posts/{self.args.post_id}')
        print("Post deleted successfully")

if __name__=="__main__":
    # Create wordpress object with url
    wp = Wordpress(os.environ['WP_URL'])
    # Authentication
    wp.login(os.environ['WP_USER'], os.environ['WP_APP_PASSWORD'])
    wp.args.func()