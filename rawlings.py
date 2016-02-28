import urllib2
pageHtml = urllib2.urlopen('http://ufl.transloc.com/t/stops/4093246').read()
temp = '<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">'
startPos = pageHtml.find(temp)+len(temp)
endPos = pageHtml.find('<',startPos)
print('12 Rawlings Hall : ',pageHtml[startPos:endPos])

pageHtml = urllib2.urlopen('http://ufl.transloc.com/t/stops/4093766').read()
temp = '<td class="wait_time time_1" width="110px"><a href="/t/routes/4001170" title="View all of Butler Plaza">'
startPos = pageHtml.find(temp)+len(temp)
endPos = pageHtml.find('<',startPos)
print('12 Gatewat at gnv : ',pageHtml[startPos:endPos])

