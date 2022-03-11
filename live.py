import http.client
def live():
    conn = http.client.HTTPSConnection("coinranking1.p.rapidapi.com")
    headers = {'x-rapidapi-host': "coinranking1.p.rapidapi.com",'x-rapidapi-key': "fbb91b8920msh0fa7611aea0b79fp11654ejsn093bddf1db21"}
    conn.request("GET", "/coin/Qwsogvtv82FCd/price?referenceCurrencyUuid=yhjMzLPhuIDl", headers=headers)
    res = conn.getresponse()
    data = res.read()
    live_price_d = (data.decode("utf-8"))
    return(live_price_d)