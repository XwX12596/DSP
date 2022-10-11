import requests

od = {'action':'snapshot'}

authe = ('xmh','xmhxmhxmh')

response = requests.get("http://mc.xwxstudio.com/?",params=od, auth=authe)
response.raise_for_status()
with open('./Monthly1/code/snapshot.jpg','wb') as f:
    f.write(response.content)