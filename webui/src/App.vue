<template>
    <div class="container">
        <div class="top">
            <Bot />
        </div>
        <div class="table">
            <ProblemList />
        </div>
    </div>
</template>

<script setup>
import Bot from './components/Bot.vue';
import ProblemList from './components/ProblemList.vue';
</script>

<style lang="less" scoped>
.container{
    display: flex;
    flex-direction: column;
    max-width: 1000px;
    margin: 30px auto;
    .top{
        box-sizing: border-box;
        padding: 15px;
        box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, .04), 0px 8px 20px rgba(0, 0, 0, .08);
        border-radius: 15px;
    }
    .table{
        margin-top: 25px;
        box-sizing: border-box;
        padding: 15px;
        box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, .04), 0px 8px 20px rgba(0, 0, 0, .08);
        border-radius: 15px;
    }
}
</style>