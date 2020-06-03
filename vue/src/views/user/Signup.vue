<template>
  <div class="signup-wrapper" v-bind:style="{ height: screenHeight + 'px' }">
    <div class="signup-title">
      <h2>Créer un compte</h2>
    </div>

    <div v-if="info != null">
      <div class="message-container" v-if="info.success">
        <div class="success">{{ info.message }}</div>
      </div>
      <div class="message-container" v-else>
        <div class="error">{{ info.message }}</div>
      </div>
    </div>
    <div class="form-container">
      <form @submit.prevent="signup" action method="POST">
        <div class="grid50-50">
          <div class="form__group field">
            <input
              v-model="form.firstName"
              type="text"
              name="firstName"
              class="form__field"
              placeholder="Prénom"
              required
            />
            <label for="firstName" class="form__label">Prénom</label>
          </div>

          <div class="form__group field">
            <input
              v-model="form.lastName"
              type="text"
              name="lastName"
              class="form__field"
              placeholder="Nom"
              required
            />
            <label for="lastName" class="form__label">Nom</label>
          </div>
        </div>

        <div class="form__group field">
          <input
            v-model="form.address"
            type="text"
            name="address"
            class="form__field"
            placeholder="Adresse"
            required
          />
          <label for="address" class="form__label">Adresse</label>
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

        <!-- <input v-model="form.firstName" type="text" name="firstName" required />
        <label for="firstName">Prénom</label>-->

        <!-- <input v-model="form.lastName" type="text" name="lastName" required />
        <label for="lastName">Nom</label>-->

        <!-- <input v-model="form.address" type="text" name="address" required />
        <label for="address">address</label>-->

        <!-- <input v-model="form.mail" type="email" name="mail" required />
        <label for="mail">mail</label>-->

        <!-- <input v-model="form.password" type="password" name="password" required />
        <label for="password">Mot de passe</label>-->

        <!-- <input v-model="form.repassword" type="password" name="repassword" required />
        <label for="repassword">repassword</label>-->
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
  name: "UserSignup",
  data: function() {
    return {
      form: {
        firstName: null,
        lastName: null,
        address: null,
        mail: null,
        password: null,
        repassword: null
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
    signup: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("firstName", this.form.firstName);
      bodyFormData.set("lastName", this.form.lastName);
      bodyFormData.set("address", this.form.address);
      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("password", this.form.password);
      bodyFormData.set("repassword", this.form.repassword);

      const response = await axios
        .post("/api/user/signup", bodyFormData, {
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
