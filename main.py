import requests
import os
import re


def search(list):
    for word in list:
        dir_name = word
        os.mkdir(dir_name)
        #图片数量
        max_value = 120
        #步长
        current_value = 30
        image_index = 1
        header = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
        while current_value <= max_value:
            result = requests.get(url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11319404409353713183&ipn=rj&ct=201326592&is=&fp=result&queryWord={0}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={0}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn={1}&rn=30&gsm=3c&1600999963331='.format(word, current_value),
                             headers=header)
            json_bytes = result.content
            json_str = str(json_bytes, 'utf-8')
            html = re.findall('"middleURL":"(.*?)"', json_str)
            for url in html:
                if url != None:
                    print('正在下载图片:', url)
                    r = requests.get(url)
                    filename = dir_name + '/' + str(image_index).zfill(10) + ".png"
                    with open(filename, 'wb') as f:
                        f.write(r.content)
                        image_index += 1
            current_value += 30
        print('图片下载完成')


if __name__ == '__main__':
    f = input('请输入搜素关键词，用空格隔开')
    search(f.split())
