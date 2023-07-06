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
    last_page = soup.find('div', class_= 'vm-pagination').find_all('li')[-1].find('a').get('href')
    # last_page =last_page0.find('a').get('href')
    # return last_page
    last = str(last_page).split(',')
    last1 = str(last[-1]).split('-')
    last2 = int(last1[-1])/100+1

    return last2
    #print(last2)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    product_list = soup.find_all('div', class_="product")
    for product in product_list:
        
        try:
            title = product.find('span', class_='prouct_name').find('a').text
        except:
            title = ''
        try:
            price = product.find('span', class_='price').text
        except:
            price = ''
        try:
            image = 'https://enter.kg' + product.find('img').get('src').text
        except:
            image = ''

        product_dict = {'title': title,
                        'image': image,
                        'price': price}
            
        write_to_csv(product_dict)    

    ''''''''''''''
    # product_list = soup.find_all('div', class_="product")
    

    # for product in product_list:

    #     title = product.find('a').attrs.get('title')
    #     image = product.find('a').attrs.get('src')
    #     price = product.find('span').text

   

def main():
    notebook_url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(notebook_url)
    get_data(html)
    end = get_last_page(html)
    for i in range(2, int(end)):
        url_with_page = notebook_url + 'results,' + f'{(i-1)*100+1}-{(i-1)*100}'
        #print(url_with_page)
        html = get_html(url_with_page)
        get_data(html) 
    # ls = list.append(get_last_page (html))
    # for i in ls:
    #     url_with_page = 'https://enter.kg/' + i
    #     html = get_html(url_with_page)
    #     get_data(html) 
        
with open('data.csv','w') as file:
    write_ = csv.writer(file)
    write_.writerow(['title       ', 'image      ', 'price       '])


main()

# def ls = []

# for i in ls:
#     url_with_page = 'https://enter.kg/' + i