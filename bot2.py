import requests
page = 0
totalData = []
import json
while True:
    print('Page:', page)

    headers = {
        'authority': 'www.opentable.com',
        'content-length': '0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'accept-language': 'en-US',
        'sec-ch-ua-mobile': '?0',
        'ot-originaluri': '/seattle-washington-restaurant-listings',
        'ot-originalhost': 'www.opentable.com',
        'ot-requestid': 'ae209be0-6f19-4c97-a525-55cc1a7d5279',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'ot-anonymousid': '21F7A0CA-24BA-4549-8032-F9E0098897CB',
        'csrf-token': 'zQssI1EX-KaStL_hpSwdmy0wEeoomtr53Djc',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'ot-domain': 'com',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.opentable.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.opentable.com/seattle-washington-restaurant-listings',
        'cookie': '_csrf=5eb6155c-a2c2-487d-8c55-12f7cf338a15; otuvid=21F7A0CA-24BA-4549-8032-F9E0098897CB; _gid=GA1.2.513657427.1631082337; __gads=ID=fe70791418a0632a-220f9cba92cb004e:T=1631082335:S=ALNI_Mb7h3U-VhzM6gR4RaX0t13ozM6NRw; _gcl_au=1.1.1516567218.1631082338; _fbp=fb.1.1631082337000.0.07053157427937795; OT-SessionId=e88536b1-6053-454e-b533-626a42de31ca; bm_mi=8383E0AB92E147739BE55376B84208D5~vOONsALWTCO4ZHkxwb6DOTJFWf709j/w/BPFhZy8JWdvEcA3qm0SdVLtzubHpgQdWXENmfxIWo2QGIK00LUqbNGZauA5ewENTdEzD4abL/woS8XJE/Ym76UlOHg8+5D9/mzEwP7b/Af1Mfdjtf2rCeo1FMp6p+ivFJTCkEBGpwdtqKHMYl+3TRM9dwh4oa0Hsdv4x3N8BNP+OxaCJ2M1yYwR4zB6SqzndMRclWz++vToMoa/sL4shIRVzBoo2yFuCFrmG9Lwo2lxW18Y+V6cZA==; ak_bmsc=04625A9CCF3D7D4704676FEC0660FD5D~000000000000000000000000000000~YAAQDT/LFx0h1ap7AQAAP8qFxA032YKT9nUt2jrFcnaINKeYKCaZJ9icGXPqS7zyW5Caap2Fon3fB2okppHBWJle84iThJWgSQcNJu6LNeBJ6TFWJla2QXcz5ztIQAzWU4NFT8gNBV7lCJuJ+H/IFDCSiivB1g9d4+qo7sQFg40+xAM/6y3jlfim08ZxE4OnW2EU42BgOsouECRr3WIo9CUyTuFf6WpunyCz2VkuV4ahKocUEkwgNFzu5jD02/j/Hz7X4wTzZvPo1M3l/l+PWGLuYlxnUeQnUD4GmarfYspYSoureeDEXZN71inOnjG+JcSsLm7cErxtZTd+o3a75FVet0EAKX97gDslipNkrDlWuXvlHpYOItoCSAWBlfBNiWldE/QwDLORSVH4J9teNCpBVRWUVvmQsHciJuI=; lvCKE=lvmreg=2%2C0&histmreg=322%2C0%7C2%2C0; ftc=x=2021-09-08T09%3A54%3A12&px=1&c=1&pt1=1&pt2=1&er=0&p1ca=s&p1q=dateTime%3D2021-09-08T19%3A00%3A00&covers=2&latitude=47.615293&longitude=-122.308567&corrid=235832ef-a...; OptanonAlertBoxClosed=2021-09-08T08:54:16.573Z; OptanonConsent=isIABGlobal=false&datestamp=Wed+Sep+08+2021+14%3A39%3A17+GMT%2B0545+(Nepal+Time)&version=6.20.0&hosts=&consentId=0f7f50ea-0966-48e4-a428-cf5b7ea3f16b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0010%3A1&AwaitingReconsent=false&geolocation=NP%3BP4; _ga=GA1.2.1658123287.1631082337; _dc_gtm_UA-52354388-1=1; _uetsid=94fd5590106d11ecb4def78e40568238; _uetvid=94fd97b0106d11ec9b5761d368ee50c5; OT-Session-Update-Date=1631091265; bm_sv=B442BA5327C03100F454C805A1839C29~TKkqZojrJ2w4A2bewaXjZJY6HWRjOD9DvdM1D3hFqfgWLL2xBpkCEWt7uyKGreqzVVAtoEukmy5mccWQO08WO/mbo8CD8zal3XP1YAPDYJueuXtYnXhSvAqALJaUxL8rVEGeRthauS5g8++jGl6KATO5357RCm/PIilV13G3+jU=; _ga_Y7868SCB6E=GS1.1.1631089186.2.1.1631091302.60',
    }

    params = (
        ('covers', '2'),
        ('currentview', 'list'),
        ('datetime', '2021-09-08 19:00'),
        ('latitude', '47.613718'),
        ('longitude', '-122.313'),
        ('metroid', '2'),
        ('size', '100'),
        ('sort', 'Popularity'),
        ('from',page),
        ('PageType', '2'),
    
    )
    page = page + 100

    response = requests.post('https://www.opentable.com/s/node/api', headers=headers, params=params)
    results = response.json().get('Results').get('Restaurants')
    if results:
        totalData = totalData + response.json().get('Results').get('Restaurants')
    else:
        break


with open('opentable_restaurants_location.json', 'w') as outfile:
            json.dump(totalData, outfile,indent=4)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.opentable.com/s/node/api?covers=2&currentview=list&datetime=2021-09-08+19%3A00&latitude=47.613718&longitude=-122.313&metroid=2&size=100&sort=Popularity&from=100&PageType=2&CorrelationId=45781641-5891-44b1-8760-60700015a0c5', headers=headers)
