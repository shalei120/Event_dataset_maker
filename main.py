import os,sys
import urllib2
import copy

from bs4 import BeautifulSoup
from distutils.filelist import findall

def Get_wiki_event_page_list():
    website = 'https://en.wikipedia.org/wiki/Portal:Current_events/'#January_2009'
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    years = range(2006,2018)
    for year in years:
        for month in months:
            web = website + month + '_' + year
            contents = urllib2.urlopen(web)
            soup = BeautifulSoup(contents, "html.parser")
            for tag in soup.find_all('li'):
                str = tag.get_text()
                print str


if __name__ == '__main__':
    # Get_wiki_event_page_list()
    website = 'https://en.wikipedia.org/wiki/Portal:Current_events/January_2009'
    contents = urllib2.urlopen(website)
    soup = BeautifulSoup(contents, "html.parser")

    title2website = {}

    for tag in soup.find_all('li'):
        str = copy.copy(tag)
        elelist = str.contents
        # if elelist[0] == None:
        # print type(type(elelist[0]).__str__)
        if type(elelist[0]) == type(tag):
            # print elelist[0].__str__()
            if elelist[0].__str__().startswith('<a '):
                if len(elelist) == 1 or elelist[1].__str__()=='\n':
                    if ':' not in elelist[0].get('href') and '//' not in elelist[0].get('href') and elelist[0].get('accesskey')==None:
                        title2website[elelist[0].get_text()] = elelist[0].get('href')
                        # print elelist

    print title2website