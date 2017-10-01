# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import urllib2
response = urllib2.urlopen('http://python.org/')
print "Response:", response

# Pega a real URL 
print "The URL is: ", response.geturl()

# Pega o codigo
print "Esse eh o codigo: ", response.code

# Pega os cabecalhos
# This returns a dictionary-like object that describes the page fetched, 
# particularly the headers sent by the server
print "The Headers are: ", response.info()

# Get the date part of the header
print "The Date is: ", response.info()['date']

# Get the server part of the header
print "The Server is: ", response.info()['server']

# Get all data
html = response.read()
print "Get all data: ", html

# Get only the length
print "Get the length :", len(html)

# Showing that the file object is iterable
for line in response:
 print line.rstrip()

# Note that the rstrip strips the trailing newlines and carriage returns before
# printing the output.