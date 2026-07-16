<template>
  <div class="sidebar">
    <h2>Papers</h2>
    <div class="upload-area">
      <input
     ref="fileInput"
    type="file"
    accept=".pdf"
    style="display:none"
    @change="handleUpload"
      >
    <button @click="openFileDialog">
      Upload PDF
    </button>
    </div>
    <ul>
      <li
        v-for="paper in props.papers"
        :key="paper"
        @click="selectPaper(paper)"
      >
        {{ paper }}
      </li>
    </ul>

  </div>
</template>

<script setup>
import  { uploadPdf} from "../api/upload.js";
import { ref } from "vue";
const props = defineProps({
    papers: Array})
const emit = defineEmits(["selectPaper","refresh"])
console.log(props.papers)
function selectPaper(paper){
  emit("selectPaper",paper)
}
const fileInput = ref(null);

function openFileDialog() {
    fileInput.value.click();
}
async function handleUpload(event) {
    const file = event.target.files[0];
    const response = await uploadPdf(file)
    console.log(file);
}
</script>

<style scoped>
.sidebar{
    width:250px;
    min-width:250px;
    overflow:hidden;
    border-right: 1px solid var(--border);
    text-align: left;
    box-sizing: border-box;
    padding: 0 12px;
}

.sidebar ul{
    list-style: none;
    padding: 0;
    margin: 0;
}

.sidebar li{
    padding: 8px 4px;
    cursor: pointer;
    overflow-wrap: anywhere;
    border-bottom: 1px solid var(--border);
}

.sidebar li:hover{
    background: var(--accent-bg);
}


</style>