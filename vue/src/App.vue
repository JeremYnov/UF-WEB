<template>
  <div id="app" >

    <navbar />

    <router-view v-bind:style="{ 'padding-top': headerHeight + 'px' }" />

    <footpage />
  </div>
</template>

<script>
import navbar from "./components/layouts/navbar.vue";
import footpage from "./components/layouts/footer.vue";

export default {
  name: "app",
  components: {
    footpage,
    navbar,
  },

  data: function() {
    return {
      headerHeight : 0,
    };
  },
  // created() {
  //   window.addEventListener("resize", this.handleResize);
    
  // },
  // destroyed() {
  //   window.removeEventListener("resize", this.handleResize);
  // },
  mounted(){
    this.handleResize();
  },
  methods: {
    handleResize() {
      // this.windowHeight = window.innerHeight;
      this.headerHeight = document.querySelector(".header-main").clientHeight;
      // this.footerHeight = document.querySelector("footer").clientHeight;
      // this.screenHeight =
      //   this.windowHeight - (this.headerHeight + this.footerHeight);
    }
  },

};
</script>

  