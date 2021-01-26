from dateutil import parser
import datefinder

log = "<30>Jan 03 15:15:29 localhost alert: {id=706222} {time=2020-01-03 15:15:23} {level=6} {levelLang=漏洞扫描事件} {name=Download File-CMD} {nameLang=下载文件-cmd} {dev=system-172.31.6.40} {sip=203.208.60.123} {dip=192.168.0.9} {sport=57866} {dport=80} {shost=203.208.60.123} {dhost=mail.cstec.org:80} {__sName__=web} {sysurl=/sys/ds_list_read.php?sName=web&level=6&id=706222} {code=301} {reason=一般来说，病毒木马、漏洞利用poc、网络爬虫，才会不通过浏览器下载文件。如果源IP来自办公网或服务器，请检查是否是病毒行为。如果是误报，请把当前下载工具标识添加到白名单：“mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)”。本事件对每台主机每12小时只记录3次。} {info=/robots.txt} {desc=发现利用非浏览器程序、cmd命令行下载文件，有可能是网络爬虫、恶意扫描、植入木马行为。} {dheader=HTTP/1.1 301 Moved Permanently"
log2 = "<129> 2020-08-14 14:20:46 System_ID=HOST Logcategory=Webfilter Protocol=HTTP Type=Spylist Client_IP=192.168.12.171 Server_IP=149.20.56.32 Http_Method=GET URL=149.20.56.32/search?q=0 Rating_id=Phishing and ID Theft Malware=Phone Home Action=blocked "
log3 = """
<141>Apr 17 19:56:25 科技园 IPS: SerialNum=100JM-0S3B8-27009-J3723-GGH63 GenTime="2020-04-17 19:56:25" UserID=2 UserName=172.21.41.226 SrcIP=172.21.41.226 DstIP=203.208.40.38 Protocol=TCP SrcPort=61008 DstPort=80 SrcMac=58:8d:09:12:a7:40 DstMac=80:fb:06:af:8a:d5 AppName=Google通行证 RuleID=1 EventID=0x125eaa EventSet=All EventName="Web 疑似代码执行 [命令执行]" EventType=命令执行 ProtocolType=HTTP Action=drop
"""

matches = datefinder.find_dates(text=log3, strict=False, index=True, source=True)

print(matches)

for match in matches:
    print(match)