from bs4 import BeautifulSoup as BS
import requests
import time

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.text
    return None

def get_glide_link(html):
    soup = BS(html,'html.parser')
    content = soup.find('div',class_='main-content')
    posts = content.find('div', class_='listings-wrapper')
    post = posts.find_all('div', class_='listing')
    links = []
    for p in post:
        r_info = p.find('div', class_='right-info')
        title = r_info.find('p', class_='title')
        link = title.find('a').get('href')
        full_link = 'https://www.house.kg/' + link
        links.append(full_link)
        # print(title.text.strip())
        # r_side = r_info.find('div', class_='right-side')
        # sep_main = r_side.find('div', class_='sep main')
        # price = sep_main.find('div', class_='price')
        # print(price.text.strip())
        # price_addition = sep_main.find('div', class_='price-addition')
        # print(price_addition.text.strip())
        # l_side = r_info.find('div', class_='left-side')
        # title_addition = l_side.find('p', class_='title-addition')
        # if title_addition:
        #     print(title_addition.text.strip())
        # else:
        #     print('Нет ЖК')
        # address = l_side.find('div', class_='address')
        # print(address.text.strip())
        # description = r_info.find('div', class_='description')
        # if description:
        #     print(description.text.strip())
        # else:
        #     print('Нет описания')
        # print()
    return links

def get_data(html):
    soup = BS(html, 'html.parser')
    content = soup.find('div', class_='content-wrapper')
    phone_block = content.find('div', class_='phone-fixable-block')
    user = phone_block.find('a', class_='name').text.strip()
    phone = phone_block.find('div', class_='number').text.strip()
    print(user, phone)
    details_main = content.find('div', class_='details-main')
    left2 = details_main.find('div', {'class':'left'})
    label = left2.find_all('div', class_='label')
    info = left2.find_all('div', class_='info')
    for l, i in zip(label, info):
        print(l.text.strip()+':', i.text.strip())
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    details_header = content.find('div', class_='details-header')
    left = details_header.find('div', class_='left')
    right_prices_block = details_header.find('div', class_='right prices-block')
    right = details_main.find('div', class_='right')
    sep_main = right_prices_block.find('div', class_='sep main')
    sep_addit = right_prices_block.find('div', class_='sep addit')
    name = left.find('h1')
    print(name.text.strip())
    c_name = left.find('div', class_='c-name')
    if c_name:
        print(c_name.text.strip())
    else:
        print('Нет ЖК.')
    address = left.find('div', class_='address')
    print(address.text.strip())
    price_dollar = sep_main.find('div', class_='price-dollar')
    print(price_dollar.text.strip())
    price_som = sep_main.find('div', class_='price-som')
    print(price_som.text.strip())
    price_dollar2 = sep_addit.find('div', class_='price-dollar')
    print(price_dollar2.text.strip())
    price_som2 = sep_addit.find('div', class_='price-som')
    print(price_som2.text.strip())
    description = right.find('div', class_='description')
    print(description.text.strip())
    
    print('_____________________________________________________________________________')
    

   
def main():
    URL = 'https://www.house.kg/kupit-kvartiru?'
    html = get_html(url=URL)
    links = get_glide_link(html=html)
    for link in links:
        posts_links = get_html(url=link)
        get_data(html=posts_links)


if __name__ == '__main__':
    main()