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
        .get("/api/restaurant/allRestaurant")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.allRestaurant = response.data.results;
      console.log(this.allRestaurant)
    },
  }

};
</script>


