<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">Commande N°</th>
        <th scope="col">Nom du client</th>
        <th scope="col">Mail du client</th>
        <th scope="col">Adresse du client</th>
        <th scope="col">Date de la commande</th>
        <th scope="col">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="order in orders" :key="order.id">
        <td>{{ order.id }}</td>
        <td>{{ order.user.name }}</td>
        <td>{{ order.user.mail }}</td>
        <td>{{ order.user.address }}</td>
        <td>{{ order.creationDate }}</td>
        <td>{{ order.total }}</td>
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
    this.getOrderHistoric();
  },
  methods: {
    async getOrderHistoric() {
      const response = await axios
        .get("/api/order/historic")
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
