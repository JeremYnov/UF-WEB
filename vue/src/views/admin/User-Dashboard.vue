<template>
  <div class="sidebar-wrapper" v-if="user != null">
    <Sidebar />
    <div class="main_content">
      <ProfileHero :user="this.user" />
      <h2 class="section-title">Commandes en cours</h2>
      <div
        class="alert alert-warning"
        role="alert"
        v-if="user.ordersInProgress.length == 0"
      >
        Aucune commande en cours
      </div>
      <table
        class="table table-striped"
        v-if="user.ordersInProgress.length > 0"
      >
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
          <tr
            v-for="currentOrder in user.ordersInProgress"
            :key="currentOrder.id"
          >
            <td>{{ currentOrder.id }}</td>
            <td>{{ currentOrder.restaurant.name }}</td>
            <td>{{ currentOrder.restaurant.address | truncate(40) }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.mail }}</td>
            <td>{{ currentOrder.total }}€</td>
          </tr>
        </tbody>
      </table>
      <h2 class="section-title">Historiques des commandes</h2>
      <div
        class="alert alert-warning"
        role="alert"
        v-if="user.ordersHistoric.length == 0"
      >
        L'utilisateur n'a jamais commandé
      </div>
      <table class="table table-striped" v-if="user.ordersHistoric.length > 0">
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
          <tr
            v-for="historicOrder in user.ordersHistoric"
            :key="historicOrder.id"
          >
            <td>{{ historicOrder.id }}</td>
            <td>{{ historicOrder.restaurant.name }}</td>
            <td>{{ historicOrder.restaurant.address | truncate(40) }}</td>
            <td>{{ user.firstName }}</td>
            <td>{{ user.mail }}</td>
            <td>{{ historicOrder.total }}€</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProfileHero from "@/components/hero/profile-hero.vue";
import Sidebar from "@/components/layouts/sidebar.vue";

export default {
  components: {
    ProfileHero,
    Sidebar,
  },
  data: function() {
    return {
      user: null,
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
  methods: {
    async getMemberProfile() {
      const response = await axios
        .get("/api/admin/member/" + this.$route.params.id + "/profile")
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.user = response.data.results;
      console.log(this.user);
    },
    
  },
  mounted: function() {
    this.getMemberProfile();
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
