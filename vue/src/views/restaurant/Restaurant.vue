<template>
  <div class="restaurant">
    <div
      class="restaurant-hero"
      v-bind:style="{ 'background-image': 'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),'+'url(' + restaurant.logo.url + ')' }"
    >
      <div class="restaurant-hero-content">
        <h1 class>{{restaurant.name}}</h1>
        <p class="restaurant-address">{{restaurant.address}}</p>
        <div class="restaurant-category">
          <p>{{restaurant.category}}</p>
        </div>
      </div>
    </div>
    <section class="menu">
      <div class="grid33-33-33">
        <div class="plates" v-for="plate in plates" :key="plate.id">
          {{plate}}
          <div class="plate-container">
            <div class="plate-image">
              <img v-bind:src="plate.picture.url" alt />
            </div>
            <div class="plate-informations">
              <h2>{{plate.name}}</h2>
              <p>{{plate.content}}</p>
              <p>{{plate.unitPrice}}</p>
            </div>
          </div>
          <!-- <p v-if="plate.type == 'Menu'">Menu : {{plate.name}}</p>
          <p v-if="plate.type == 'Plate'">Plat : {{plate.name}}</p>
          <p v-if="plate.type == 'Dessert'">Dessert : {{plate.name}}</p>
          <p v-if="plate.type == 'Boisson'">Boisson : {{plate.name}}</p> -->
        </div>
      </div>
    </section>
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
