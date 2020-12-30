{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use beautiful soup to collect and append titles to list then take\n",
    "# first entry as top_news_title\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "nasa_news_titles = []\n",
    "\n",
    "results = soup.find_all(\"div\",class_=\"content_title\")\n",
    "\n",
    "for entry in results[1:-10]:\n",
    "    div_tag = entry.find(\"a\").text\n",
    "    nasa_news_titles.append(div_tag)\n",
    "top_news_title = nasa_news_titles[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#use beautiful soup to append paragraphs to list then take first entry as \n",
    "# news_p\n",
    "html2 = browser.html\n",
    "soup2 = BeautifulSoup(html2, 'html.parser')\n",
    "teasers = []\n",
    "\n",
    "results2 = soup2.find_all(\"div\",class_=\"article_teaser_body\")\n",
    "for entry2 in results2[0:]:\n",
    "    div_2 = entry2.text\n",
    "    teasers.append(div_2)\n",
    "\n",
    "news_paragraph = teasers[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find featured image on jpl.nasa.gov/spaceimages/?search=&category=Mars\n",
    "#click through data link to find expanded size img src\n",
    "url_3 = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url_3)\n",
    "html_3 = browser.html\n",
    "soup_3 = BeautifulSoup(html_3, 'html.parser')\n",
    "\n",
    "results_3 = soup_3.find_all(\"div\", class_=\"carousel_items\")\n",
    "for entry1 in results_3:\n",
    "    a_tag = entry1.find('a')\n",
    "    link_url='https://www.jpl.nasa.gov' + a_tag['data-link']\n",
    "    browser.visit(link_url)\n",
    "    html_4 = browser.html\n",
    "    soup_4 = BeautifulSoup(html_4, 'html.parser')\n",
    "    results_4 = soup_4.find('img', class_=\"main_image\")\n",
    "    a_tag_2= results_4['src']\n",
    "\n",
    "featured_image_url = 'https://www.jpl.nasa.gov' + a_tag_2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA19083_hires.jpg'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# URL for main image on scrolling carousel at any given time\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pull table data\n",
    "mars_facts_url = \"https://space-facts.com/mars/\"\n",
    "tables = pd.read_html(mars_facts_url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Data</th>\n",
       "      <th>Values</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Data                         Values\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# put data in dataframe\n",
    "mars_facts_df = tables[0]\n",
    "mars_facts_df.columns = ['Data','Values']\n",
    "mars_facts_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Values</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Data</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Values\n",
       "Data                                               \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# set index as Data\n",
    "mars_facts_df.set_index('Data', inplace=True)\n",
    "mars_facts_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Values</th>\\n    </tr>\\n    <tr>\\n      <th>Data</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Equatorial Diameter:</th>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>Polar Diameter:</th>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Distance:</th>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Period:</th>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>Surface Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>First Record:</th>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>Recorded By:</th>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use pandas function df.to_html() to create a table in HTML\n",
    "mars_facts_html_table = df.to_html()\n",
    "mars_facts_html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pull item class to grab link to hemisphere pages and use as list in for loop\n",
    "\n",
    "hemisphere_url =\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemisphere_url)\n",
    "html5 = browser.html\n",
    "soup_5 = BeautifulSoup(html5, 'html.parser')\n",
    "results_hem=soup_5.find_all('div',class_=\"item\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create containers for images and titles\n",
    "\n",
    "mars_hemisphere_images=[]\n",
    "mars_image_titles = []\n",
    "\n",
    "# Use for loop to visit pages; CSS selector for link because it is the most \n",
    "# precise direction while soup.find works well for the titles since the\n",
    "# class is title\n",
    "\n",
    "for result in results_hem:\n",
    "    a_tag_5 = result.find('a')\n",
    "    hemi_link = a_tag_5['href']\n",
    "    new_link = \"https://astrogeology.usgs.gov\" + hemi_link\n",
    "    browser.visit(new_link)\n",
    "    html6 = browser.html\n",
    "    soup_6 = BeautifulSoup(html6, 'html.parser')\n",
    "    selector = soup_6.select('li > a[href$=\"jpg\"]')\n",
    "    link_list = selector[0]\n",
    "    mars_hemisphere_images.append(link_list['href'])\n",
    "    find_titles = soup_6.find('h2', class_='title').text\n",
    "    mars_image_titles.append(find_titles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use for loop to append images and titles to dictionaries in a list\n",
    "hemisphere_image_urls=[]\n",
    "\n",
    "for x in range(4):\n",
    "    url_dict = {}\n",
    "    url_dict['title']=titles[x]\n",
    "    url_dict['image_url']=images[x]\n",
    "    hemisphere_image_urls.append(url_dict)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}