import requests
from bs4 import BeautifulSoup

#r = requests.get("https://www.blockchain.com/eth/address/0x03f034fb47965123ea4148e3147e2cfdc5b1f7a5")
#soup = BeautifulSoup(r.text, 'html.parser')

prefix = "https://www.blockchain.com"

def process(postfix):
    url = prefix + postfix
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    information = soup.find('div', class_ = "hnfgic-0 enzKJw")
    info = []

    for a in information:
        info.append(a.find('span', "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC").getText())

    print(info[5])
    #info array
    #Nonce 1
    #Number of Transactions 2
    #Final Balance 3
    #Total Sent 4
    #Total Received 5
    #Total Fees 6

    
    #find next url
    hrefs = []

    item = soup.find_all('div', class_ = "sc-1fp9csv-0 koYsLf")
    item.reverse()

    for data in item:
        if (data.find('span', class_ = "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC sc-85fclk-0 fhjukF") != None):
            
            date = data.find('span', class_ = "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC").getText()
            print(date)
            to = data.find('div', class_ = "sc-1rk8jst-2 flPSdq").getText()
            print(to)
            amount = data.find('div', class_ = "sc-1rk8jst-1 bFopoh").getText()
            print(amount)
            
            links = data.find_all('a')
            for href in links:
                hrefs = href.get('href')
            break

    #Text Preprocessing
    #Nonce 1
    #Number of Transactions 2
    #Final Balance 3
    #Total Sent 4
    #Total Received 5
    #Total Fees 6
    txt = ""
    txt = txt + "Nonce: "
    txt = txt + info[1] + "\n"
    txt = txt + "Number of Transactions: "
    txt = txt + info[2] + "\n"
    txt = txt + "Final Balance: "
    txt = txt + info[3] + "\n"
    txt = txt + "Total Sent: "
    txt = txt + info[4] + "\n"
    txt = txt + "Total Received: "
    txt = txt + info[5] + "\n"
    txt = txt + "Total Fees"
    txt = txt + info[6] + "\n"
    txt = txt + "Date: "
    txt = txt + date + "\n"
    txt = txt + "To: "
    txt = txt + to + "\n"
    txt = txt + "Amount: "
    txt = txt + amount + "\n"
    

    f = open('test.txt', 'w')
    f.write(txt)
    f.close()


process("/eth/address/0x03f034fb47965123ea4148e3147e2cfdc5b1f7a5")