<template>
  <div class="restaurant">
    <!-- <div class="hero" v-bind:style="{ 'background-image': 'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),' + 'url(' + restaurant.logo.url + ')' }">
      <div class="hero-content">
        <h1 class>{{ restaurant.name }}</h1>
        <p class="restaurant-address">{{ restaurant.address }}</p>
        <div class="restaurant-category">
          <p>{{ restaurant.category }}</p>
        </div>
      </div>
    </div> -->

    <RestaurantHero :restaurantInfos="this.restaurant" />

    <section class="menu">
      <div class="submit-btn-container">
        <button class="submit-btn" v-on:click="toggleAddPlate()">
          Ajouter un plat
        </button>
        <button class="submit-btn" v-on:click="toggleEditInformations()">
          Modifier les informations
        </button>
      </div>
      <div
        class="overlay"
        v-bind:class="{ 'is-open': closeThePopup }"
        v-on:click="closePopup()"
      ></div>
      <div class="grid33-33-33 container">
        <div class="plates" v-for="plate in plates" :key="plate.id">
          <div
            class="plate-container"
            v-on:click="
              togglePlateInformations(),
                getPlate(
                  plate.name,
                  plate.content,
                  plate.picture.url,
                  plate.unitPrice
                )
            "
          >
            <div class="plate-image">
              <img v-bind:src="plate.picture.url" alt />
            </div>
            <div class="plate-informations">
              <h2 class="plate-name">{{ plate.name }}</h2>
              <p class="plate-content" v-if="plate.content != null">
                {{ plate.content | truncate(90) }}
              </p>
              <p>{{ plate.unitPrice }}€</p>
            </div>
          </div>

          <div
            class="plate-popup"
            v-if="platePopupActive"
            v-bind:class="{ 'is-active': platePopupActive }"
          >
            <div class="plate-image">
              <img v-bind:src="onlyOnePlate.image" alt />
            </div>
            <div class="plate-informations">
              <h2 class="plate-name">{{ onlyOnePlate.name }}</h2>
              <p class="plate-content">{{ onlyOnePlate.content }}</p>
              <button
                class="add-to-cart-button"
                v-on:click="togglePlateInformations()"
              >
                Ajouter au panier ({{ onlyOnePlate.unitPrice }}€)
              </button>
            </div>
          </div>

          <div
            class="add-plate-popup"
            v-if="addPlatePopupActive"
            v-bind:class="{ 'is-active': addPlatePopupActive }"
          >
            TEST
          </div>

          <div
            class="add-plate-popup"
            v-if="editInformationsPopupActive"
            v-bind:class="{ 'is-active': editInformationsPopupActive }"
          >
            TEST
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios";
import RestaurantHero from "@/components/hero/restaurant-hero.vue";
export default {
  components: {
    RestaurantHero,
  },
  data: function() {
    return {
      restaurant: null,
      plates: null,
      onlyOnePlate: null,
      platePopupActive: false,
      addPlatePopupActive: false,
      editInformationsPopupActive: false,
      closeThePopup: false,
    };
  },

  mounted: function() {
    this.getRestaurantPlate();
  },
  methods: {
    toggleAddPlate() {
      this.addPlatePopupActive = !this.addPlatePopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    togglePlateInformations() {
      this.platePopupActive = !this.platePopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    toggleEditInformations() {
      this.editInformationsPopupActive = !this.editInformationsPopupActive;
      this.closeThePopup = !this.closeThePopup;
    },
    closePopup() {
      this.closeThePopup = !this.closeThePopup;
      if (this.platePopupActive == true) {
        this.platePopupActive = !this.platePopupActive;
      } else if (this.addPlatePopupActive == true) {
        this.addPlatePopupActive = !this.addPlatePopupActive;
      } else if (this.editInformationsPopupActive == true) {
        this.editInformationsPopupActive = !this.editInformationsPopupActive;
      }
    },
    async getRestaurantPlate() {
      const response = await axios
        .get("/api/restaurant/" + this.$route.params.id + "/plates")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });
      this.restaurant = {
        id: response.data.results.id,
        name: response.data.results.name,
        category: response.data.results.category,
        logo: {
          url: response.data.results.logo.url,
          name: response.data.results.logo.name,
        },
        address: response.data.results.address,
        mail: response.data.results.mail,
        creation: response.data.results.creation,
        selection: response.data.results.selection,
      };

      this.plates = response.data.results.plates;
    },
    getPlate(name, content, image, unitPrice) {
      this.onlyOnePlate = {
        name: name,
        content: content,
        image: image,
        unitPrice: unitPrice,
      };
    },
  },
  filters: {
    truncate: function(value, limit) {
      // console.log(value)
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    },
  },
};
</script>
