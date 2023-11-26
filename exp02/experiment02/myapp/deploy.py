import requests

deploy_url = 'https://api.render.com/deploy/srv-clhm5tef27hc739ruru0?key=Y1WGFnJrYTg'

response = requests.post(deploy_url)

if response.status_code == 200:
    print("Deployment triggered successfully!")
else:
    print(f"Failed to trigger deployment. Status code: {response.status_code}")
