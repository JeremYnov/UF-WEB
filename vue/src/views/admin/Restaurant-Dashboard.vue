<template>
  <div class="sidebar-wrapper" v-if="restaurant != null">
    <div
      class="overlay"
      v-bind:class="{ 'is-open': closeThePopup }"
      v-on:click="closePopup()"
    ></div>
    <Sidebar />
    <div class="main_content">
      <RestaurantHero :restaurantInfos="restaurant" />

      <div class="submit-btn-container">
        <button
          class="submit-btn"
          v-on:click="toggleAdminAddPlate(), scrollToTop()"
        >
          Ajouter un plat
        </button>
        <button
          class="submit-btn"
          v-on:click="toggleAdminEditInformations(), scrollToTop()"
        >
          Modifier les informations
        </button>
      </div>
      <div class="submit-btn-container">
        <button class="submit-btn" v-on:click="chosenTable = 1">
          Liste des plats
        </button>
        <button class="submit-btn" v-on:click="chosenTable = 2">
          Commandes en cours
        </button>
        <button class="submit-btn" v-on:click="chosenTable = 3">
          Historique des commandes
        </button>
      </div>
      <PlatesTable
        :plates="restaurant.plates"
        v-if="chosenTable == 1"
        v-on:openPopup="editPlatePopupActive = $event"
        v-on:openOverlay="closeThePopup = $event"
        v-on:plateId="plateId = $event"
      />

      <CurrentOrdersTable :restaurant="restaurant" v-if="chosenTable == 2" />

      <HistoryOrdersTable :restaurant="restaurant" v-if="chosenTable == 3" />
    </div>

    <AdminAddPlatePopup
      :popupActive="addPlatePopupActive"
      v-on:closeOverlay="closeThePopup = $event"
      v-on:closePopup="addPlatePopupActive = $event"
    />

    <AdminEditRestaurantPopup
      :restaurant="restaurant"
      :popupActive="editInformationsPopupActive"
      v-on:closeOverlay="closeThePopup = $event"
      v-on:closePopup="editInformationsPopupActive = $event"
    />

    <AdminEditPlatePopup
      :popupActive="editPlatePopupActive"
      :plateId="plateId"
      v-on:closeOverlay="closeThePopup = $event"
      v-on:closePopup="editInformationsPopupActive = $event"
    />
  </div>
</template>

<script>
import axios from "axios";
import RestaurantHero from "@/components/hero/restaurant-hero.vue";
import Sidebar from "@/components/layouts/sidebar.vue";
import AdminEditRestaurantPopup from "@/components/admin/restaurant/edit-restaurant-popup.vue";
import AdminAddPlatePopup from "@/components/admin/restaurant/add-plate-popup.vue";
import PlatesTable from "@/components/admin/restaurant/plates-table.vue";
import CurrentOrdersTable from "@/components/admin/restaurant/current-orders-table.vue";
import HistoryOrdersTable from "@/components/admin/restaurant/history-orders-table.vue";
import AdminEditPlatePopup from "@/components/admin/restaurant/edit-plate-popup.vue";
export default {
  components: {
    RestaurantHero,
    Sidebar,
    AdminEditRestaurantPopup,
    AdminAddPlatePopup,
    CurrentOrdersTable,
    HistoryOrdersTable,
    PlatesTable,
    AdminEditPlatePopup,
  },
  data: function() {
    return {
      restaurant: null,
      editInformationsPopupActive: false,
      editPlatePopupActive: false,
      addPlatePopupActive: false,
      closeThePopup: false,
      chosenTable: 1,
      plateId: 0,
    };
  },

  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    toggleAdminAddPlate() {
      this.addPlatePopupActive = !this.addPlatePopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    toggleAdminEditInformations() {
      this.editInformationsPopupActive = !this.editInformationsPopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    closePopup() {
      this.closeThePopup = !this.closeThePopup;
      if (this.editInformationsPopupActive == true) {
        this.editInformationsPopupActive = !this.editInformationsPopupActive;
      } else if (this.addPlatePopupActive == true) {
        this.addPlatePopupActive = !this.addPlatePopupActive;
      }else if (this.editPlatePopupActive == true) {
        this.editPlatePopupActive = !this.editPlatePopupActive;
      }
    },
    async getRestaurantDashboard() {
      const response = await axios
        .get("/api/admin/restaurant/" + this.$route.params.id + "/dashboard")
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.restaurant = response.data.results;
    },
  },

  mounted: function() {
    this.getRestaurantDashboard();
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
