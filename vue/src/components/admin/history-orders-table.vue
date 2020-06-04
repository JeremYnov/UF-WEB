<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">Commande N°</th>
        <th scope="col">Restaurant</th>
        <th scope="col">Adresse du restaurant</th>
        <th scope="col">Client</th>
        <th scope="col">Mail du client</th>
        <th scope="col">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="currentOrder in currentOrders" :key="currentOrder.id">
        <td>{{ currentOrder.id }}</td>
        <td>{{ currentOrder.restaurant.name}}</td>
        <td>{{ currentOrder.restaurant.address | truncate(40)}}</td>
        <td>{{ currentOrder.user.name}}</td>
        <td>{{ currentOrder.user.mail}}</td>
        <td>{{ currentOrder.total}}€</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      currentOrders: null
    };
  },
  filters: {
    truncate: function(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    },
  },
  mounted() {
    this.getAllOrderInProgress();
  },
  methods: {
    async getAllOrderInProgress() {
      const response = await axios
        .get("/api/admin/all/order/historic")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.currentOrders = response.data.results;
    }
  }
};
</script>