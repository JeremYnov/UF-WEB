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
      <div class="filter-container">
        <button @click="getCategoryRestaurant('pizza')" class="category-button category-pizza">
          <div class="category-name">
            Pizza
          </div>
        </button>
        <button @click="getCategoryRestaurant('fast food')" class="category-button category-fast-food">
          <div class="category-name">
            Fast-Food
          </div>
        </button>
        <button @click="getCategoryRestaurant('sushi')" class="category-button category-sushi">
          <div class="category-name">
            Sushi
          </div>
        </button>
        <button @click="getCategoryRestaurant('asiatique')" class="category-button category-asiatique">
          <div class="category-name">
            Asiatique
          </div>
        </button>
        <button @click="getCategoryRestaurant('burger')" class="category-button category-burger">
          <div class="category-name">
            Burger
          </div>
        </button>
        <button @click="getCategoryRestaurant('japonais')" class="category-button category-japonais">
          <div class="category-name">
            Japonais
          </div>
        </button>
      </div>

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
