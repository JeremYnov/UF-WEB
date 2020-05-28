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
      <input v-model="form.name" type="text" name="name" required />
      <label for="name">name</label>

      <input @change="previewFiles" type="file" name="logo" required />
      <label for="logo">logo</label>

      <input v-model="form.address" type="text" name="address" required />
      <label for="address">address</label>

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
        <div class="grid50-50">
          <div class="form__group field">
            <input
              v-model="form.name"
              type="text"
              name="name"
              class="form__field"
              placeholder="Nom"
              required
            />
            <label for="name" class="form__label">Nom</label>
          </div>

          <div class="form__group field">
            <input @change="previewFiles" type="file" id="file" required />
            <label for="file">Choisir un fichier...</label>
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
        <div class="grid50-50">
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
            <select v-model="form.category" name="category" id="category" required>
              <option disabled>Choisissez</option>
              <option>Fast food</option>
              <option>Burger</option>
              <option>Pizza</option>
              <option>Sushi</option>
              <option>Asiatique</option>
              <option>Japonais</option>
            </select>

            <label for="category" class="form__label">Categorie</label>
          </div>
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
  name: "RestaurantSignup",
  data: function() {
    return {
      form: {
        name: null,
        logo: null,
        address: null,
        mail: null,
        category: null,
        password: null,
        repassword: null
      },
      info: null,
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

      bodyFormData.set("name", this.form.name);
      bodyFormData.set("logo", this.form.logo);
      bodyFormData.set("address", this.form.address);
      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("category", this.form.category);
      bodyFormData.set("password", this.form.password);
      bodyFormData.set("repassword", this.form.repassword);

      const response = await axios
        .post("/api/restaurant/signup", bodyFormData, {
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded; multipart/form-data"
          }
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
    },
    previewFiles: function(event) {
      console.log(event.target.files[0]);
      this.form.logo = event.target.files[0];
      console.log(this.form.logo);
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
