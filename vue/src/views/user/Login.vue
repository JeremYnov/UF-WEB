<template>
  <div class="login-wrapper" v-bind:style="{ height: screenHeight + 'px' }">
    <div class="login-title">
      <h2>Connexion</h2>
    </div>

    <div v-if="info != null">
      <div v-if="info.success">
        <p>Success {{ info.message }}</p>
      </div>
      <div v-else>
        <p>Error {{ info.message }}</p>
      </div>
    </div>

    <div class="form-container">
      <form @submit.prevent="login" method="POST">
        <div class="form__group field">
          <input
            v-model="form.mail"
            type="email"
            name="mail"
            class="form__field"
            placeholder="Adresse mail"
            required
          />
          <label for="mail" class="form__label">Adresse mail</label>
        </div>

        <div class="form__group field">
          <input
            v-model="form.password"
            type="password"
            name="password"
            class="form__field"
            placeholder="Mot de passe"
            required
          />
          <label for="password" class="form__label">Mot de passe</label>
        </div>

        <div class="submit-btn-container">
          <button type="submit" class="submit-btn">Connexion</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "UserLogin",
  data: function() {
    return {
      form: {
        mail: null,
        password: null
      },
      info: null,
      // windowHeight:0,
      // headerHeight : 0,
      // footerHeight: 0,
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
    login: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("password", this.form.password);

      const response = await axios
        .post("/api/user/login", bodyFormData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;

      console.log(response.data);

      localStorage.setItem("session", response.data.session);

      location.reload();
    },
    handleResize() {
      this.windowHeight = window.innerHeight;
      this.headerHeight = document.querySelector(".header-main").clientHeight;
      this.footerHeight = document.querySelector("footer").clientHeight;
      this.screenHeight =
        this.windowHeight - (this.headerHeight + this.footerHeight);
    }
  }
};
</script>