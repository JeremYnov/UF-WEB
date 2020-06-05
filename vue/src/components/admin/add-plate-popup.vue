<template>
  <div class="add-plate-popup" v-if="popupActive" v-bind:class="{ 'is-active': popupActive }">
    <div class="add-plate-title">
      <h2>Ajouter un plat</h2>
    </div>

    <form @submit.prevent="setNewPlate" action method="POST">
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
          <select v-model="form.type" name="type" class="form-select" required>
            <option disabled>Choisissez</option>
            <option>Menu</option>
            <option>Plat</option>
            <option>Boisson</option>
            <option>Déssert</option>
          </select>
          <label for="type" class="form__label">Type de plat</label>
        </div>
      </div>

      <div class="form__group field">
        <textarea
          v-model="form.description"
          type="text"
          name="description"
          class="form__field"
          placeholder="Description"
        />
        <label for="description" class="form__label">Description</label>
      </div>

      <div class="grid50-50">
        <div class="form__group field">
          <input @change="previewFiles" type="file" id="file" required />
          <label for="file">Choisir un fichier...</label>
        </div>
        <div class="form__group field">
          <input
            v-model="form.unitPrice"
            type="text"
            name="unitPrice"
            class="form__field"
            placeholder="Prix Unitaire"
            required
          />
          <label for="name" class="form__label">Prix Unitaire</label>
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
    popupActive: null
  },
  data: function() {
    return {
      form: {
        name: "",
        type: "",
        description: "",
        unitPrice: "",
        image: ""
      }
    };
  },
  methods: {
    previewFiles: function(event) {
      this.form.image = event.target.files[0];
    },
    setNewPlate: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("name", this.form.name);
      bodyFormData.set("type", this.form.type);
      bodyFormData.set("content", this.form.description);
      bodyFormData.set("picture", this.form.image);
      bodyFormData.set("price", this.form.unitPrice);

      const response = await axios
        .post("/api/restaurant/add/new/plate", bodyFormData, {
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
      this.$emit("closeOverlay", false);
      this.$emit("closePopup", false);
      location.reload();
    }
  }
};
</script>