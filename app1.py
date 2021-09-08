import requests
import json
total_data = []

page = 1
skipResults = 0
skipPopResults = 0

while True:
    
    print("Running for the page:::",page)
    headers = {
        # 'authority': 'www.opentable.com',
        # 'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        # 'ot-page-type': 'multi-search',
        'x-csrf-token': '57f4e495-d637-4c3a-b557-72c560e10e91',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-query-timeout': '11779',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.opentable.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
    # 'referer': 'https://www.opentable.com/s?dateTime=2021-09-08T19%3A00%3A00&covers=2&latitude=47.615293&longitude=-122.308567',
        'accept-language': 'ne-NP,ne;q=0.9,en-US;q=0.8,en;q=0.7',
        #'cookie': '_csrf=5eb6155c-a2c2-487d-8c55-12f7cf338a15; otuvid=21F7A0CA-24BA-4549-8032-F9E0098897CB; OT-SessionId=48fe92ba-c88c-42c2-9dc7-2fccc0b2d302; _gid=GA1.2.513657427.1631082337; __gads=ID=fe70791418a0632a-220f9cba92cb004e:T=1631082335:S=ALNI_Mb7h3U-VhzM6gR4RaX0t13ozM6NRw; ak_bmsc=62FE0532584DCC0FBD2A20EC2092E3AD~000000000000000000000000000000~YAAQMVstF9tfXrV7AQAABUwVxA3DAUKRMuwhumpJ+beUUbiUH1LGq6dN3DrAcwntif4Nx9ZV5+ld34kR9Hh5hNVzBUVgig3R7WF+TrDJC5/Z8w5hJLTEN4l3tH55t022VGtcodAnKKBRc1A5joacrhtbzNmF2pf7QLQMqY67IKN6zIdcai6AilYOv2Qk6h7xEDyZS2Ip1RpGjo8q33ky3fOEdPjIgox6GjnQTzEmbJ+jDljPwvP2X4EwZBgc+1kZxf4HAROdCBqPghRJm9hX8RUkRv32JigL+CvFytWSeGWxsttkHonHBuD1m5P5kK2h+OZR1nvwEBZsaoxtPACKVIVBN2nwcrwNYRMQn74jFvLSWYmZfa6CGd95HEChk8OCxAZZBDcNTS7H4L13Ub6nyBYgX0UytrCYBhviAeTpqeuixWio3G8sN2gJxU6CO+eLoFT+Pm5fozL8OcSGDNPgIabF3whGNZras37EeLH/bgMvQwEcTRcVjX1fjw==; _gcl_au=1.1.1516567218.1631082338; _fbp=fb.1.1631082337000.0.07053157427937795; ftc=x=2021-09-08T07%3A31%3A09&c=1&pt1=1&pt2=1; OptanonConsent=isIABGlobal=false&datestamp=Wed+Sep+08+2021+12%3A16%3A13+GMT%2B0545+(Nepal+Time)&version=6.20.0&hosts=&consentId=0f7f50ea-0966-48e4-a428-cf5b7ea3f16b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0010%3A1&AwaitingReconsent=false&geolocation=NP%3BP4; OptanonAlertBoxClosed=2021-09-08T06:31:13.259Z; _ga=GA1.2.1658123287.1631082337; _uetsid=94fd5590106d11ecb4def78e40568238; _uetvid=94fd97b0106d11ec9b5761d368ee50c5; _ga_Y7868SCB6E=GS1.1.1631081038.1.1.1631082836.60; OT-Session-Update-Date=1631082844; bm_sv=F7C92BE9B45348668765F1C7278D9D8B~gAN9tdDjQfxpNeK8kw386Oc7uKBrPnj1cu+uXR2m0UV0Y/Gc2nlrcXrmNFmuLWOZt2nYCEE1RnjkWaH6sKV/0WNbVrG8EpIF+V2x0FtaAl2xuL2eMcLOsKRpHpj4AQgwbYH/2go500iR+hpukfzOe+JRySo4+gekdRGhnwOLwjc=',
    }
    
    data_json = {"operationName":"MultiSearchRestaurants",
    "variables":{"limit":100,
    "popLimit":3,"skipResults":skipResults,
    "skipPopResults":skipPopResults,
    "diningType":"ALL",
    "sortBy":"WEB_CONVERSION","mods":["NO_INCENTIVE_PROMOTION"],
    "withAnytimeAvailability":True,
    "forwardMinutes":150,
    "backwardMinutes":150,
    "notWithAnytimeAvailability":False,
    "notWithFacets":False,
    "needRemodeledSearchFacets":True,
    "withFallbackToListingMode":False,
    "metroId":2,"metroIds":[2],
    "latitude":47.615293,
    "longitude":
    -122.308567,"tld":"com",
    "date":"2021-09-08",
    "time":"19:00","partySize":
    page,

    "onlyPop":False,"includePopRestaurants":True,
    "pinnedRid":None,"shouldIncludeDeliveryDetails":
    True,"shouldIncludeTakeoutDetails":True,
    "originalTerm":None,"intentModifiedTerm":None,
    "loyaltyRedemptionTiers":[],
    "experienceTypeIds":[],
    "withFacets":False,"withTags":True,
    "withLoyaltyRedemptionFacets":False,
    "withPointRedemptionRewards":False,
    "countryCode":"US"},"extensions":
    {"persistedQuery":{"version":1,
    "sha256Hash":
    "6422e11e02144f7aa2d89b7c85cccc9303fd9dfcc7b08e3ff6e33adc29e01043"}}}
    data = json.dumps(data_json)
    response = requests.post('https://www.opentable.com/dapi/fe/gql', headers=headers, data=data)
    response_data = response.json()
    required_data = response_data.get('data').get('restaurantSearch').get('restaurants')
    if required_data:
        total_data = total_data + required_data
        
    else:
        print('No data found')
        breakpoint()
        break
    page = page + 1
    skipPopResults = skipPopResults + 3
    skipResults = skipResults + 100
breakpoint()
with open('opentable_restaurants8.json', 'w') as outfile:
            json.dump(total_data, outfile,indent=4)

