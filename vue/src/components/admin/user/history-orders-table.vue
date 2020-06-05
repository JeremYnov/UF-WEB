<template>
  <section class="current-orders">
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
  </section>
</template>

<script>
export default {
  props: {
    user: null,
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