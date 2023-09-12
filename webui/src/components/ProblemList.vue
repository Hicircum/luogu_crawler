<template>
    <div class="table-container">
        <div class="btn">
            <span>
                <el-button type="success" @click="getLocalData">刷新列表</el-button>
            </span>
        </div>
        <div class="form">
            <el-table :data="data">
                <el-table-column prop="pid" label="操作" width="80">
                    <template #default="scope">
                        <el-button size="small" type="primary" @click="test()">打开</el-button>
                    </template>
                </el-table-column>
                <el-table-column prop="pid" label="题号" sortable width="120" />
                <el-table-column prop="title" label="题目名称" />

                <el-table-column>
                    <template #header>
                        <span class="fliter-btn"
                        @click="isDisplayStatus=!isDisplayStatus"
                        >{{ isDisplayStatus ? "显示算法" : "显示来源" }}</span> 标签
                    </template>
                    <template #default="scope">
                        <el-tag
                        v-for="i in scope.row.tags"
                        v-show="isDisplay(i)"
                        :disable-transitions="true"
                        type="success"
                        style="margin-left: 2px;margin-right: 2px;margin-top: 1px;margin-bottom: 1px;"
                        >{{ getTagName(i) }}</el-tag
                        >
                    </template>
                </el-table-column>

                <!-- 难度筛选 -->
                <el-table-column
                prop="difficulty"
                label="难度"
                :filters="[
                    { text: '暂无评定', value: 0 },
                    { text: '入门', value: 1 },
                    { text: '普及−', value: 2 },
                    { text: '普及/提高−', value: 3 },
                    { text: '普及+/提高', value: 4 },
                    { text: '提高+/省选−', value: 5 },
                    { text: '省选/NOI−', value: 6 },
                    { text: 'NOI/NOI+/CTSC', value: 7 }
                ]"
                :filter-method="filterDifficulty"
                filter-placement="bottom-end"
                >
                    <template #default="scope">
                        <el-tag>{{ difficulty[scope.row.difficulty] }}</el-tag>
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>

    <div class="test" v-for="i in datab">{{ i.pid }}</div>
</template>

<script setup>
import { ref } from 'vue';
import request from '../utils/request';

const data = ref();
const datab = ref();

function getLocalData(){
    request.get("/api/local").then((res) => {
        data.value = res.data;
        console.log(abc)
    });
}


let y = [];
// getLocalData();

let difficulty = {
    "0": "暂无评定",
    "1": "入门",
    "2": "普及−",
    "3": "普及/提高−",
    "4": "普及+/提高",
    "5": "提高+/省选−",
    "6": "省选/NOI−",
    "7": "NOI/NOI+/CTSC"
}

const filterDifficulty = (value, row) => {
    return row.difficulty === value
}

function getTagName(tagNum){
    let arrlen = y.tags.length;
    var i;
    for(i=0; i<arrlen; i++){
        if(y.tags[i].id == tagNum){
            return y.tags[i].name
        }
    }
    return "NoTag"
}

const isDisplayStatus = ref(true);
function isDisplay(Num){
    let arrlen = y.tags.length;
    var i;
    var typeNum=-1;
    for(i=0; i<arrlen; i++){
        if(y.tags[i].id == Num){
            typeNum = y.tags[i].type
            break
        }
    }
    if(!isDisplayStatus.value){
        if(typeNum == 2){
            return true
        }else{
            return false
        }
    }else{
        if(typeNum == 2){
            return false
        }else{
            return true
        }
    }
}
</script>

<style lang="less" scoped>
.table-container{
    display: flex;
    flex-direction: column;
    .btn{
        padding: 15px;
        display: flex;
        justify-content: end;
        align-items: center;
    }
    .fliter-btn{
        cursor: pointer;
        color: #409eff;
    }
}
</style>