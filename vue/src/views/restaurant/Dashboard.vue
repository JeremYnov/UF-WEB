<template>
  <section class="dashboard">
    <div
      class="overlay"
      v-bind:class="{ 'is-open': closeThePopup }"
      v-on:click="closePopup()"
    ></div>
    
    <div class="submit-btn-container">
      <button class="submit-btn" v-on:click="toggleAddPlate()">
        Ajouter un plat
      </button>
      <button class="submit-btn" v-on:click="toggleEditInformations()">
        Modifier les informations
      </button>
    </div>
    <div class="submit-btn-container">
      <button class="submit-btn" v-on:click="chosenTable = 1">
        Tableau 1
      </button>
      <button class="submit-btn" v-on:click="chosenTable = 2">
        Tableau 2
      </button>
      <button class="submit-btn" v-on:click="chosenTable = 3">
        Tableau 3
      </button>
    </div>
    <div class="container">
      <Plates v-if="chosenTable == 1" />
      <InProgressOrder v-if="chosenTable == 2" />
      <OrdersPlaces v-if="chosenTable == 3" />
    </div>

    <AddPlatePopup :popupActive="addPlatePopupActive" v-on:closeOverlay="closeThePopup = $event" v-on:closePopup="addPlatePopupActive = $event"  />
    <EditRestaurantPopup :popupActive="editInformationsPopupActive" v-on:closeOverlay="closeThePopup = $event" v-on:closePopup="editInformationsPopupActive = $event"  />


  </section>
</template>
<script>
import axios from "axios";
import Plates from "@/components/table/plates-table.vue";
import InProgressOrder from "@/components/table/in-progress-table.vue";
import OrdersPlaces from "@/components/table/orders-places-table.vue";
import EditRestaurantPopup from "@/components/popup/edit-restaurant.vue";
import AddPlatePopup from "@/components/popup/add-plate.vue";
export default {
  components: {
    Plates,
    InProgressOrder,
    OrdersPlaces,
    EditRestaurantPopup,
    AddPlatePopup,
  },
  data: function() {
    return {
      addPlatePopupActive: false,
      editInformationsPopupActive: false,
      closeThePopup: false,
      chosenTable: 1,
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
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
