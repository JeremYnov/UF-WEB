<template>
  <div class="sidebar-wrapper">
    <Sidebar />
    <div class="main_content">
      <DashboardCards />
    </div>
  </div>
</template>

<script>
import DashboardCards from "@/components/admin/cards.vue";
import Sidebar from "@/components/layouts/sidebar.vue";

export default {
  components: {
    DashboardCards,
    Sidebar,
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
