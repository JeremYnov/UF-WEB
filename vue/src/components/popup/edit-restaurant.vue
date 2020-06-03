<template>
  <div
    class="add-plate-popup"
    v-if="popupActive"
    v-bind:class="{ 'is-active': popupActive }"
  >
    <div class="add-plate-title">
      <h2>Modifier les informations</h2>
    </div>

    <form @submit.prevent="setNewPlate" action method="POST">
      <div class="form__group field">
        <input
          v-model="formModification.name"
          type="text"
          name="name"
          class="form__field"
          placeholder="Nom"
          required
        />
        <label for="name" class="form__label">Nom</label>
      </div>

      <div class="form__group field">
        <input
          v-model="formModification.address"
          type="text"
          name="address"
          class="form__field"
          placeholder="Adresse"
        />
        <label for="address" class="form__label">Adresse</label>
      </div>

      <div class="grid50-50">
        <div class="form__group field">
          <input @change="previewFiles" type="file" id="file" required />
          <label for="file">Choisir un fichier...</label>
        </div>
        <div class="form__group field">
          <select
            v-model="formModification.category"
            name="category"
            id="category"
            class="form-select"
            required
          >
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
        <button
          type="submit"
          class="submit-btn"
          v-on:click="
            $emit('closeOverlay', false) && $emit('closePopup', false)
          "
        >
          Valider
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    popupActive: null,
  },
  data: function() {
    return {
      formModification: {
        name: null,
        category: null,
        address: null,
        image: null,
      },
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
              "application/x-www-form-urlencoded; multipart/form-data",
          },
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
      location.reload();
    },
  },
};
</script>
