<template>
  <div>
    <div class="nav-responsive" v-bind:class="{ 'nav-transition' : isBurgerActive}">
      <ul class="nav-list">
        <li class="nav-item">
          <a href="#">Home</a>
        </li>

        <li class="nav-item">
          <a href="#">About</a>
        </li>

        <li class="nav-item">
          <a href="#">Blog</a>
        </li>
        <li class="nav-item">
          <a href="#">Inscription</a>
        </li>
        <li class="nav-item">
          <a href="#">Connexion</a>
        </li>
      </ul>
    </div>

    <div class="overlay" v-bind:class="{ 'is-open' : isBurgerActive }" v-on:click="toggle()"></div>

    <header class="header-main">
      <div class="header-logo">
        <a href="/">
          <h1>EatYng</h1>
        </a>
      </div>

      <nav class="header-nav">
        <ul class="nav-list">
          <li class="nav-item">
            <a href="/">Restaurant</a>
          </li>

          <li class="nav-item middle-item">
            <a href="/about">About</a>
          </li>

          <li class="nav-item">
            <a href="#">Blog</a>
          </li>
        </ul>
      </nav>
      <nav class="header-nav">
        <ul v-if="session == false" class="nav-list">
          <li class="nav-item left-item">
            <a href="#">Inscription</a>
            <ul class="sub-menu">
              <li class="nav-item">
                <a href="user/signup">Client</a>
              </li>
              <li class="nav-item">
                <a href="/restaurant/signup">Restaurant</a>
              </li>
            </ul>
          </li>

          <li class="nav-item">
            <a href="#">Connexion</a>
          </li>
        </ul>
        <ul v-else class="nav-list">
          <li class="nav-item">
            <a @click="logout">Deconnexion</a>
          </li>
        </ul>
      </nav>

      <div class="header-nav-wrapper" v-on:click="toggle()">
        <div class="header-nav-burger" v-bind:class="{ 'is-animate' : isBurgerActive }"></div>
      </div>
    </header>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  props: ["session"],
  data: () => ({
    isBurgerActive: false
  }),
  methods: {
    toggle() {
      this.isBurgerActive = !this.isBurgerActive;
    },
    logout: () => {
      axios
        .get("/api/user/logout")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.$route.router.push("Home");
    }
  }
};
</script>

<style lang="scss">
@import "../../assets/scss/main.scss";
</style>