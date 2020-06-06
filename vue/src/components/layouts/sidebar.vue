<template>
  <div class="sidebar">
    <h2>DashBoard</h2>

    <ul>
      <h3>Utilisateur</h3>
      <li>
        <router-link
          v-bind:to="{
            name: 'AdminMemberTableDashboard',
          }"
        >
          <i class="fas fa-user"></i>Membres</router-link
        >
      </li>
      <li>
        <router-link
          v-bind:to="{
            name: 'AdminRestaurantTableDashboard',
          }"
          ><i class="fas fa-concierge-bell"></i>Restaurateurs</router-link
        >
      </li>
      <h3>Commande</h3>
      <li>
        <router-link
          v-bind:to="{
            name: 'AdminCurrentOrderTableDashboard',
          }"
        >
          <i class="fas fa-project-diagram"></i>En cours</router-link
        >
      </li>
      <li>
        <router-link
          v-bind:to="{
            name: 'AdminHistoryOrderTableDashboard',
          }"
          ><i class="fas fa-history"></i>Historique</router-link
        >
      </li>
    </ul>
    <div class="submit-btn-container">
      <router-link :to="{ name: 'UserLogout' }"><button type="button" class="btn btn-danger">Déconnexion</button></router-link>
      
    </div>
  </div>
</template>

<script>
export default {
};
</script>

<style></style>
