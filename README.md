# 洛谷爬虫
> **注意：本项目是软件工程个人作业，本人不保证其稳定性，仅供学习使用，请勿用于生产环境**  
> [课程链接](https://bbs.csdn.net/topics/617213407) [Internet Archive](https://web.archive.org/web/20230913062739/https://bbs.csdn.net/topics/617213407)

## 简介
本项目由前端（Vue3 + Element Plus）与后端（Fastapi）组成。可以爬取洛谷题目以及对应题解。

爬取结果结构如下：
```
download
  ├─P1000-超级玛丽游戏
  ├─P1001-A+B Problem
  ├─P1002-[NOIP2002 普及组] 过河卒
  └─index.json
```
其中`index.json`为自动生成的索引文件，请勿直接修改。

## 注意事项
请将 `backend\module\crawler\luogu_parser.py` 内 `def pid_parser(pid: str):` 函数内的cookie更换为有效cookie

## 源码运行
请确保你已经安装python、nodejs与git
```
git clone https://github.com/Hicircum/luogu_crawler.git
cd luogu_crawler
```
修改 `webui/src/utils/request.js` 内的 `baseURL: 'http://127.0.0.1:8000'` 为 `baseURL: ''`  
修改 `backend/module/api/webapi.py` 内的 `enable_webui` 为 `True`
```
构建前端
cd webui
npm install
npm run build
cd ..
```
将 `dist` 文件夹内的所有文件拷贝到`backend`的`templates`文件夹内，运行`main.py`即可。  
**注意：如果有报错找不到路径，请确保当前目录为 `backend` 文件夹**

## 运行打包文件
下载release中的 `luogu.zip` 安装相应的python包即可运行，如果你使用pycharm，可直接导入，pycharm会为你自动安装。
