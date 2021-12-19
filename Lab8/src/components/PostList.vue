<template>
  <div>
    <h3 v-if="posts.length > 0">Список пользователей</h3>
    <h3 v-else >Список пользователей ПУСТ </h3>
    <post-item v-for="post in posts" :post="post" :key="post.id" @remove="$emit('remove', post)"/>
  </div>

</template>

<script>
import PostItem from "@/components/PostItem";
export default {
  components: {
    PostItem
  },
  props: {
    posts: {
      type: Array,
      required: true,
    }
  }

}
</script>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
}

</style>