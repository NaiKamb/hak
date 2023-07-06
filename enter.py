import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open ('prod.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data ['title'],
                         data ['image'],
                         data ['price']))

def get_html(url):
    response = requests.get(url)
    return response.text

# def get_last_page (html):
#     soup = BeautifulSoup(html, 'lxml')
#     last_page = soup.find('div', class_='vm-pagination').find_all('span', class_= 'pagenav').text
#     # .find_all('li')[-1].text
#     return last_page
#     print(last_page)

def get_last_page (html):
    soup = BeautifulSoup(html, 'lxml')
    last_page0 = soup.find('div', class_= 'vm-pagination').find('ul').find_all('li')[-3].find('a').get('href')
    # last_page =last_page0.find('a').get('href')
    # return last_page
    print(last_page0)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find_all('div', class_="product")
    

    for product in product_list:

        title = product.find('a').attrs.get('title')
        image = product.find('a').attrs.get('src')
        price = product.find('span').text

        product_dict = {'title': title,
                        'image': image,
                        'price': price}
            
        write_to_csv(product_dict)

def main():
    notebook_url = 'https://enter.kg/computers/noutbuki_bishkek/'
    html = get_html(notebook_url)
    get_data(html)
    get_last_page(html)
    # ls = list.append(get_last_page (html))
    # for i in ls:
    #     url_with_page = 'https://enter.kg/' + i
    #     html = get_html(url_with_page)
    #     get_data(html) 
    # urls = [notebook_url.format(x) for x in range (1, get_last_page+1)]

    # page = 1
    # while True:
    #     get_url = notebook_url + '/' + str(page)
    #     html = get_html(get_url)
    #     get_data(html)
    #     if get_last_page(get_html(get_url)) == 'Вперёд':
    #         page += 1
    #     else:
    #         break
        
with open('data.csv','w') as file:
    write_ = csv.writer(file)
    write_.writerow(['title       ', 'image      ', 'price       '])


main()

# def ls = []

# for i in ls:
#     url_with_page = 'https://enter.kg/' + i