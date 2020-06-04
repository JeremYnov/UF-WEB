<template>
 <RestaurantHero :restaurantInfos="restaurant"/>
</template>

<script>
import axios from "axios";
import RestaurantHero from "@/components/hero/restaurant-hero.vue";

export default {
  components: {
    RestaurantHero,
  },
  data: function() {
    return {
      restaurant: null,
    };
  },
  methods: {
    async getRestaurantProfile() {
      const response = await axios
        .get("/api/restaurant/dashboard/restaurant/" + this.$route.params.id)
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.restaurant = response.data.results;
    },
  },
  mounted: function() {
    this.getRestaurantProfile();
  },
};
</script>
