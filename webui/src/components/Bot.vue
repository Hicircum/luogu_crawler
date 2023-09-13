<template>
    <div class="bot-main">
        <div class="btn">
            <span>
                <el-button type="primary" size="small" plain @click="showList">{{ task_list_text }}</el-button>
                当前任务数：{{ task_num }}
            </span>
            <span>
                <el-button type="success" @click="startTask" :loading="buttonStatus">开始爬取</el-button>
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
import request from '../utils/request';

const task_num = ref(0);
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


const getTask = () => {
    request({
        url: '/api/task',
        method: 'get',
    }).then(res => {
        task_list.value = res.data;
        task_num.value = task_list.value.length;
    })
}


const startTask = () => {
    request({
        url: '/api/start',
        method: 'get',
    }).then(res => {
        console.log(res.data)
    })
    buttonWait.apply()
}

const buttonStatus = ref(false);
const buttonWait = () => {
  buttonStatus.value = true
  setTimeout(() => {
    buttonStatus.value = false
  }, 6000)
}
// 每隔1s执行一次gettask
setInterval(getTask, 1000);
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