<template>
  <div class="home-container">
      <Hero />
    
    <RestaurantCard />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Hero from "@/components/hero/hero.vue";
import RestaurantCard from "@/components/restaurant-card.vue";

export default {
  name: "Home",
  components: {
    // HelloWorld,
    Hero,
    RestaurantCard,
  }
};
</script>
