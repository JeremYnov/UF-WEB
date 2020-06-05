<template>
  <div class="sidebar-wrapper" v-if="user != null">
    <div
      class="overlay"
      v-bind:class="{ 'is-open': closeThePopup }"
      v-on:click="closePopup()"
    ></div>
    <Sidebar />
    <div class="main_content">
      <ProfileHero :user="this.user" />

      <div class="submit-btn-container">
        <button class="submit-btn" v-on:click="toggleAdminEditInformations(), scrollToTop()">
          Modifier les informations
        </button>
      </div>

      <CurrentOrdersTable :user="user" />

      <HistoryOrdersTable :user="user" />
    </div>

    <AdminEditUserPopup
      :user="user"
      :popupActive="editInformationsPopupActive"
      v-on:closeOverlay="closeThePopup = $event"
      v-on:closePopup="editInformationsPopupActive = $event"
    />
  </div>
</template>

<script>
import axios from "axios";
import ProfileHero from "@/components/hero/profile-hero.vue";
import Sidebar from "@/components/layouts/sidebar.vue";
import CurrentOrdersTable from "@/components/admin/user/current-orders-table.vue";
import HistoryOrdersTable from "@/components/admin/user/history-orders-table.vue";
import AdminEditUserPopup from "@/components/admin/user/edit-user-popup.vue";

export default {
  components: {
    ProfileHero,
    Sidebar,
    CurrentOrdersTable,
    HistoryOrdersTable,
    AdminEditUserPopup
  },
  data: function() {
    return {
      user: null,
      editInformationsPopupActive: false,
      closeThePopup: false,
    };
  },
  filters: {
    truncate: function(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    },
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
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
      }
    },
    async getMemberProfile() {
      const response = await axios
        .get("/api/admin/member/" + this.$route.params.id + "/profile")
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.user = response.data.results;
      console.log(this.user);
    },
    
  },
  mounted: function() {
    this.getMemberProfile();
  },
};
</script>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
</style>
