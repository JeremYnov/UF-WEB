<template>
<section class="history-orders" v-if="historyOrders != null">
  <div
      class="alert alert-warning"
      role="alert"
      v-if="historyOrders.length == 0"
    >
      Aucune commande n'a été passée
    </div>
<table class="table table-striped" v-if="historyOrders.length != 0">
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
      <tr v-for="historyOrder in historyOrders" :key="historyOrder.id">
        <td>{{ historyOrder.id }}</td>
        <td>{{ historyOrder.restaurant.name}}</td>
        <td>{{ historyOrder.restaurant.address | truncate(40)}}</td>
        <td>{{ historyOrder.user.name}}</td>
        <td>{{ historyOrder.user.mail}}</td>
        <td>{{ historyOrder.total}}€</td>
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
      historyOrders: null
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

      this.historyOrders = response.data.results;
    }
  }
};
</script>