import requests

day = 5
url = "https://adventofcode.com/2022/day/" + str(day) + "/input"
print(url)
x = requests.get(url)