<template>
  <section class="restaurant-presentation">
    <section class="toscew toscew-3">
      <div class="toscew-content center">
        <h1>
          Tous les restaurants
          <br />
          <span>disponibles sur EatYng</span>
        </h1>
      </div>
    </section>
    <div class="container wrapper">
      <!-- <div v-for="restaurant in allRestaurant" :key="restaurant.id"> -->
      <button @click="getCategoryRestaurant('pizza')">Pizza</button>
      <button @click="getCategoryRestaurant('fast food')">Fast food</button>
      <button @click="getCategoryRestaurant('sushi')">Sushi</button>
      <button @click="getCategoryRestaurant('asiatique')">Asiatique</button>
      <button @click="getCategoryRestaurant('burger')">Burger</button>
      <button @click="getCategoryRestaurant('japonais')">Japonais</button>

      <RestaurantCard :restaurants="allRestaurant" />
      <!-- <h1>{{restaurant.name}}</h1> -->
      <!-- </div> -->
    </div>
  </section>
</template>
<script>
import axios from "axios";
import RestaurantCard from "@/components/restaurant-card.vue";

export default {
  name: "Restaurants",
  components: {
    RestaurantCard
  },

  data() {
    return {
      allRestaurant: null
    };
  },

  mounted() {
    this.getAllRestaurant();
  },

  methods: {
    async getAllRestaurant() {
      const response = await axios
        .get("/api/restaurant/all")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.allRestaurant = response.data.results;
    },
    async getCategoryRestaurant(category) {
      const response = await axios
        .get("/api/restaurant/category/" + category)
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.allRestaurant = response.data.results;
    }
  }
};
</script>


