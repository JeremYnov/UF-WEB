<template>
  <div class="home-container">
    <Hero />

    <section class="selection" id="our-selection">
      <h2 class="section-title">Notre selection</h2>
      <RestaurantCard :restaurants="selectRestaurant" />
    </section>

    <section class="toscew toscew-1">
      <div class="toscew-content right">
        <h1>
          Vos restaurants préférés
          <br />
          <span>sont sur EatYng</span>
        </h1>
      </div>
    </section>

    <section class="selection" id="last-selection">
      <h2 class="section-title">Les derniers arrivants</h2>
      <RestaurantCard :restaurants="lastRestaurant" />
    </section>
    <section class="toscew toscew-2">
      <div class="toscew-content left">
        <h1>
          Des plats gourmands 
          <br />
          <span>disponibles en 2 clics</span>
        </h1>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Hero from "@/components/hero/home-hero.vue";
import RestaurantCard from "@/components/card/restaurant-card.vue";

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


