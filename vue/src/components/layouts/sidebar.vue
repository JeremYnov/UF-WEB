<template>
  <div class="sidebar">
      <h2>DashBoard</h2>
      <ul>
        <h3>Utilisateur</h3>
        <li>
            <router-link
            v-bind:to="{
              name: 'AdminMemberTableDashboard'
            }"
          >
           <i class="fas fa-home"></i>Membres</router-link>
        </li>
        <li>
          <router-link
            v-bind:to="{
              name: 'AdminRestaurantTableDashboard'
            }"
          ><i class="fas fa-user"></i>Restaurateurs</router-link>
        </li>
        <h3>Commande</h3>
        <li>
            <router-link
            v-bind:to="{
              name: 'AdminCurrentOrderTableDashboard'
            }"
          >
          <i class="fas fa-project-diagram"></i>En cours</router-link>
        </li>
        <li>
            <router-link
            v-bind:to="{
              name: 'AdminHistoryOrderTableDashboard'
            }"
          ><i class="fas fa-blog"></i>Historique</router-link>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
data: function() {
    return {
      chosenTable: 1
    };
  },
}
</script>

<style>

</style>