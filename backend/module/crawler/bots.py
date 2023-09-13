from .luogu_parser import pid_parser
from urllib import request
from time import sleep
import json, random, os


list_url = "https://www.luogu.com.cn/problem/list"
problem_url = "https://www.luogu.com.cn/problem/"
solution_url = "https://www.luogu.com.cn/problem/solution/"

task_list = []
failed_list = []
local_list = []
skip_list = []
total_num = 0
total_page = 0


def get_index():
    if os.path.exists("index.json"):
        with open("index.json", "r") as f:
            index = json.load(f)
            return index
    else:
        with open("index.json", "w") as f:
            json.dump([], f)
        return []
    

def update_index(index: dict):
    file = get_index()
    file.append(index)
    with open("index.json", "w") as f:
        json.dump(file, f)


def init_bot():
    # 初始化爬虫，对题目总数 total_num 和总页数 total_page 进行初始化
    rsp = request.urlopen(list_url + "?page=1&_contentOnly=1")
    js = json.loads(rsp.read())
    global total_num
    total_num = js["currentData"]["problems"]["count"]
    per_page = js["currentData"]["problems"]["perPage"]
    global total_page
    total_page = total_num // per_page + 1
    # 检查download文件夹是否存在
    if not os.path.exists("./download"):
        os.mkdir("./download")
    os.chdir("download")
    global local_list
    local_list = get_index()
    print("Total page: ", total_page, "Total num: ", total_num)
    print("bot init success")


def new_task(limit_num: int = 50, random_sleep: bool = True):
    # 新建任务
    task_count = 0

    def get_problem_list(page: int):
        # 获取第 {{ page }} 页的题目
        if random_sleep:
            sleep(random.randint(1, 3))
        rsp = request.urlopen(list_url + "?page=" + str(page) + "&_contentOnly=1")
        js = json.loads(rsp.read())
        return js["currentData"]["problems"]["result"]
    
    def check_is_local(dict: dict):
        with open("index.json", "r") as f:
            index = json.load(f)
            for i in index:
                if i["pid"] == dict["pid"]:
                    return True
        return False
    
    for i in range(1, total_page + 1):
        _task_list = get_problem_list(i)
        print("Now At Page: ", i)
        for task in _task_list:
            if task_count >= limit_num:
                return
            if not check_is_local(task):
                global task_list
                task_list.append(task)
                task_count += 1
                print("New Task: ", task["pid"], task["title"])


def start_task():
    def save_to_folder(task_dict: dict):
        folder_name = task_dict["pid"] + "-" + task_dict["title"]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        os.chdir(folder_name)
        pid_parser(task_dict["pid"])
        
    home_path = os.getcwd()
    while task_list != []:
        task = task_list.pop(0)
        try:
            os.chdir(home_path)
            print("saving " + task["pid"])
            save_to_folder(task)
            task.update({"loacl_path": os.getcwd()})
            os.chdir(home_path)
            update_index(task)
            sleep(random.randint(2, 4))
        except Exception as e:
            failed_list.append(task)
            print("failed" + task["pid"] + str(e))
            continue
    os.chdir("..")


def start_bot(task_num: int = 10, random_sleep: bool = True):
    init_bot()
    new_task(3, True)
    start_task()


if __name__ == "__main__":
    pass