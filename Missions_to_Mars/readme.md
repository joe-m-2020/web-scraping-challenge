In This challenge, in the script "scrape_mars.py" splinter was used to access a variety of web pages and data was scraped using Python and Beautiful Soup. The first data was collected 'https://mars.nasa.gov/news/' where ther top story was collected as well as teaser paragraph for this article.  
The next data was the scrolling image found on https://www.jpl.nasa.gov.  The link 'https://www.jpl.nasa.gov' was used to pull the full-sized image.
The third data point was a table of interesting facts about the planet Mars taken from "https://space-facts.com/mars/" using pd.read_html function to import the data into a dataframe and then df.to_html() was used to pass the table as html on the index page.
Lastly, the images of the four hemispheres of Mars were taken from "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" using Splinter, Python and Beautiful Soup.
This data was all saved in a dictionary to call from app.py using flask.

HTML button "GET DATA" was created to call the flask app to run the scrape_mars.py algorithm and populate the index.html page.