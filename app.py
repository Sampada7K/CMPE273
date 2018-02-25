from flask import Flask
import requests
import sys
import re

header = {'accept': 'application/vnd.github.VERSION.raw'}

url = sys.argv[1]
match = re.search(r'https://github.com/([\w/-]+)', url)
if match:
    user_repo = match.group(1)
    
name = 'README.md'
gh_url = 'https://api.github.com/repos/' + user_repo + '/contents/' + name + '?ref=master'
#print gh_url

app = Flask(__name__)

@app.route('/')
@app.route('/v1/')
def download():
    r=requests.get(gh_url, headers=header)
    return r.text
  
@app.route('/v1/<name>')
def download_dconfig_yml(name):
	
	gh_url = 'https://api.github.com/repos/' + user_repo + '/contents/' + name + '?ref=master'
	r=requests.get(gh_url, headers=header)
	return r.text

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')