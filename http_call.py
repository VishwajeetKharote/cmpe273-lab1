import requests

# List of Urls
URLs = ['https://webhook.site/2852a47a-7c19-44dc-8674-1303ef9213bf','https://webhook.site/468b1d6a-a5d4-44a4-942d-43197e831c36', 'https://webhook.site/d5b0da01-1dfe-45ec-afb3-d5e0db44c6ca']

def getHeader():
    fopen = open("output.txt","a")
    fopen.write("This is the synchronous way to execute Http requests\n")
    for URL in URLs:
         r=requests.get(URL)
         data = r.headers
         # Getting the date from response header and appending it to the file
         dateHeader = data['Date']
         fopen.write(dateHeader+'\n')
    fopen.close()     
    
def main():
    getHeader()

if __name__ == '__main__':
    main()
    