<template>
  <div class="add-plate-popup" v-if="popupActive" v-bind:class="{ 'is-active': popupActive }">
    <div class="add-plate-title">
      <h2>Modifier les informations</h2>
    </div>

    <div v-if="info != null">
      <div class="message-container" v-if="info.success">
        <div class="success">{{ info.message }}</div>
      </div>
      <div class="message-container" v-else>
        <div class="error">{{ info.message }}</div>
      </div>
    </div>

    <form @submit.prevent="setUpdateProfile" method="POST">
      <div class="grid50-50">
        <div class="form__group field">
          <input
            v-model="form.firstName"
            type="text"
            name="firstname"
            class="form__field"
            placeholder="Prénom"
          />
          <label for="firstname" class="form__label">Prénom</label>
        </div>

        <div class="form__group field">
          <input
            v-model="form.lastName"
            type="text"
            name="laststname"
            class="form__field"
            placeholder="Nom"
          />
          <label for="lastname" class="form__label">Nom</label>
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
        <label for="address" class="form__label">Adresse</label>
      </div>

      <div class="form__group field">
        <input v-model="form.sold" type="text" name="sold" class="form__field" placeholder="Solde" />
        <label for="sold" class="form__label">Solde</label>
      </div>

      <div class="submit-btn-container">
        <button type="submit" class="submit-btn">Valider</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    popupActive: null,
    restaurant: null
  },
  data: function() {
    return {
      form: {
        firstName: "",
        lastName: "",
        address: "",
        sold: ""
      },
      info: null
    };
  },
  methods: {
    previewFiles: function(event) {
      this.form.image = event.target.files[0];
    },
    setUpdateProfile: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("firstName", this.form.firstName);
      bodyFormData.set("lastName", this.form.lastName);
      bodyFormData.set("address", this.form.address);
      bodyFormData.set("sold", this.form.sold);

      const response = await axios
        .post(
          "/api/admin/member/" + this.$route.params.id + "/update/profile",
          bodyFormData,
          {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          }
        )
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;

      if (response.data.success) {
        await setTimeout(() => {
          this.$emit("closeOverlay", false);
          this.$emit("closePopup", false);

          location.reload();
        }, 2000);
      }
    }
  }
};
</script>
