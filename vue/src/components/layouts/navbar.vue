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
        <ul v-if="session" class="nav-list">
          <li class="nav-item">
            <router-link :to="{ name: 'UserLogout'}">Deconnexion</router-link>
          </li>
        </ul>
        <ul v-else class="nav-list">
          <li class="nav-item left-item">
            <a href="#">Inscription</a>
            <ul class="sub-menu">
              <li class="nav-item">
                <router-link :to="{ name: 'UserSignup'}">Client</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'RestaurantSignup'}">Restaurant</router-link>
              </li>
            </ul>
          </li>

          <li class="nav-item">
            <a href="#">Connexion</a>
            <ul class="sub-menu">
              <li class="nav-item">
                <router-link :to="{ name: 'UserLogin'}">Client</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'UserLogin'}">Restaurant</router-link>
              </li>
            </ul>
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
export default {
  // props: ["session"],
  data: () => {
    return {
      session: JSON.parse(localStorage.getItem("session")),
      isBurgerActive: false
    };
  },
  methods: {
    toggle() {
      this.isBurgerActive = !this.isBurgerActive;
    }
  }
};
</script>

<style lang="scss">
@import "../../assets/scss/main.scss";
</style>