<template>
  <div class="dashboard-informations-container">
    <div class="dashbord dashbord-dark">
      <div class="icon-section">
        <i class="fa fa-users" aria-hidden="true"></i>
        <br />
        <small>Membres</small>
        <p>{{ numberUser }}</p>
      </div>
    </div>
    <div class="dashbord dashbord-clear">
      <div class="icon-section">
        <i class="fas fa-utensils" aria-hidden="true"></i>
        <br />
        <small>Restaurants</small>
        <p>{{ numberRestaurant }}</p>
      </div>
    </div>
    <div class="dashbord dashbord-dark">
      <div class="icon-section">
        <i class="fa fa-money" aria-hidden="true"></i>
        <br />
        <small>Revenus</small>
        <p>{{ profit }} €</p>
      </div>
    </div>
    <div class="dashbord dashbord-clear">
      <div class="icon-section">
        <i class="fas fa-cart-arrow-down" aria-hidden="true"></i>
        <br />
        <small>
          Commande(s)
          <br />en cours
        </small>
        <p>{{ numberOrderInProgress }}</p>
      </div>
    </div>
    <div class="dashbord dashbord-dark">
      <div class="icon-section">
        <i class="fas fa-shopping-cart" aria-hidden="true"></i>
        <br />
        <small>
          Total des
          <br />commandes
        </small>
        <p>{{ numberOrder }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      numberRestaurant: null,
      numberUser: null,
      numberOrderInProgress: null,
      numberOrder: null,
      profit: null
    };
  },
  mounted: function() {
    this.getDashboardData();
  },
  methods: {
    async getDashboardData() {
      const response = await axios
        .get("/api/admin/dashboard/data")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.numberRestaurant = response.data.results.numberRestaurant;
      this.numberUser = response.data.results.numberUser;
      this.numberOrderInProgress = response.data.results.numberOrderInProgress;
      this.numberOrder = response.data.results.numberOrder;
      this.profit = response.data.results.profit;
    }
  }
};
</script>

<style></style>
