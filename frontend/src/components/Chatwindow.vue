<script setup>
  const props=defineProps({paper:String})
  import { ref } from "vue";
  const question = ref("");
  const messages = ref([]);
  async function sendMessage(){
    if (!question.value.trim()) {
    return;
}
    messages.value.push({
      role:"user",
      content:question.value
    })

    const response= await chat(
        props.paper,
        question.value
    );
    question.value="";
    messages.value.push({
      role:"assistant",
      content:response.data.answer
    })

  }
  import { chat } from "../api/chat.js"
</script>

<template>
  <div class="chatwindow">
    <h2>chat</h2>
    <p>Current Paper:</p>
    <p>{{ props.paper }}</p>
    <div class="message-area">
    <div v-for="(message,index) in messages"
    key="index",>
      <strong>{{message.role}}</strong>
      {{message.content}}
    </div>
  </div>
    <div class="input-area">

      <input
          @keyup.enter="sendMessage"
          v-model="question"
          type="text"
          placeholder="Ask something about this paper">
      <button @click="sendMessage">
        send</button>

    </div>
  </div>
</template>

<style scoped>
.chatwindow{
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.message-area{
  flex: 1;
  border: 1px solid #ddd;
  margin: 20px 0;
}

.input-area{display: flex;gap: 10px}
.input-area input{flex:1;padding: 10px}
.input-area button{padding:10px 20px}
</style>