### 代码主要借鉴自 https://www.jianshu.com/p/c8b81dec24ff

import requests, re, time
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0'}
pages = []
page_n = 1
#获取音频ID模块
while 1:
    episode_id = '19421464' # 专辑编号，自行修改
    urls = 'https://www.ximalaya.com/youshengshu/%s/p%s'%(episode_id, str(page_n))
    html = requests.get(urls, headers=header)
#     time.sleep(2)
    regex = re.compile('href="/youshengshu/' + episode_id + '/(.*?)"')
    page = re.findall(regex, html.text)
    if page == []:
        break
    pages.extend(page)
    page_n += 1
#去重音频ID
pages = list(set(pages))
#排序音频ID
pages.sort()
#下载音频模块
for m in pages:
#     time.sleep(2)
    #开始拼接json网址
    json_usr = 'http://www.ximalaya.com/tracks/' + m + '.json'
    #开始提交json网址
    html_json = requests.get(json_usr, headers=header)
    #开始提取音频网址和音频名称
    music_url = html_json.json()['play_path_64']
    music_name = html_json.json()['title']
    #开始下载音频,保存为二进制数据
    music_data = requests.get(music_url,headers = header).content
    #下载到本地
    with open('%s.m4a'%music_name,'wb') as f:
        f.write(music_data)
        print('正在下载....',music_name)
