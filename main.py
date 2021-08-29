import eel
import requests
from bs4 import BeautifulSoup


eel.init('web')

@eel.expose
def convertCurrency(ammount):
    RUB_DOLLAR = 'https://www.google.com/search?q=ruble+to+dollar&sxsrf=AOaemvKCUQg-oQqepTJizd3-a3U9BGEx9w%3A1630262487893&ei=19QrYcfbNdmExc8PpbeQ4A0&oq=ruble+&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQgAQyBQgAEIAEMgUIABDLATIFCAAQywEyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwguECcQkwI6BAgjECc6CggAEIAEEIcCEBQ6BAgAEEM6BwgAELEDEEM6CAgAEIAEELEDOgsILhCABBDHARCvAToICAAQsQMQgwE6CwgAEIAEELEDEIMBOgsILhCABBCxAxCDAToFCAAQsQM6CwgAEIAEEAoQARAqOgoIABCxAxCDARAKOgUILhCABDoJCAAQgAQQChABOgcILhCABBAKOgcIABCABBAKOg4ILhCABBDHARCvARCTAjoPCC4QgAQQxwEQrwEQChABOgkILhCABBAKEAE6DgguEIAEEAoQARAqEJMCOgYIABAKEB46BAgAEB46CAgAEAUQChAeOgQIABAKOgcIIxDqAhAnOg0ILhDHARCjAhDqAhAnOgsILhCABBDHARCjAjoOCC4QgAQQsQMQxwEQowI6CwguEIAEEMcBENEDOhQILhCABBCxAxCDARDHARDRAxCTAjoICC4QgAQQsQM6DgguEIAEELEDEMcBENEDOgoIABCxAxCDARBDOgcIABDJAxBDOgYIABAKEENKBAhBGABQ_LgjWMHgI2Dh6CNoCHABeACAAXmIAdgLkgEEMi4xMpgBAKABAbABCsABAQ&sclient=gws-wiz'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    full_page = requests.get(RUB_DOLLAR, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {'data-precision': '3'})
    k = convert[0].text.replace(',', '.')
    return float(k) * int(ammount)


eel.start('main.html', size=(750, 900))
