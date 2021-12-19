<template>
  <div class="app">
    <post-from @create="createPost"/>
    <post-list :posts="posts" @remove="removePost" />
    <div class="btnpl">
      <button class="btn1" @click="fetchPosts">Добавить посты</button>
    </div>
  </div>
</template>

<script>
import PostFrom from "@/components/PostFrom";
import PostList from "@/components/PostList";
import axios from 'axios';
export default {
  components: {
    PostList, PostFrom
  },
  data() {
    return {
      posts: [],
    }
  },
  methods: {
    createPost(post) {
      this.posts.push(post);
    },
    removePost(post){
      this.posts = this.posts.filter(p => p.id !== post.id)
    },
    async fetchPosts() {
      try {
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts?_limit=10')
        this.posts = response.data
        console.log(response)
      } catch (e) {
        alert('Ошибка')
      }

    }
  }
}

</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  padding: 20px;
}

.btnpl {
  display: flex;
  flex-direction: column;
}

.btn1 {
  margin-top: 15px;
  align-self: flex-end;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
}

</style>