<template>
  <div class="sidebar-wrapper">
    <div class="sidebar">
      <h2>DashBoard</h2>
      <ul>
        <h3>Utilisateur</h3>
        <li>
          <a href="#"><i class="fas fa-home"></i>Membres</a>
        </li>
        <li>
          <a href="#"><i class="fas fa-user"></i>Restaurateurs</a>
        </li>
        <h3>Commande</h3>
        <li>
          <a href="#"><i class="fas fa-project-diagram"></i>En cours</a>
        </li>
        <li>
          <a href="#"><i class="fas fa-blog"></i>Historique</a>
        </li>
      </ul>
    </div>
    <div class="main_content">
      <DashboardCards />
      <UsersTable />
      <RestaurantsTable />
      <CurrentOrdersTable />
      <HistoryOrdersTable />
    </div>
  </div>
</template>

<script>
import UsersTable from "@/components/admin/users-table.vue";
import RestaurantsTable from "@/components/admin/restaurants-table.vue";
import CurrentOrdersTable from "@/components/admin/current-orders-table.vue";
import DashboardCards from "@/components/admin/cards.vue";
import HistoryOrdersTable from "@/components/admin/history-orders-table.vue";
 

export default {
  components: {
    DashboardCards,
    UsersTable,
    CurrentOrdersTable,
    RestaurantsTable,
    HistoryOrdersTable,
  },
};
</script>

<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
