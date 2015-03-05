###############################################################################
# Twitter srcaper for the hashtag #bbcsms.
###############################################################################

import scraperwiki
import simplejson

# retrieve a page
base_url = 'http://search.twitter.com/search.json?q='
q = 'I'
options = '&rpp=100&page='
page = 1
import collections
cnt = collections.Counter()
cnt['I'] += 1

while 1:
    q = cnt.popitem()
    try:
        url = base_url + q + options + str(page)
        html = scraperwiki.scrape(url)
        #print html
        soup = simplejson.loads(html)
        for result in soup['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            for word in data['text']:
                cnt[word] += 1 
                
            data['from_user'] = result['from_user']
            # save records to the datastore
            scraperwiki.datastore.save(["id"], data) 
        page = page + 1
    except:
        print str(page) + ' pages scraped'
        break
        
    
