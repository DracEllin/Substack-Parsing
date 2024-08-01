# from bs4 import BeautifulSoup as BS
# import requests

# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         return response.text
#     return None



# def get_glide_link(html):
#     links =[]
#     soup = BS(html,'html.parser')
#     content = soup.find('div', class_='content')
#     posts = content.find('div', class_='sect__content grid-items')
#     post = posts.find_all('div', class_='poster__desc order-last')
    
#     for p in post:
#         link = p.find('a').get('href')
#         links.append(link)
        
    
#     return links
    
    
#     # content = soup.find('div',class_='main-content')
#     # posts = content.find('div', class_='listings-wrapper')
#     # post = posts.find_all('div', class_='listing')
#     # links = []
#     # for p in post:
#     #     r_info = p.find('div', class_='right-info')
#     #     title = r_info.find('p', class_='title')
#     #     link = title.find('a').get('href')
#     #     full_link = 'https://www.house.kg' + link
#     #     links.append(full_link)
        

   

# def get_data(html):
#     soup = BS(html, 'html.parser')
#     content = soup.find('div', class_='content')
#     pmovie = content.find('div', class_ = 'pmovie__main')
#     title = pmovie.find('header', class_='pmovie__header').find('h1').text.strip()
#     orig_title = pmovie.find('div', class_='pmovie__main-info ws-nowrap').text.strip()
#     raiting = pmovie.find('div',class_ = 'pmovie__anime').find('div', class_='item-slide__ext-rating item-slide__ext-rating--imdb').text.strip()
#     print(title, orig_title, raiting)
    
    
    
    
    
    
#     # content = soup.find('div', class_='content-wrapper')
#     # phone_block = content.find('div', class_='phone-fixable-block')
#     # user = phone_block.find('a', class_='name').text.strip()
#     # phone = phone_block.find('div', class_='number').text.strip()
    
#     # details = content.find('div', class_='details-main')
#     # left = details.find('div', {'class':'left'})
#     # label = left.find_all('div', class_='label')
#     # info = left.find_all('div', class_='info')
    
#     # for l, i in zip(label, info):
#     #     print(l.text.strip()+':'+ i.text.strip())
    

# def main():
#     URL = 'https://amedia.site/' #'https://www.house.kg/kupit-kvartiru?'
#     html = get_html(url=URL)
#     links = get_glide_link(html=html)
    
    
#     for link in links:
#         posts_links = get_html(url=link)
#         get_data(html=posts_links)
        
        
        
        
        
        
# if __name__ == '__main__':
#     main()





















from bs4 import BeautifulSoup as BS
import requests
from multiprocessing import Pool

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
    name = left.find('h1').text.strip()
    print(name)
    c_name = left.find('div', class_='c-name')
    c_name = c_name.text.strip() if c_name else 'Нет ЖК'
    address = left.find('div', class_='address').text.strip()
    print(address)
    price_dollar = sep_main.find('div', class_='price-dollar').text.strip()
    print(price_dollar)
    price_som = sep_main.find('div', class_='price-som').text.strip()
    print(price_som)
    price_dollar2 = sep_addit.find('div', class_='price-dollar').text.strip()
    print(price_dollar2)
    price_som2 = sep_addit.find('div', class_='price-som').text.strip()
    print(price_som2)
    description = right.find('div', class_='description')
    description = description.text.strip() if description else 'Нет описания.'
    print(description)

    data = {
        'title': name,
        'price': price_som,
        'price_dollar': price_dollar,
        'price_m2': price_som2,
        'price_dollar_m2': price_dollar2,
        'address': address,
        'zhk': c_name,
        'user': user,
        'phone': phone,
        'description': description,
        'INFO' : {l:i}
    }
    
    print('_____________________________________________________________________________')
    return data

def last_page(html):
    soup =BS(html, 'html.parcer')
    page = soup.find('ul', class_='pagination')
    pages = page.find_all('a', class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)
  
def parsing(page_num):
    URL = 'https://www.house.kg/kupit-kvartiru?'
    page_url = URL + f'page={page_num}'
    page_html = get_html(page_url)
    links = get_glide_link(page_html)
    for link in links:
        posts_links = get_html(link)
        get_data(posts_links)

def main():
    URL = 'https://www.house.kg/kupit-kvartiru?'
    html = get_html(URL)
    pages = last_page(html)
    with Pool(60) as p:
        p.map(parsing, range(1, pages+1))

if __name__ == '__main__':
    main()