import bs4, requests

def getMercadoLibrePrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price > div > div.ui-pdp-price__second-line > span > span.andes-money-amount__fraction')
    return elems[0].text.strip()

price = getMercadoLibrePrice ('https://articulo.mercadolibre.com.ar/MLA-1155297868-mouse-inalambrico-logitech-g-series-lightspeed-g603-negro-_JM?variation=175069697653#reco_item_pos=2&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-trend-recommendations&reco_id=311bb00a-288e-4576-bfd3-59177c6ad84b&c_id=/home/navigation-trends-recommendations/element&c_element_order=3&c_uid=79b3d9ae-51c2-453a-9054-6b3e9dda22ad')
print('The price is $' + price)                        
