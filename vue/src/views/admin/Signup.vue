<template>
  <!-- <div>
    <div v-if="info != null">
      <div v-if="info.success">
        <p>Success {{ info.message }}</p>
      </div>
      <div v-else>
        <p>Error {{ info.message }}</p>
      </div>
    </div>

    <form @submit.prevent="signup" method="POST">
      <input v-model="form.userName" type="text" name="userName" required />
      <label for="userName">userName</label>

      <input v-model="form.mail" type="email" name="mail" required />
      <label for="mail">mail</label>

      <input v-model="form.password" type="password" name="password" required />
      <label for="password">password</label>

      <input v-model="form.repassword" type="password" name="repassword" required />
      <label for="repassword">repassword</label>

      <button type="submit">Envoyer</button>
    </form>
  </div>-->
  <div class="signup-wrapper" v-bind:style="{ height: screenHeight + 'px' }">
    <div class="signup-title">
      <h2>Créer un compte</h2>
      <p>Réservé aux administrateurs !</p>
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
      <form @submit.prevent="signup" action method="POST">
          <div class="form__group field">
            <input
              v-model="form.userName" type="text" name="userName"
              class="form__field"
              placeholder="Nom d'utilisateur"
              required
            />
            <label for="firstName" class="form__label">Nom d'utilisateur</label>
          </div>

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

        

        <div class="grid50-50">

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

          <div class="form__group field">
            <input
              v-model="form.repassword"
              type="password"
              name="repassword"
              class="form__field"
              placeholder="Confirmation"
              required
            />
            <label for="repassword" class="form__label">Confirmation</label>
          </div>

        </div>

        <div class="submit-btn-container">
          <button type="submit" class="submit-btn">Créer mon compte</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "AdminSignup",
  data: function() {
    return {
      form: {
        userName: null,
        mail: null,
        password: null,
        repassword: null
      },
      info: null,
      screenHeight: 0,
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
    signup: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("userName", this.form.userName);
      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("password", this.form.password);
      bodyFormData.set("repassword", this.form.repassword);

      const response = await axios
        .post("/api/admin/signup", bodyFormData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
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

<style lang="scss">
</style>