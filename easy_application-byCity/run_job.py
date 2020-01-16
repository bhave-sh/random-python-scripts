import requests 
from pprint import pprint

url = "https://raw.githubusercontent.com/j-delaney/easy-application/master/README.md"
resp=requests.get(url)

city=[0]
city=city_input.strip().replace(" ","").lower()


result = []
skip2lines = 0
counter=0
for i in resp.text.split('\n'):
    if i.startswith('|') and skip2lines >= 2:
        text = i.split('|')[1].split('](')
        text[0] = text[0].strip()[1:]
        text[1] = text[1].strip()[0:-1]
        text.append(i.split('|')[2])
        result.append(text)

    if (i.strip() == str('| Company Name | Location |')):
        skip2lines += 1
    elif (i.strip() == '| --- | --- |'):
        skip2lines += 1
pass
pprint(len(result))


refined_result = []

for i in range(len(result)):
    if city in str(result[i][2]).strip().replace(" ","").lower():
        refined_result.append(result[i])
pass

pprint(refined_result)
