<template>
  <section class="profile" v-bind:style="[resize  ? {height: screenHeight + 'px'} : {height: 'auto'}]">
    <div
      class="hero"
      v-bind:style="{
        'background-image':
          'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),' +
          'url(https://cdn.pixabay.com/photo/2016/04/19/17/07/eat-1339061_1280.jpg)',
      }"
    >
      <div class="hero-content">
        <h1 class>{{ user.lastName }} <span class="last-name">{{user.firstName}}</span> </h1>
        <p>{{ user.address }}</p>
        <p class="restaurant-address">{{ user.mail }}</p>
        <div class="restaurant-category">
          <p>Solde : {{ user.balance}}€ </p>
        </div>
      </div>
    </div>
    <h2 class="section-title">Commandes en cours</h2>
    <!-- <div style="height:1500px"></div> -->
    <h2 class="section-title">Historiques des commandes</h2>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      user: null,
      screenHeight: 0,
      resize : false,
    };
  },
  
  methods: {
    async getProfile() {
      const response = await axios
        .get("/api/user/profile")
        .then(function(response) {
          // console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.user = response.data.results;
    },
     handleResize() {
      this.windowHeight = window.innerHeight;
      this.pageHeight = document.querySelector(".header-main").clientHeight;;
      console.log("HEIGHT OF MY PAGE "+this.pageHeight);
      
      this.headerHeight = document.querySelector(".header-main").clientHeight;
      this.footerHeight = document.querySelector("footer").clientHeight;
      this.screenHeight =
        this.windowHeight - (this.headerHeight + this.footerHeight);
        console.log("WINDOW HEIGHT :"+this.windowHeight + "SCREEN HEIGHT :"+this.screenHeight)
        if(this.windowHeight > this.pageHeight ){
          this.resize = true
          console.log(this.resize);
          
        }else if(this.windowHeight < this.pageHeight){
          this.resize = false
          console.log(this.resize);
        }
        console.log(this.resize);
    }
  },
  mounted: function() {
    this.getProfile();
    this.handleResize();
  },
};
</script>
