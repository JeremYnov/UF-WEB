<template>
  <section class="current-orders" v-if="currentOrders != null">
    <div
      class="alert alert-warning"
      role="alert"
      v-if="currentOrders.length == 0"
    >
      Aucune commande en cours
    </div>
    <table class="table table-striped" v-if="currentOrders.length != 0">
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
          <td>{{ currentOrder.restaurant.name }}</td>
          <td>{{ currentOrder.restaurant.address | truncate(40) }}</td>
          <td>{{ currentOrder.user.name }}</td>
          <td>{{ currentOrder.user.mail }}</td>
          <td>{{ currentOrder.total }}€</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      currentOrders: null,
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
        .get("/api/admin/all/order/progress")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.currentOrders = response.data.results;
    },
  },
};
</script>
