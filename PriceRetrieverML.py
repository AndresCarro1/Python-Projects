import bs4, requests

print ("Please paste the article's URL from Mercado Libre.")
article = input()

try:
    def getMercadoLibrePrice(productUrl):
        res = requests.get(productUrl)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#price > div > div.ui-pdp-price__second-line > span > span.andes-money-amount__fraction')
        return elems[0].text.strip()

    price = getMercadoLibrePrice (article)
    print('The price is $' + price)                        

except IndexError:
    print ("Sorry, could not find the product. Please try again later.")      
