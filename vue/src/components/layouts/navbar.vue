<template>
  <div>
    <div class="nav-responsive" v-bind:class="{ 'nav-transition': isBurgerActive }">
      <ul class="header-nav-list">
        <li class="header-nav-item">
          <a href="#">Home</a>
        </li>

        <li class="header-nav-item">
          <a href="#">About</a>
        </li>

        <li class="header-nav-item">
          <a href="#">Blog</a>
        </li>
        <li class="header-nav-item">
          <a href="#">Inscription</a>
        </li>
        <li class="header-nav-item">
          <a href="#">Connexion</a>
        </li>
      </ul>
    </div>

    <div class="overlay" v-bind:class="{ 'is-open': isBurgerActive }" v-on:click="toggle()"></div>

    <header>
      <div class="header-main">
        <div class="header-logo">
          <a href="/">
            <h1>EatYng</h1>
          </a>
        </div>

        <nav class="header-nav">
          <ul class="header-nav-list">
            <li class="header-nav-item">
              <router-link :to="{ name: 'Restaurants' }">Restaurants</router-link>
            </li>
            <!-- <li class="header-nav-item middle-item">
              <a href="/about">About</a>
            </li>

            <li class="header-nav-item">
              <a href="#">Blog</a>
            </li>-->
          </ul>
        </nav>
        <nav class="header-nav">
          <ul v-if="session" class="header-nav-list">
            <li class="header-nav-item shopping-cart-item">
              <router-link :to="{ name: 'ShoppingCart' }">
                <img src="../../assets/icons/icons8-panier-80.png" alt />
              </router-link>
            </li>
            <li class="header-nav-item profile-item">
              <img src="../../assets/icons/icons8-compte-test-80.png" alt />
              <ul class="sub-menu">
                <li v-if="role == 'restaurant'" class="header-nav-item">
                  <router-link :to="{ name: 'RestaurantDashboard' }">Dashboard</router-link>
                </li>
                <li v-else class="header-nav-item">
                  <router-link :to="{ name: 'UserProfile' }">Profil</router-link>
                </li>
                <li class="header-nav-item">
                  <router-link :to="{ name: 'UserLogout' }">Déconnexion</router-link>
                </li>
              </ul>
            </li>
          </ul>
          <ul v-else class="header-nav-list">
            <li class="header-nav-item left-item">
              <a href="#">Inscription</a>
              <ul class="sub-menu">
                <li class="header-nav-item">
                  <router-link :to="{ name: 'UserSignup' }">Client</router-link>
                </li>
                <li class="header-nav-item">
                  <router-link :to="{ name: 'RestaurantSignup' }">Restaurant</router-link>
                </li>
              </ul>
            </li>

            <li class="header-nav-item">
              <a href="#">Connexion</a>
              <ul class="sub-menu">
                <li class="header-nav-item">
                  <router-link :to="{ name: 'UserLogin' }">Client</router-link>
                </li>
                <li class="header-nav-item">
                  <router-link :to="{ name: 'RestaurantLogin' }">Restaurant</router-link>
                </li>
              </ul>
            </li>
          </ul>
        </nav>

        <div class="header-nav-wrapper" v-on:click="toggle()">
          <div class="header-nav-burger" v-bind:class="{ 'is-animate': isBurgerActive }"></div>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  // props: ["session"],
  data: () => {
    return {
      session: "",
      role: "",
      isBurgerActive: false
    };
  },
  mounted: function() {
    this.getSession();
  },
  methods: {
    toggle() {
      this.isBurgerActive = !this.isBurgerActive;
    },
    getSession() {
      this.session = JSON.parse(localStorage.getItem("session")).session;
      this.role = JSON.parse(localStorage.getItem("session")).user.role;
    }
  }
};
</script>
