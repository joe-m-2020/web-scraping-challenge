from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'C:/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    #Use beautiful soup to collect and append titles to list then take
    # first entry as top_news_title
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    nasa_news_titles = []

    results = soup.find_all("div",class_="content_title")

    for entry in results[1:-10]:
        div_tag = entry.find("a").text
        nasa_news_titles.append(div_tag)
    top_news_title = nasa_news_titles[0]

    #use beautiful soup to append paragraphs to list then take first entry as 
    # news_p
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    teasers = []

    results2 = soup2.find_all("div",class_="article_teaser_body")
    for entry2 in results2[0:]:
        div_2 = entry2.text
        teasers.append(div_2)

    news_paragraph = teasers[0]


    # Find featured image on jpl.nasa.gov/spaceimages/?search=&category=Mars
    #click through data link to find expanded size img src
    url_3 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_3)
    html_3 = browser.html
    soup_3 = BeautifulSoup(html_3, 'html.parser')

    results_3 = soup_3.find_all("div", class_="carousel_items")
    for entry1 in results_3:
        a_tag = entry1.find('a')
        link_url='https://www.jpl.nasa.gov' + a_tag['data-link']
        browser.visit(link_url)
        html_4 = browser.html
        soup_4 = BeautifulSoup(html_4, 'html.parser')
        results_4 = soup_4.find('img', class_="main_image")
        a_tag_2= results_4['src']

    featured_image_url = 'https://www.jpl.nasa.gov' + a_tag_2

    # pull table data
    mars_facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(mars_facts_url)


    # put data in dataframe
    mars_facts_df = tables[0]
    mars_facts_df.columns = ['Data','Values']

    # set index as Data
    mars_facts_df.set_index('Data', inplace=True)

    # Use pandas function df.to_html() to create a table in HTML
    mars_facts_html_table = mars_facts_df.to_html()

    # Pull item class to grab link to hemisphere pages and use as list in for loop

    hemisphere_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    html5 = browser.html
    soup_5 = BeautifulSoup(html5, 'html.parser')
    results_hem=soup_5.find_all('div',class_="item")

    # Create containers for images and titles

    mars_hemisphere_images=[]
    mars_image_titles = []

    # Use for loop to visit pages; CSS selector for link because it is the most 
    # precise direction while soup.find works well for the titles since the
    # class is title

    for result in results_hem:
        a_tag_5 = result.find('a')
        hemi_link = a_tag_5['href']
        new_link = "https://astrogeology.usgs.gov" + hemi_link
        browser.visit(new_link)
        html6 = browser.html
        soup_6 = BeautifulSoup(html6, 'html.parser')
        selector = soup_6.select('li > a[href$="jpg"]')
        link_list = selector[0]
        mars_hemisphere_images.append(link_list['href'])
        find_titles = soup_6.find('h2', class_='title').text
        mars_image_titles.append(find_titles)

    # Use for loop to append images and titles to dictionaries in a list
    hemisphere_image_urls=[]

    for x in range(4):
        url_dict = {}
        url_dict['title']=mars_image_titles[x]
        url_dict['image_url']=mars_hemisphere_images[x]
        hemisphere_image_urls.append(url_dict)
        
    # Save data in dictionary
    mars_data = {
        "Top News Title" : top_news_title,
        "News Paragraph" : news_paragraph,
        "Featued Image URL" : featured_image_url,
        "Mars Facts HTML Table" : mars_facts_html_table,
        "Hemisphere Image URLs" : hemisphere_image_urls
    }

    # return results
    return mars_data