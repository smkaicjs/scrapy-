# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver


class ZhinianSpider(CrawlSpider):
    name = 'zhinian'
    allowed_domains = ['zhaoping.com']
    start_urls = ['https://sou.zhaopin.com/?jl=765&kw=python&kt=3']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS':{
'authority':'fe-api.zhaopin.com',
'method':'GET',
'path':'/c/i/user/site?at=a832230474d1427f9dbf1e1ed712e4b1&rt=a59f23d275b84298ada920c38125360e&_v=0.38087334&x-zp-page-request-id=c5ec4e470ce040a9894792606828f5b9-1585293646574-595104&x-zp-client-id=f24a29af-d3ea-44f2-af63-d4fa30ac5b2a&MmEwMD=5BHVIIBEfNHIAfR_2WA8_A5Exz._9HVgIZ_gWKVuyaPteA.pHlnCF0EoCS7uqM9U0sn6wdtVHlPHROEwiBTL0Pzt1p1Xt.Kg6yq6UQAogoSbUsE0_SCBgQOD9JWgh0.bTO7PQ7bDbjMWB1NZ8KrRb.slS6Tlo5ZIUtwJCzsHJv7LEbHYyP0wp4dwICYQDDqfXbuo_RpbakNxIm5iXy11_GN1GPaXgRjnzBPjzzh5b6CyxOodvDkNb.1s0NXTKl251efBdrv_pewdXaC3T4hJbr.QWCefipYNNkQ4TbUQjmK7y8NFRuQpGsZ5mn7yCcW2nZeycUdprJOxqDF3YMjO8Vs7Pk0d6MZ2QNrMT3Sf2AVG85Bn5EwaSK.aPaaUakMrvXnpU26KRVVCMVWkV_05a0KsV',
'scheme':'https',
'accept':'application/json, text/plain, */*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cookie':'x-zp-client-id=f24a29af-d3ea-44f2-af63-d4fa30ac5b2a; x-zp-device-id=68a482aa8b7ec3975bf011b7e4d938e7; c=36mUk0Zz-1584954215914-23de2895d048938051990; sts_deviceid=17106a20e3927c-0ae755c3a16d9e-3f6b4e04-1778000-17106a20e3a3cf; dywec=95841923; __utmc=269921210; _fmdata=1Lcxfel05Xufso2SYgnQ3%2BmESogzou40XVGyLfcerDOUL8FhDb5d2gi90MnCFjlc8CQYocTxDuDr16jiE0UJ9MGk2XKPPqzgJBXaH8jIK7k%3D; _xid=LxiGQyTihEHcbxyWYnZYzt1URi%2BdB%2B8w4ZzRH4hvtF7N9oEpEIlHF6fZeiqdPmJAG0VVI10A56EJ6xHtItngHg%3D%3D; adfbid=0; adfbid2=0; acw_tc=2760822415849542704844383e19fa0f1e1d05964b0be19168f4574fca599e; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com%2F; jobRiskWarning=true; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1584954270; JsNewlogin=3056954399; JSloginnamecookie=18208425928; JSShowname=%E6%96%BD%E6%98%8E%E5%9D%A4; uiioit=213671340f69446b5d6a59794c644a740e3500325e75526d5368427426733036083402694e6b8; ZP_OLD_FLAG=false; privacyUpdateVersion=3; POSSPORTLOGIN=2; CANCELALL=1; loginreleased=1; adfcid=none; adfcid2=none; urlfrom=121126445; urlfrom2=121126445; at=a832230474d1427f9dbf1e1ed712e4b1; Token=a832230474d1427f9dbf1e1ed712e4b1; rt=a59f23d275b84298ada920c38125360e; JSpUserInfo=3d692e695671467155775875516a5d7548775c695d6952714e715e772575276a59754177506958695b714f7151775b755c6a5d754277506951693e7139715877d410670c00224b772d692769567146715d775b75596a5c7544775a695f69527145715d772975586a527543774669096904711a715e773a753d6a5975417753692b693f714a71577744755d6a44754277596950695d714c7124772575546a55754b773d692b6956713d712c775875516a5d7548775c695d6952714e71517752753c6a30754d775969516938713e7158775a755a6a5f756; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221018984799%22%2C%22%24device_id%22%3A%2217106a20e413d7-04f7cb77873a0e-3f6b4e04-1778000-17106a20e426bf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2217106a20e413d7-04f7cb77873a0e-3f6b4e04-1778000-17106a20e426bf%22%7D; sts_sid=1711aadddff2d7-0053c3da8daced-3f6b4e04-1778000-1711aadde0075c; dywea=95841923.2296066846535022300.1584954216.1585227988.1585290545.12; dywez=95841923.1585290545.12.11.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utma=269921210.1874220739.1584954216.1585227988.1585290545.13; __utmz=269921210.1585290545.13.12.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/; LastCity=%E5%A4%A9%E6%B4%A5; LastCity%5Fid=531; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1585293290; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%225b8ae119-aeb3-460c-8ec2-e7b7eb08de4e-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22ef6717d9-2658-4cec-8fbc-8510113d10f8-job%22}}; sts_evtseq=16',
'origin':'https://sou.zhaopin.com',
'referer':'https://sou.zhaopin.com/?jl=531&kw=python&kt=3&sf=0&st=0',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }
    }

    #通过正则表达式判断哪些是我们想要的content
    rules = (
        Rule(LinkExtractor(allow='https://sou.zhaopin.com/' + '?jl=[0-9]*\&kw=python\&kt=3'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('找到一个页面，url是：',response.url)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item











