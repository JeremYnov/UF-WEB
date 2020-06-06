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
        <button
          @click="getCategoryRestaurant('fast food')"
          class="category-button category-fast-food"
        >
          <div class="category-name">
            Fast-Food
          </div>
        </button>
        <button
          @click="getCategoryRestaurant('indien')"
          class="category-button category-indien"
        >
          <div class="category-name">
            Indien
          </div>
        </button>
        <button
          @click="getCategoryRestaurant('healthy')"
          class="category-button category-healthy"
        >
          <div class="category-name">
            Healthy
          </div>
        </button>
        <button
          @click="getCategoryRestaurant('asiatique')"
          class="category-button category-asiatique"
        >
          <div class="category-name">
            Asiatique
          </div>
        </button>
        <button
          @click="getCategoryRestaurant('libanais')"
          class="category-button category-libanais"
        >
          <div class="category-name">
            Libanais
          </div>
        </button>
        <button
          @click="getCategoryRestaurant('gastronomie')"
          class="category-button category-gastronomie"
        >
          <div class="category-name">
            Gastronomie
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
import RestaurantCard from "@/components/card/restaurant-card.vue";

export default {
  name: "Restaurants",
  components: {
    RestaurantCard,
  },

  data() {
    return {
      allRestaurant: null,
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
    },
  },
};
</script>
