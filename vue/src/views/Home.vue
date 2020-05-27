<template>
  <div class="home-container">
    <Hero />

    <section class="our-selection">
      <h2 class="section-title">Notre selection</h2>
      <div class="grid33-33-33">
        <RestaurantCard v-for="restaurant in lastRestaurant" :key="restaurant"/>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Hero from "@/components/hero/hero.vue";
import RestaurantCard from "@/components/restaurant-card.vue";

import axios from "axios";

export default {
  name: "Home",
  components: {
    // HelloWorld,
    Hero,
    RestaurantCard
  },
  data() {
    return {
      selectRestaurant: null,
      lastRestaurant: null
    };
  },
  mounted() {
    this.getSelection();
    this.getLastRestaurant();
  },
  methods: {
    async getSelection() {
      const response = await axios
        .get("/api/restaurant/selection")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      
      this.selectRestaurant = response.data.results;
    },
    async getLastRestaurant() {
      const response = await axios
        .get("/api/restaurant/last")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.lastRestaurant = response.data.results;
    }
  }
};
</script>
