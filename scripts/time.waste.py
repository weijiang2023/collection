# write a program to download news
import requests
from bs4 import BeautifulSoup

# Make a request to the BBC News website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and URLs on the page
articles = soup.find_all('a', class_='gs-c-promo-heading')

# Print the article titles and URLs
for article in articles:
    title = article.text.strip()
    url = article['href']
    print('Title:', title)
    print('URL:', url)

'''
import requests
from bs4 import BeautifulSoup
import re

# Make a request to the BBC News website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and URLs on the page
articles = soup.find_all('a', class_='gs-c-promo-heading')

# Loop through each article and download the content
for article in articles:
    # Get the URL of the article
    url = article['href']
    
    # Check if the URL starts with http:// or https://
    if not re.match(r'http(s)?://', url):
        url = 'https://www.bbc.com' + url
    
    # Make a request to the article URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the article title, pic, and video
    title = soup.find('h1', class_='story-body__h1').text.strip()
    pic = soup.find('div', class_='js-delayed-image-load')['data-src']
    video = soup.find('div', class_='js-delayed-image-load')['data-alt']
    
    # Extract the article content
    content = ''
    paragraphs = soup.find_all('div', class_='story-body__inner')
    for paragraph in paragraphs:
        content += paragraph.text.strip() + '\n'
    
    # Save the article title, pic, video, and content to a file
    with open('news.txt', 'a') as f:
        f.write('Title: ' + title + '\n')
        f.write('Pic: ' + pic + '\n')
        f.write('Video: ' + video + '\n')
        f.write('Content: ' + content + '\n\n')
'''

'''
import requests
from bs4 import BeautifulSoup
import re

# Make a request to the BBC News website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and URLs on the page
articles = soup.find_all('a', class_='gs-c-promo-heading')

# Loop through each article and download the content
for article in articles:
    # Get the URL of the article
    url = article['href']
    
    # Check if the URL starts with http:// or https://
    if not re.match(r'http(s)?://', url):
        url = 'https://' + url
    
    # Make a request to the article URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the article title, pic, and video
    title = soup.find('h1', class_='story-body__h1').text.strip()
    pic = soup.find('div', class_='js-delayed-image-load')['data-src']
    video = soup.find('div', class_='js-delayed-image-load')['data-alt']
    
    # Extract the article content
    content = ''
    paragraphs = soup.find_all('div', class_='story-body__inner')
    for paragraph in paragraphs:
        content += paragraph.text.strip() + '\n'
    
    # Save the article title, pic, video, and content to a file
    with open('news.txt', 'a') as f:
        f.write('Title: ' + title + '\n')
        f.write('Pic: ' + pic + '\n')
        f.write('Video: ' + video + '\n')
        f.write('Content: ' + content + '\n\n')
'''

'''
import requests
from bs4 import BeautifulSoup

# Make a request to the BBC News website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and URLs on the page
articles = soup.find_all('a', class_='gs-c-promo-heading')

# Loop through each article and download the content
for article in articles:
    # Get the URL of the article
    url = article['href']
    
    # Make a request to the article URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the article title, pic, and video
    title = soup.find('h1', class_='story-body__h1').text.strip()
    pic = soup.find('div', class_='js-delayed-image-load')['data-src']
    video = soup.find('div', class_='js-delayed-image-load')['data-alt']
    
    # Extract the article content
    content = ''
    paragraphs = soup.find_all('div', class_='story-body__inner')
    for paragraph in paragraphs:
        content += paragraph.text.strip() + '\n'
    
    # Save the article title, pic, video, and content to a file
    with open('news.txt', 'a') as f:
        f.write('Title: ' + title + '\n')
        f.write('Pic: ' + pic + '\n')
        f.write('Video: ' + video + '\n')
        f.write('Content: ' + content + '\n\n')
'''

'''
import requests
from bs4 import BeautifulSoup

# Make a request to the BBC News website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and URLs on the page
articles = soup.find_all('a', class_='gs-c-promo-heading')

# Open a file to write the article titles and URLs
with open('news.txt', 'w') as f:
    # Write the article titles and URLs to the file
    for article in articles:
        title = article.text.strip()
        url = article['href']
        f.write('Title: ' + title + '\n')
        f.write('URL: ' + url + '\n')
        f.write('\n')
'''

'''
import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
url = 'https://www.vogue.co.jp/article/area-interview'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the article title and content
title = soup.find('h1', class_='article-title').text.strip()
content = soup.find('div', class_='article-body').text.strip()

# Print the results
print('Title:', title)
print('Content:', content)
'''
exit()


# the program to play
mobile_web_urls = []
url_00 = 'https://m.vip.com/product-1712113374-6920233443785874078.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685175878612&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_01 = 'https://m.vip.com/product-1712113374-6920150872492365982.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685175977411&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_02 = 'https://m.vip.com/product-1712113374-6920149387357352158.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685176037758&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_03 = 'https://m.vip.com/product-1712113374-6920320050469233886.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685176153109&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_04 = 'https://m.vip.com/product-1712113374-6920282350456338078.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685176291071&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_05 = 'https://m.vip.com/product-1710615555-6919215431619897731.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685176575630&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_06 = 'https://m.vip.com/product-1710615555-6919308635027689539.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685177060438&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_07 = 'https://m.vip.com/product-1710613848-6919734452508559704.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685177492228&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_08 = 'https://m.vip.com/product-1710613848-6919341627674719960.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685177566098&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_09 = 'https://m.vip.com/product-1710613848-6919785510787974232.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685177694005&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_10 = 'https://m.vip.com/product-1711260442-6919846423661425754.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685178303187&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'
url_11 = 'https://m.vip.com/product-1711260442-6920159645493330010.html?nmsns=shop_android-7.92.7-link&nst=product&nsbc=&nct=link&ncid=f28739a2-9f74-3372-b95d-038b61a13ad0&nabtid=13&nuid=430653402&nchl_param=share:f28739a2-9f74-3372-b95d-038b61a13ad0:1685178419943&mars_cid_a=f28739a2-9f74-3372-b95d-038b61a13ad0&chl_type=share'

mobile_web_urls.append(url_00)
mobile_web_urls.append(url_01)
mobile_web_urls.append(url_02)
mobile_web_urls.append(url_03)
mobile_web_urls.append(url_04)
mobile_web_urls.append(url_05)
mobile_web_urls.append(url_06)
mobile_web_urls.append(url_07)
mobile_web_urls.append(url_08)
mobile_web_urls.append(url_09)
mobile_web_urls.append(url_10)
mobile_web_urls.append(url_11)

# convert the above mobile website links to pc website links
pc_web_urls = []
base = "https://detail.vip.com/detail-"
for url in mobile_web_urls:
    web_url = base + url.split("?")[0].split("product-")[1]
    pc_web_urls.append(web_url)
print(pc_web_urls)

# for each pc_web_url crawl the product info from it
for pc_web_url in pc_web_urls:
    import requests
    from bs4 import BeautifulSoup

    # Make a request to the website
    response = requests.get(pc_web_url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    #print(soup)

    product_name_element = soup.find('div', {'class': 'name'})
    if product_name_element is not None:
        product_name = product_name_element.text.strip()
    else:
        product_name = 'Product name not found'
    print(product_name)

    '''
    # Find all the product links on the page
    product_links = soup.find_all('a', class_='product-link')

    # Extract the product information from each link
    for link in product_links:
        product_name = link.find('div', class_='product-name').text
        product_price = link.find('div', class_='product-price').text
        product_image = link.find('img')['src']
        
        # Do something with the product information (e.g. save it to a file)
        print(product_name, product_price, product_image)
    '''