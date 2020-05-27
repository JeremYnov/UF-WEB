<template>
 <div class="grid33-33-33">
    <div class="restaurant" v-for="restaurant in restaurants" :key="restaurant.id">
      <a href="#">
        
        <div class="restaurant-image">
          <img v-bind:src="restaurant.logo.url"  class="image" />
        </div>
        <div class="restaurant-name">
          <h3>{{restaurant.name}}</h3>
          <p>{{restaurant.address}}</p>
        </div>
        <div class="restaurant-category">
          <i class="fas fa-tags"></i>
          <p>{{restaurant.category}}</p>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    restaurants: null
  }
};
</script>

<style lang="scss">
@import "../assets/scss/main.scss";
</style>