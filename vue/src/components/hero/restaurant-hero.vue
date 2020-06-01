<template>
  <div class="hero" v-bind:style="{ 'background-image': 'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),' + 'url(' + restaurantInfos.logo.url + ')' }">
      <div class="hero-content">
        <h1 class>{{ restaurantInfos.name }}</h1>
        <p class="restaurant-address">{{ restaurantInfos.address }}</p>
        <div class="restaurant-category">
          <p>{{ restaurantInfos.category }}</p>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  props: {
    restaurantInfos: null
  },
};
</script>