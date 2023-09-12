<template>
    <div class="bot-main">
        <div class="btn">
            <span>
                <el-button type="primary" size="small" plain @click="showList">{{ task_list_text }}</el-button>
                当前任务数：{{ task_num }}
            </span>
            <span>
                <el-button type="primary">新建任务</el-button>
                <el-button type="success">开始爬取</el-button>
            </span>
        </div>
        <div class="list" v-show="task_list_show">
            <el-scrollbar height="200px">
                <el-tag size="large" v-for="i in task_list" style="margin: 5px;">{{ i.pid }}</el-tag>
            </el-scrollbar>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const task_num = ref(50);
const task_list = ref([]);
const task_list_text = ref("展开");
const task_list_show = ref(false);

function showList(){
    if(task_list_text.value == "展开"){
        task_list_show.value = true;
        task_list_text.value = "收起";
    }else{
        task_list_show.value = false;
        task_list_text.value = "展开";
    }
}


let x = [
    {
        "tags": [
            1
        ],
        "wantsTranslation": false,
        "totalSubmit": 1153624,
        "totalAccepted": 651586,
        "flag": 5,
        "pid": "P1001",
        "title": "A+B Problem",
        "difficulty": 1,
        "fullScore": 100,
        "type": "P"
    },
    {
        "tags": [
            3,
            19,
            82
        ],
        "wantsTranslation": false,
        "totalSubmit": 511263,
        "totalAccepted": 150962,
        "flag": 5,
        "pid": "P1002",
        "title": "[NOIP2002 普及组] 过河卒",
        "difficulty": 2,
        "fullScore": 100,
        "type": "P"
    }
]
console.log(x.length)
task_list.value = x;
task_num.value = x.length;

</script>

<style lang="less" scoped>
.bot-main{
    display: flex;
    flex-direction: column;
    .btn{
        padding: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .list{
        height: 200px;
    }
}
</style>