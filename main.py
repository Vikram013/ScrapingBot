import discord
from bs4 import BeautifulSoup
import requests

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    url = 'https://listado.mercadolibre.com.co/'
    #shoes#D[A:shoes]
    content = message.content
    u = url + content + '#D[A' + content + ']'
    response = requests.get(u)
    html = response.text
    
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find(class_ = 'ui-search-layout ui-search-layout--stack')
    product = links.find(class_ = 'ui-search-item__title').get_text()
    price = links.find(class_ = 'price-tag-fraction').get_text()
    link = links.find('a').get('href')
    

    await message.channel.send('product: '+product+'\n' +'price: $ '+price+'\n' + 'link: '+link)

    
    url = 'https://paytmmall.com/shop/search?q='
    url1 = '&from=organic&child_site_id=6&site_id=2&category=5048%2C5254'
    u = url + content + url1
    response = requests.get(u)
    html = response.text
    
    soup = BeautifulSoup(html, "html.parser")

    links = soup.find(class_ = '_3WhJ')
    link = 'https://paytmmall.com/' + links.find('a').get('href')
    detail = soup.find(class_ = 'pCOS')
    product = detail.find(class_ = 'UGUy').get_text();
    price = detail.find(class_ = '_1kMS').get_text()

    
    await message.channel.send('product: '+product+'\n' +'price: $ '+price+'\n' + 'link: '+link)
    

    

client.run('OTc2MTE3MDc1MDQwOTYwNTQz.G7JoVz.Z0C6ObvOKZVfQbnfxnkAJTWuLcDap9lEgiiIPQ')