<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">Commande N°</th>
        <th scope="col">Nom du client</th>
        <th scope="col">Mail du client</th>
        <th scope="col">Adresse du client</th>
        <th scope="col">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="inProgressOrder in orders" :key="inProgressOrder.id">
        <td>{{ inProgressOrder.id }}</td>
        <td>{{ inProgressOrder.user.name }}</td>
        <td>{{ inProgressOrder.user.mail }}</td>
        <td>{{ inProgressOrder.user.address }}</td>
        <td>{{ inProgressOrder.total }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      orders: null
    };
  },
  mounted: function() {
    this.getOrderInProgress();
  },
  methods: {
    async getOrderInProgress() {
      const response = await axios
        .get("/api/order/progress")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.orders = response.data.results;
    }
  }
};
</script>