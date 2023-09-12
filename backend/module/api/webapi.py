from fastapi import FastAPI, BackgroundTasks
from time import sleep
from module.crawler.bots import start_bot, task_list, init_bot


router = FastAPI()
init_path = ""


@router.on_event("startup")
async def startup_event():
    import os
    global init_path
    init_path = os.getcwd()


@router.get("/api/tags", tags=["Proxy"])
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
    

@router.get("/api/start", tags=["Bot"])
async def t(background_tasks: BackgroundTasks):
    background_tasks.add_task(start_bot)
    return "ok"


@router.get("/api/task", tags=["Bot"])
async def status():
    return task_list


@router.get("/api/local", tags=["file"])
async def test():
    import os, json
    if os.path.exists(init_path+"/download/index.json"):
        with open(init_path+"/download/index.json", "r") as f:
            return json.load(f)
    else:
        return []