import requests,os,threading, time
from pathlib import Path

spamsent = 0
def title():
	global spamsent
	while True:
		os.system(f'title [Strawpoll Spammer] [Spam Sent] [{spamsent}]')
threading.Thread(target = title).start()
print("\nIf https://www.strawpoll.me/1234/r was the url, 1234 would be your code.\n\nGet the strawpoll option by inspecting the network traffic via developer tools.\nA request named the strawpollcode is what you want.\nFind the options section in form data(scroll down) and copy the number .\n\nStrawpoll code?")
strawpollcode = input()

print("\nStrawpoll option?")
strawpolloption = input()





def spamstrawpoll(strawpollcode,strawpolloption,proxy):
	global spamsent
	global allproxies
	try:
		data = requests.post(f"https://www.strawpoll.me/{strawpollcode}",data = {"options": strawpolloption}, proxies={'https': 'http://%s' % (proxy)}, timeout=5)
		if data.status_code == 200 and "success" in data.text:
			spamsent += 1
	except Exception as Error:
		#print(Error)
		pass
	try:
		allproxies.remove(proxy) #if we use the proxy we wanna get rid of it - ip duplication check is on for most surveys - if the proxy doesn't work no point using it, hence I always attempt to remove them'
	except:
		pass		



allproxies = []



proxyfile = Path("proxies.txt")
if proxyfile.is_file():
	print("Reading off proxies.txt")
	with open("proxies.txt", 'r') as f:
		for prox in f.readlines():
			allproxies.append(prox.strip())
	print("Read successfully")
else:
	print("Scraping Proxies")
	data = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all').text
	for p in data.splitlines():
		allproxies.append(p)
		#i coulda saved a few lines here - ill improve this in my next update
	print("Proxies Scraped")

time.sleep(1)
os.system("cls")
while True:
	for proxy in allproxies:
		#print(proxy)
		try:
			threading.Thread(target = spamstrawpoll, args = (strawpollcode,strawpolloption,proxy,)).start()
		except:
			pass
		time.sleep(0.1)
