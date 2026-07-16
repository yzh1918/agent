
<template>
  <div class="container">
    <Sidebar :papers="papers"
    @select-paper="handleSelectPaper"
    @refresh="loadPapers"/>
    <chatwindow :paper="selectedPaper" />
  </div>

</template>

<script setup>
import { ref, onMounted } from "vue";
import { getPapers } from "./api/paper";
import Sidebar from "./components/Sidebar.vue";
import chatwindow from "./components/Chatwindow.vue";
const papers = ref([]);
const selectedPaper=ref("");
onMounted(() => {
    loadPapers();
});
async function loadPapers() {
    const response = await getPapers();
    papers.value = response.data.papers;
}
function handleSelectPaper(paper) {
    selectedPaper.value = paper;
    console.log(selectedPaper.value);
}
</script>

<style scoped>
.container{display: flex; flex: 1;}
</style>