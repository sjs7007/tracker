import urllib2
def getTimings(stopName,stopUrl,waitUrl):
    pageHtml = urllib2.urlopen(stopUrl).read()
    startPos = pageHtml.find(waitUrl)+len(waitUrl)
    endPos = pageHtml.find('<ab',startPos)
    print(stopName,pageHtml[startPos:endPos]),

getTimings('Ra','http://ufl.transloc.com/t/stops/4093246','<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">')

#getTimings('Re','http://ufl.transloc.com/t/stops/4091138','<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">')
getTimings('Re','http://ufl.transloc.com/t/stops/4093250','<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">')

getTimings('G','http://ufl.transloc.com/t/stops/4093766','<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">')

getTimings('A','http://ufl.transloc.com/t/stops/4093774','<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">')


