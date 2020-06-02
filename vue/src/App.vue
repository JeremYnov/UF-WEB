<template>
  <div id="app">
    <navbar />

    <router-view v-bind:style="{ 'padding-top': headerHeight + 'px' }" />

    <footpage />
    <script type="application/javascript" src="https://kit.fontawesome.com/c3feb606cd.js" crossorigin="anonymous"></script>
  </div>
</template>

<script>
import navbar from "./components/layouts/navbar.vue";
import footpage from "./components/layouts/footer.vue";

export default {
  name: "app",
  components: {
    footpage,
    navbar
  },

  data: function() {
    return {
      headerHeight: 0
    };
  },
  mounted() {
    this.handleResize();
  },
  methods: {
    handleResize() {
      this.headerHeight = document.querySelector(".header-main").clientHeight;
    }
  }
};

</script>

<style lang="scss">
@import "assets/scss/main.scss";
</style>

  