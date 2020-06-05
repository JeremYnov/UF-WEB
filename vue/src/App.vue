<template>
  <div id="app">
    <navbar />

    <router-view v-if="role != 'admin'" v-bind:style="{ 'padding-top': headerHeight + 'px' }" />

    <router-view v-if="role == 'admin'" />

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
      headerHeight: 0,
      role:null
    };
  },
  
  mounted() {
    this.handleResize();
    this.getSession()
  },
  methods: {
    handleResize() {
      this.headerHeight = document.querySelector(".header-main").clientHeight;
    },
    getSession() {
      this.session = JSON.parse(localStorage.getItem("session")).session;
      this.role = JSON.parse(localStorage.getItem("session")).user.role;
    }
  }
};


</script>

<style lang="scss">
@import "assets/scss/main.scss";
</style>

  