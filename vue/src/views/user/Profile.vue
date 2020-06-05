<template>
  <section class="profile" v-if="user != null">
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
    <div class="container">
      <h2 class="section-title">Commandes en cours</h2>
      <InProgressOrders />
      <!-- <div style="height:1500px"></div> -->
      <h2 class="section-title">Historiques des commandes</h2>
      <HistoricOrders />
    </div>
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
import HistoricOrders from "@/components/table/orders-placed-table.vue";
import InProgressOrders from "@/components/table/in-progress-table.vue";

export default {
  name: "UserProfile",
  components: {
    ProfileHero,
    HistoricOrders,
    InProgressOrders,
  },
  data: function() {
    return {
      user: null,
      // screenHeight: 0,
      // resize: false,
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
  },
  mounted: function() {
    this.getProfile();
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
