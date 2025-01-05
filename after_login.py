import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,bn;q=0.8",
    "authorize": 'EAAAAAMRqGS4mWH/R62Hmsqk76/kHfh0CTuWuifAhChLHxKFbUM3ByYDMIasxVOrhExfcATr8koNANTDOqYFVbLXjqlPT5OvG9erwO4O1yyNkx0FPgHSwpGj9EK/6KzOWN1cpFRNOhezXN+dqLd0b5oZH1Q3f69elgYl/fYKkWRY9S4gc1W3UUQj9mZYOr7I6orcuDaAz0qy161U6cBzvfX+RBUxRCEUpS4FoimHn8XA+Ts/SUo9b32VzXmIk0BkETZ6y2cxI5fMvqO6eISci157MMCQEkwqeIv0vZs1Cz8bKtwtwTy3jbcR52wcxPEBR070eJdaJWbl3dWUXQ9nriVlrFQaoNSGp9z9akNnhpYAAYYJ+GCJpFHxxWHwyNV1vhSwcasInB0oQQv4OobUDeH2Eoif1gq4Fk0tv1DLKsyJ65kc2FuLYXT7Kqk/ViID28+eC4pSNdbbv1XybqofCgy4wZuFof+ttF8yUsJ/8MfhQEIc9Of8zNWefea46PvaTeMhakZK5GrkuR/nX+eKJsIEfvM=',
    "Cookie": 'rxVisitor=17336474398081I1DUK7PI98CTLJSD6U2HEUUIHA0UB20; OptanonAlertBoxClosed=2024-12-09T09:51:03.781Z; dtCookie=-10$2282GOOHDP87R3OOCLF693L4UHR4GO6A; rxvt=1734685591646|1734683791646; __cf_bm=I_fHGAW_qrSuiJYfYoqwnuVTvAtLSboSPpAJ5Q7lYQY-1734683815-1.0.1.1-1JgIyhY9vhbAhZBrltxRKIGsEO9oNNTIzQYY5XuqOVlor_ILWlPTuctfFCIUsCUTadoR8bYQa.VvTZlMTnu4zg; _cfuvid=E68yuWcekpu74tJ7JJMIofUDeoLzKZVNqbH9BeT2hrs-1734683815693-0.0.1.1-604800000; cf_clearance=kmFFFj21Yl5.XIv5IeCG0jz3cw2c4CXbRL96Z7TIRvs-1734683819-1.2.1.1-AGhC7oJ1FpSoHTKaX1PlhsZ4VJ.lwy6wfQBjgsLWng3ZT0HRKarE3_Rv.ATF4hmPw6kAffaeStatlizPPjflrI6EAoPyLeEItsePzSmMCge2hXn64tW6lrRx7lWxm8rQxfzGBgWwQQommE430clRDxsQVkhXzTkESpPx_diwMDA1Q7U4XyCn9CMTk4lspSLBxKDzZyU6nH_nz.KNaDoqH3bAODsXwNdTbj7RLgXiXpU23UoX1xDnJ4sUWzENVFBVhu6_An76d7ibmMSGzi9fvVgHf9KbmxKjFpS0mW4qxfptZgILC9t_HR7BarKij5DrTJ5RmD8NEJAnXRFNL.l6iU4DBRotlysk.nGGc9bjaum6rLXRe40IxDwlkOKlzDrVq8s2D8_ZLDMWTgG0ARQSA0W8ILs0gbU3lyHTiDwRHq4; dtPC=-10$83791643_920h1p-10$83819107_742h1p-10$83822134_937h1p-10$83846258_434h1p-10$83850089_532h1vJVRQQHGTRAHJEKFULIKUVUSKFSRAAKQK-0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+20+2024+14%3A37%3A31+GMT%2B0600+(Bangladesh+Standard+Time)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=eb2a3bb5-e28e-4bcc-81f6-cf07c03736f7&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false&intType=2&geolocation=BD%3BC; lt_sn=b83c731b-0a33-4521-91c8-39a25e580556',
    "cache-control": "no-cache",
    "clientsource": "MaqiVlL/EgJZaFsE0ISbLlDTvdeYLOWaMevRp7ETD3NAR3R4SyEVj2evBJ7DSru2/akcn9dKYSifLUTRoUl50jZl+bzaEc07RJ7hTGkGhvNeZG+2pM2m6mu7Vo9oCnSnW337EcxzGOZhny9Jrrmi2qZozSpofd8Wfsdx9cYaWcI=",
    "content-length": "1203",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://visa.vfsglobal.com",
    "pragma": "no-cache",
    "referer": "https://visa.vfsglobal.com/",
    "route": "npl/en/ltp",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
}

url = 'https://visa.vfsglobal.com/npl/en/ltp/dashboard'

response = requests.get(url, headers=headers)
html = response.content
print(html)
