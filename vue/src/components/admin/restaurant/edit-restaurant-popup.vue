<template>
  <div class="add-plate-popup" v-if="popupActive" v-bind:class="{ 'is-active': popupActive }">
    <div class="add-plate-title">
      <h2>Modifier les informations</h2>
    </div>

    <form @submit.prevent="setUpdateProfile" method="POST">
      <div class="form__group field">
        <input v-model="form.name" type="text" name="name" class="form__field" placeholder="Nom" />
        <label for="name" class="form__label">Nom</label>
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

      <div class="grid50-50">
        <div class="form__group field">
          <input @change="previewFiles" type="file" id="file" />
          <label for="file">Choisir un fichier...</label>
        </div>
        <div class="form__group field">
          <select v-model="form.category" name="category" id="category" class="form-select">
            <option selected disabled>Choisissez</option>
            <option>Fast food</option>
            <option>Burger</option>
            <option>Pizza</option>
            <option>Sushi</option>
            <option>Asiatique</option>
            <option>Japonais</option>
          </select>
          <label for="category" class="form__label">Catégorie</label>
        </div>
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
        // name: this.restaurant.name,
        // category: this.restaurant.category,
        // address: this.restaurant.address,
        // image: "",
        name: "",
        category: "",
        address: "",
        image: ""
      }
    };
  },
  methods: {
    previewFiles: function(event) {
      this.form.image = event.target.files[0];
    },
    setUpdateProfile: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("name", this.form.name);
      bodyFormData.set("category", this.form.category);
      bodyFormData.set("address", this.form.address);
      bodyFormData.set("logo", this.form.image);

      const response = await axios
        .post(
          "/api/admin/restaurant/" + this.$route.params.id + "/update/profile",
          bodyFormData,
          {
            headers: {
              "Content-Type":
                "application/x-www-form-urlencoded; multipart/form-data"
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

      console.log(response.data);

      if (response.data.success) {
        location.reload();
      }

      this.$emit("closeOverlay", false);
      this.$emit("closePopup", false);
    }
  }
};
</script>
