<template>
  <section
    class="profile"
    v-bind:style="[
      resize ? { height: screenHeight + 'px' } : { height: 'auto' },
    ]"
  >
    <!-- <div
      class="hero"
      v-bind:style="{
        'background-image':
          'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),' +
          'url(https://cdn.pixabay.com/photo/2016/04/19/17/07/eat-1339061_1280.jpg)',
      }"
    >
      <div class="hero-content">
        <h1 class>
          {{ user.lastName }}
          <span class="last-name">{{ user.firstName }}</span>
        </h1>
        <p>{{ user.address }}</p>
        <p class="restaurant-address">{{ user.mail }}</p>
        <div class="restaurant-category">
          <p>Solde : {{ user.balance }}€</p>
        </div>
      </div>
    </div> -->

    <ProfileHero :user="this.user" />
    <div class="submit-btn-container">
      <button class="submit-btn" v-on:click="toggleEditProfile()">
        Modifier les informations
      </button>
    </div>
    <div
      class="overlay"
      v-bind:class="{ 'is-open': closeThePopup }"
      v-on:click="closePopup()"
    ></div>
    <h2 class="section-title">Commandes en cours</h2>
    <!-- <div style="height:1500px"></div> -->
    <h2 class="section-title">Historiques des commandes</h2>

    <div
      class="edit-profile-popup"
      v-if="editProfilePopupActive"
      v-bind:class="{ 'is-active': editProfilePopupActive }"
    >
      <div class="edit-profile-title">
        <h2>Modifier le profil</h2>
      </div>
      <form @submit.prevent="updateProfile" method="POST">
        <div class="grid50-50">
          <div class="form__group field">
            <input
              v-model="form.firstName"
              type="text"
              name="firstName"
              class="form__field"
              placeholder="Prénom"
            />
            <label for="firstName" class="form__label">{{
              user.firstName
            }}</label>
          </div>

          <div class="form__group field">
            <input
              v-model="form.lastName"
              type="text"
              name="lastName"
              class="form__field"
              placeholder="Nom"
            />
            <label for="lastName" class="form__label">{{
              user.lastName
            }}</label>
          </div>
        </div>

        <div class="form__group field">
          <input
            v-model="form.address"
            type="text"
            name="address"
            class="form__field"
            placeholder="Adresse"
          />
          <label for="address" class="form__label">{{ user.address }}</label>
        </div>

        <!-- <div class="form__group field">
          <input
            v-model="form.mail"
            type="email"
            name="mail"
            class="form__field"
            placeholder="Adresse mail"
          />
          <label for="mail" class="form__label">{{user.mail}}</label>
        </div> -->

        <!-- <div class="grid50-50">
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
        </div> -->
        <div class="submit-btn-container">
          <button class="submit-btn" type="submit">
            Valider
          </button>
        </div>
      </form>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import ProfileHero from "@/components/hero/profile-hero.vue";
  

export default {
  name: "UserProfile",
  components: {
    ProfileHero,
  },
  data: function() {
    return {
      user: null,
      screenHeight: 0,
      resize: false,
      editProfilePopupActive: false,
      closeThePopup: false,
      form: {
        firstName: "",
        lastName: "",
        address: "",
      },
    };
  },
  methods: {
    toggleEditProfile() {
      this.editProfilePopupActive = !this.editProfilePopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    closePopup() {
      this.closeThePopup = !this.closeThePopup;
      if (this.editProfilePopupActive == true) {
        this.editProfilePopupActive = !this.editProfilePopupActive;
      }
    },
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
    updateProfile: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("firstName", this.form.firstName);
      bodyFormData.set("lastName", this.form.lastName);
      bodyFormData.set("address", this.form.address);

      const response = await axios
        .post("/api/user/profile/update", bodyFormData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;

      // localStorage.setItem("session", response.data.session);
      // router.push("/");
      location.reload();
    },
    handleResize() {
      this.windowHeight = window.innerHeight;
      this.pageHeight = document.querySelector("#app").clientHeight;
      console.log("HEIGHT OF MY PAGE " + this.pageHeight);

      this.headerHeight = document.querySelector(".header-main").clientHeight;
      this.footerHeight = document.querySelector("footer").clientHeight;
      this.screenHeight =
        this.windowHeight - (this.headerHeight + this.footerHeight);
      console.log(
        "WINDOW HEIGHT :" +
          this.windowHeight +
          "SCREEN HEIGHT :" +
          this.screenHeight
      );
      if (this.windowHeight > this.pageHeight) {
        this.resize = true;
        console.log(this.resize);
      } else if (this.windowHeight < this.pageHeight) {
        this.resize = false;
        console.log(this.resize);
      }
      console.log(this.resize);
    },
  },
  mounted: function() {
    this.getProfile();
    this.handleResize();
  },
};
</script>
