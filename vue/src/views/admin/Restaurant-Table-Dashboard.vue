<template>
   <div class="sidebar-wrapper" v-bind:style="{ 'min-height': screenHeight + 'px' }" >
    <Sidebar />
    <div class="main_content">
      <DashboardCards />
      <RestaurantsTable />
    </div>
  </div>
</template>

<script>
import RestaurantsTable from "@/components/admin/restaurants-table.vue";
import Sidebar from "@/components/layouts/sidebar.vue";
import DashboardCards from "@/components/admin/cards.vue";
export default {
components: {
    DashboardCards,
    RestaurantsTable,
    Sidebar
  },
  data: function() {
    return {
      screenHeight: 0
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.windowHeight = window.innerHeight;
      this.footerHeight = document.querySelector("footer").clientHeight;
      this.screenHeight =
        this.windowHeight -  this.footerHeight;
    }
  }
}
</script>

<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>