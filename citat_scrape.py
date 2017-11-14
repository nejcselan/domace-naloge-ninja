

from BeautifulSoup import BeautifulSoup as bs
import urllib2
import csv



html = urllib2.urlopen("http://quotes.yourdictionary.com/theme/marriage/")
response = html.read()


quote_soup = bs(response)
quotes = quote_soup.findAll("p", attrs={"class": "quoteContent"})

with open("citati.csv", "wb") as csv_file:
    for quote in quotes:
        print quote.text

        quote_writer = csv.writer(csv_file, delimiter=";")
        quote_writer.writerow([quote.text])


