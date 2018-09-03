import asyncio
import requests

#List of URLs 
URL1 = "https://webhook.site/2852a47a-7c19-44dc-8674-1303ef9213bf"
URL2 = "https://webhook.site/468b1d6a-a5d4-44a4-942d-43197e831c36"
URL3 = "https://webhook.site/d5b0da01-1dfe-45ec-afb3-d5e0db44c6ca"

fopen = open("output.txt","a")
fopen.write("This is the asynchronous way to execute Http requests\n")
fopen.close() 

# Definition of coroutine 
async def myCoroutine(URL):
    fopen1 = open("output.txt","a")
    await asyncio.sleep(3)
    r=requests.get(URL)
    # Getting header information
    data = r.headers['Date']
    fopen1.write(data+'\n')
    fopen1.close()

async def main():
        tasks=[]
        tasks.append(asyncio.ensure_future(myCoroutine(URL1)))
        tasks.append(asyncio.ensure_future(myCoroutine(URL2)))
        tasks.append(asyncio.ensure_future(myCoroutine(URL3)))
        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()