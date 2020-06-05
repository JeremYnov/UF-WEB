<template>
  <section class="current-orders">
    <h2 class="section-title">Commandes en cours</h2>
    <div
      class="alert alert-warning"
      role="alert"
      v-if="restaurant.ordersInProgress.length == 0"
    >
      Aucune commande en cours
    </div>
    <table
      class="table table-striped"
      v-if="restaurant.ordersInProgress.length > 0"
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
          v-for="currentOrder in restaurant.ordersInProgress"
          :key="currentOrder.id"
        >
          <td>{{ currentOrder.id }}</td>
          <td>{{ currentOrder.restaurant.name }}</td>
          <td>{{ currentOrder.restaurant.address | truncate(40) }}</td>
          <td>{{ restaurant.name }}</td>
          <td>{{ restaurant.mail }}</td>
          <td>{{ currentOrder.total }}€</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
export default {
    props: {
    restaurant: null,
  },
  filters: {
    truncate: function(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    },
  },
};
</script>

<style></style>
