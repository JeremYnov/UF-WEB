<template>
  <div class="grid33-33-33">
    <div class="restaurant" v-for="restaurant in restaurants" :key="restaurant.id">
    <router-link v-bind:to="{ name: 'Restaurant', params: { id: restaurant.id } }">
        <div class="restaurant-image">
          <img v-bind:src="restaurant.logo.url" class="image" />
        </div>
        <div class="restaurant-name">
          <h3>{{restaurant.name}}</h3>
          <p>{{restaurant.address}}</p>
        </div>
        <div class="restaurant-category">
          <p>{{restaurant.category}}</p>
        </div>
        </router-link>
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
