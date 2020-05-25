<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>-->

    <navbar :session="session" />
      <hero />
    <router-view />

    <footpage />
  </div>
</template>

<script>
import navbar from "./components/layouts/navbar.vue";
import footpage from "./components/layouts/footer.vue";
import hero from "./components/hero/hero.vue";

export default {
  name: "app",
  components: {
    footpage,
    navbar,
    hero
  },
  data: function() {
    return {
      session: null
    };
  },
  created: function() {
    this.getSession();
  },
  methods: {
    getSession: async function() {
      const response = await axios
        .get("/api/user/login")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.session = response.data.session;

      console.log(this.session);
    }
  }
};
</script>
