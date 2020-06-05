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
