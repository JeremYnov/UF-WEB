<template>
  <div class="sidebar-wrapper">
    <Sidebar />
    <div class="main_content">
      <DashboardCards />
      <CurrentOrdersTable />
    </div>
  </div>
</template>

<script>
import CurrentOrdersTable from "@/components/admin/current-orders-table.vue";
import Sidebar from "@/components/layouts/sidebar.vue";
import DashboardCards from "@/components/admin/cards.vue";
export default {
  components: {
    DashboardCards,
    CurrentOrdersTable,
    Sidebar,
  },
};
</script>

<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>