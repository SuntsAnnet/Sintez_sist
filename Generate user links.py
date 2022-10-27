'''
Generate user links
https://www.codewars.com/kata/57037ed25a7263ac35000c80
'''
from urllib.parse import quote
import urllib
def generate_link(user):
    baseUrl='http://www.codewars.com/users/'
    finalurl = baseUrl + urllib.parse.quote(user)
    return(finalurl)
