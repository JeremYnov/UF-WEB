<template>
  <div class="sidebar-wrapper">
    <Sidebar />
    <div class="main_content">
      <RestaurantHero :restaurantInfos="restaurant" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import RestaurantHero from "@/components/hero/restaurant-hero.vue";
import Sidebar from "@/components/layouts/sidebar.vue";

export default {
  components: {
    RestaurantHero,
    Sidebar,
  },
  data: function() {
    return {
      restaurant: null,
    };
  },
  methods: {
    async getRestaurantDashboard() {
      const response = await axios
        .get("/api/admin/restaurant/" + this.$route.params.id + "/dashboard")
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
    this.getRestaurantDashboard();
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
