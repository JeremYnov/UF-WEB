<template>
  <div class="restaurant">
    <div
      class="restaurant-hero"
      v-bind:style="{ 'background-image': 'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),'+'url(' + restaurant.logo.url + ')' }"
    >
      <div class="restaurant-hero-content">
        <h1>{{restaurant.name}}</h1>
        <p>{{restaurant.address}}</p>
        <p>{{restaurant.category}}</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data: function() {
    return {
      restaurant: null,
      plates: null
    };
  },
  mounted: function() {
    this.getRestaurantPlate();
  },
  methods: {
    async getRestaurantPlate() {
      const response = await axios
        .get("/api/restaurant/" + this.$route.params.id + "/plates")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });
      this.restaurant = {
        id: response.data.results.id,
        name: response.data.results.name,
        category: response.data.results.category,
        logo: {
          url: response.data.results.logo.url,
          name: response.data.results.logo.name
        },
        address: response.data.results.address,
        mail: response.data.results.mail,
        creation: response.data.results.creation,
        selection: response.data.results.selection
      };

      this.plates = response.data.results.plates;
    }
  }
};
</script>
