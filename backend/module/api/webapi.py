from fastapi import FastAPI, BackgroundTasks
from time import sleep
from module.crawler.bots import start_bot, task_list


router = FastAPI()
abc = [1,2,3,4,5,6,7,8,9,10]

def aaaa():
    while len(abc) > 0:
        abc.pop()
        sleep(5)

@router.get("/api/test", tags=["test"])
async def test():
    import urllib.request
    import json
    url = "https://www.luogu.com.cn/problem/list?page=1&_contentOnly"
    req = urllib.request.Request(url)
    json_data = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(json_data)
    return data


@router.get("/api/tags", tags=["test"])
async def tags():
    import urllib.request
    import json
    import time
    x = str(int(time.time()))
    url = "https://www.luogu.com.cn/_lfe/tags?page=1&_contentOnly" + "?_version=" + x
    req = urllib.request.Request(url)
    json_data = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(json_data)
    return data
    

@router.get("/api/start", tags=["test"])
async def t(background_tasks: BackgroundTasks):
    background_tasks.add_task(start_bot)
    return "ok"


@router.get("/api/task", tags=["status"])
async def status():
    return task_list
