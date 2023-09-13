from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from time import sleep
from module.crawler.bots import start_bot, task_list, init_bot


router = FastAPI()
init_path = ""
enable_webui = False


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
    

if enable_webui:
    router.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")
    templates = Jinja2Templates(directory="templates")


    @router.get("/favicon.ico", tags=["html"])
    def favicon():
        return FileResponse("templates/favicon.ico")


    # HTML Response
    @router.get("/{full_path:path}", response_class=HTMLResponse, tags=["html"])
    def index(request: Request):
        context = {"request": request}
        return templates.TemplateResponse("index.html", context)