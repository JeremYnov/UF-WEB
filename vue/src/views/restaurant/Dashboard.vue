<template>
  <section class="dashboard">
    <div class="submit-btn-container">
      <button class="submit-btn" v-on:click="toggleAddPlate()">
        Ajouter un plat
      </button>
      <button class="submit-btn" v-on:click="toggleEditInformations()">
        Modifier les informations
      </button>
    </div>
    <div class="submit-btn-container">
      <button class="submit-btn" v-on:click="chosenTable=1">
        Tableau 1
      </button>
      <button class="submit-btn" v-on:click="chosenTable=2">
        Tableau 2
      </button>
      <button class="submit-btn" v-on:click="chosenTable=3">
        Tableau 3
      </button>
    </div>
    <div
      class="overlay"
      v-bind:class="{ 'is-open': closeThePopup }"
      v-on:click="closePopup()"
    ></div>
    <div class="container">
      <Plates v-if="chosenTable == 1"/>
      <InProgressOrder v-if="chosenTable == 2"/>
      <OrdersPlaces v-if="chosenTable == 3"/>
    </div>
    <div
      class="add-plate-popup"
      v-if="addPlatePopupActive"
      v-bind:class="{ 'is-active': addPlatePopupActive }"
    >
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
            <select v-model="form.type" name="type" required>
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
          <button type="submit" class="submit-btn" v-on:click="closePopup()">
            Valider
          </button>
        </div>
      </form>
    </div>

    <div
      class="add-plate-popup"
      v-if="editInformationsPopupActive"
      v-bind:class="{ 'is-active': editInformationsPopupActive }"
    >
      <div class="add-plate-title">
        <h2>Modifier les informations du restaurant</h2>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";
import Plates from "@/components/table/plates-table.vue";
import InProgressOrder from "@/components/table/in-progress-table.vue";
import OrdersPlaces from "@/components/table/orders-places-table.vue";
export default {
  components: {
    Plates,
    InProgressOrder,
    OrdersPlaces,
  },
  data: function() {
    return {
      addPlatePopupActive: false,
      editInformationsPopupActive: false,
      closeThePopup: false,
      chosenTable : 1,
      form: {
        name: null,
        type: null,
        description: null,
        unitPrice: null,
        image: null,
      },
    };
  },
  methods: {
    toggleAddPlate() {
      this.addPlatePopupActive = !this.addPlatePopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    toggleEditInformations() {
      this.editInformationsPopupActive = !this.editInformationsPopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    closePopup() {
      this.closeThePopup = !this.closeThePopup;
      if (this.addPlatePopupActive == true) {
        this.addPlatePopupActive = !this.addPlatePopupActive;
      } else if (this.editInformationsPopupActive == true) {
        this.editInformationsPopupActive = !this.editInformationsPopupActive;
      }
    },
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
      location.reload();
    },
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
