import json
import requests
from urllib import parse
from bs4 import BeautifulSoup
from urllib.parse import quote
from requests.packages.urllib3 import disable_warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)


class addr2locTGOS(): 
    def __init__(self): 
        self.sess = requests.Session()
    def cookie_maker(self, session):
        cookie_dict = session.cookies.get_dict()
        cookie_list = [k + "=" + v for k, v in cookie_dict.items()]
        cookie = "; ".join(item for item in cookie_list)
        return cookie
    def address_transformer(self, address, pagekey="mzUDx/damjylIZO4IrPmo4A6oQX6m0xV"): 
        add = quote(address)
        # get
        url_1 = f"https://map.tgos.tw/TGOSCloud/Web/Map/TGOSViewer_Map.aspx?addr={add}"
        headers = {
            "Host": "map.tgos.tw", 
            "Connection": "keep-alive", 
            "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'", 
            "sec-ch-ua-mobile": "?0", 
            "sec-ch-ua-platform": "'Windows'", 
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", 
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Sec-Fetch-Site": "none", 
            "Sec-Fetch-Mode": "navigate", 
            "Sec-Fetch-User": "?1", 
            "Sec-Fetch-Dest": "document", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
        }
        rsp = self.sess.get(url_1, headers=headers, verify=False)
        Cookie = self.cookie_maker(self.sess)
        # post 
        url_2 = f"https://map.tgos.tw/TGOSCloud/Generic/Utility/UG_Handler.ashx?method=GetSessionID&pagekey={pagekey}"
        data = {
            "method": "GetCurrentAccount", 
            "pagekey": pagekey
        }
        headers = {
            "Host": "map.tgos.tw", 
            "Connection": "keep-alive", 
            "Content-Length": "0", 
            "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'", 
            "Accept": "*/*", 
            "X-Requested-With": "XMLHttpRequest", 
            "sec-ch-ua-mobile": "?0", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", 
            "sec-ch-ua-platform": "'Windows'", 
            "Origin": "https://map.tgos.tw", 
            "Sec-Fetch-Site": "same-origin", 
            "Sec-Fetch-Mode": "cors", 
            "Sec-Fetch-Dest": "empty", 
            "Referer": url_1, 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
            "Cookie": Cookie
        }
        rsp = self.sess.post(url_2, headers=headers, data=data, verify=False)
        res = json.loads(rsp.text)
        # post
        url_3 = f"https://map.tgos.tw/TGOSCloud/Generic/Project/GHTGOSViewer_Map.ashx?pagekey={pagekey}"
        data = {
            "method": "querymoiaddr", 
            "address": address, 
            "useoddeven": "false", 
            "sid": res["id"], 
        }
        headers = {
            "Host": "map.tgos.tw", 
            "Connection": "keep-alive", 
            "Content-Length": "{}".format(len(parse.urlencode(data))), 
            "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'", 
            "Accept": "*/*", 
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
            "X-Requested-With": "XMLHttpRequest", 
            "sec-ch-ua-mobile": "?0", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", 
            "sec-ch-ua-platform": "'Windows'", 
            "Origin": "https://map.tgos.tw", 
            "Sec-Fetch-Site": "same-origin", 
            "Sec-Fetch-Mode": "cors", 
            "Sec-Fetch-Dest": "empty", 
            "Referer": url_1, 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
            "Cookie": Cookie
        }
        rsp = self.sess.post(url_3, headers=headers, data=data, verify=False)
        res = json.loads(rsp.text)
        X = res["AddressList"][0]["X"]
        Y = res["AddressList"][0]["Y"]
        return X, Y
    def location_transformer(self, X, Y): 
        # get
        url = "https://ts01.gi-tech.com.tw/waterAbnormal/trancoor/trancoor.aspx"
        headers = {
            "Host": "ts01.gi-tech.com.tw", 
            "Connection": "keep-alive", 
            "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'", 
            "sec-ch-ua-mobile": "?0", 
            "sec-ch-ua-platform": "'Windows'", 
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", 
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Sec-Fetch-Site": "none", 
            "Sec-Fetch-Mode": "navigate", 
            "Sec-Fetch-User": "?1", 
            "Sec-Fetch-Dest": "document", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
        }
        rsp = self.sess.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(rsp.text, "html.parser")
        __VIEWSTATE = soup.find("input", {"name": "__VIEWSTATE", "id": "__VIEWSTATE"})["value"]
        __VIEWSTATEGENERATOR = soup.find("input", {"name": "__VIEWSTATEGENERATOR", "id": "__VIEWSTATEGENERATOR"})["value"]
        __EVENTVALIDATION = soup.find("input", {"name": "__EVENTVALIDATION", "id": "__EVENTVALIDATION"})["value"]
        # post
        data = {
            "__ASYNCPOST": "true", 
            "__EVENTARGUMENT": "", 
            "__EVENTTARGET": "", 
            "__EVENTVALIDATION": __EVENTVALIDATION, 
            "__VIEWSTATE": __VIEWSTATE, 
            "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR, 
            "btn_Tran97to84": "TWD97轉WGS84", 
            "rbl_Setting": "1", 
            "ScriptManager1": "UpdatePanel1|btn_Tran97to84", 
            "txt_TWD97_X": X, 
            "txt_TWD97_X_2": "", 
            "txt_TWD97_Y": Y, 
            "txt_TWD97_Y_2": "", 
            "txt_WGS84_E": "", 
            "txt_WGS84_N": "", 
        }
        headers = {
            "Host": "ts01.gi-tech.com.tw", 
            "Connection": "keep-alive", 
            "Content-Length": "{}".format(len(parse.urlencode(data))), 
            "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'", 
            "sec-ch-ua-mobile": "?0", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", 
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
            "Cache-Control": "no-cache", 
            "X-Requested-With": "XMLHttpRequest", 
            "X-MicrosoftAjax": "Delta=true", 
            "sec-ch-ua-platform": "'Windows'", 
            "Accept": "*/*", 
            "Origin": "https://ts01.gi-tech.com.tw", 
            "Sec-Fetch-Site": "same-origin", 
            "Sec-Fetch-Mode": "cors", 
            "Sec-Fetch-Dest": "empty", 
            "Referer": "https://ts01.gi-tech.com.tw/waterAbnormal/trancoor/trancoor.aspx", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
        }
        rsp = self.sess.post(url, headers=headers, data=data, verify=False)
        soup = BeautifulSoup(rsp.text, "html.parser")
        txt_WGS84_E = soup.find("input", {"name": "txt_WGS84_E", "id": "txt_WGS84_E"})["value"]
        txt_WGS84_N = soup.find("input", {"name": "txt_WGS84_N", "id": "txt_WGS84_N"})["value"]
        return txt_WGS84_N + "," + txt_WGS84_E

class addr2locGOOG(): 
    def __init__(self): 
        self.sess = requests.Session()
    def cookie_maker(self, session):
        cookie_dict = session.cookies.get_dict()
        cookie_list = [k + "=" + v for k, v in cookie_dict.items()]
        cookie = "; ".join(item for item in cookie_list)
        return cookie
    def location_transformer(self, address):
        url = "https://www.google.com/maps/place?q=" + address
        headers = {
            "Host": "www.google.com", 
            "Connection": "keep-alive", 
            "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'", 
            "sec-ch-ua-mobile": "?0", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36", 
            "sec-ch-ua-arch": "'x86'", 
            "sec-ch-ua-platform-version": "'10.0.0'", 
            "sec-ch-ua-full-version": "'100.0.4896.127'", 
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Upgrade-Insecure-Requests": "1", 
            "sec-ch-ua-bitness": "'64'", 
            "sec-ch-ua-model": "''", 
            "sec-ch-ua-platform": "'Windows'", 
            "Sec-Fetch-Site": "same-origin", 
            "Sec-Fetch-Mode": "navigate", 
            "Sec-Fetch-Dest": "empty", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
        }
        rsp = self.sess.get(url, headers=headers, verify=False, allow_redirects=False)
        soup = BeautifulSoup(rsp.text, "html.parser")
        url = soup.find("a", string="here")["href"]
        headers.update({"Cookie": rsp.headers["Set-Cookie"]})
        rsp = self.sess.get(url, headers=headers, verify=False, allow_redirects=False)
        soup = BeautifulSoup(rsp.text, "html.parser")
        text = soup.prettify()
        initial_pos = text.find(";window.APP_INITIALIZATION_STATE")
        data = text[initial_pos+36:initial_pos+85]
        data = data.split(",")
        location = "{},{}".format(data[2], data[1])
        return location


if __name__ == "__main__": 
    tgos = addr2locTGOS()
    X, Y = tgos.address_transformer(address="高雄市新興區青年一路156號")
    tgos.location_transformer(X=X, Y=Y)
    
    goog = addr2locGOOG()
    goog.location_transformer(address="高雄市新興區青年一路156號")