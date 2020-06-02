<template>
  <div class="restaurant">
    <RestaurantHero :restaurantInfos="this.restaurant" />

    <section class="menu">
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
              togglePlateInformations(),scrollToTop(),
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
        </div>
      </div>
    </section>
    <!-- <div
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
                  <select
                    v-model="form.type"
                    name="type"
                    required
                  >
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
                  <input
                    @change="previewFiles"
                    type="file"
                    id="file"
                    required
                  />
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
                <button type="submit" class="submit-btn">
                  Valider
                </button>
              </div>
            </form>
          </div> -->

    <!-- <div
            class="add-plate-popup"
            v-if="editInformationsPopupActive"
            v-bind:class="{ 'is-active': editInformationsPopupActive }"
          >
            TEST
          </div> -->
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
      // addPlatePopupActive: false,
      editInformationsPopupActive: false,
      closeThePopup: false,
      form: {
        name: null,
        type: null,
        description: null,
        unitPrice: null,
        image: null,
      },
    };
  },

  mounted: function() {
    this.getRestaurantPlate();
  },
  methods: {
    // toggleAddPlate() {
    //   this.addPlatePopupActive = !this.addPlatePopupActive;
    //   this.closeThePopup = !this.closeThePopup;
    // },
    scrollToTop() {
      window.scrollTo(0, 0);
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
        description: content,
        image: image,
        unitPrice: unitPrice,
      };
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
    previewFiles: function(event) {
      this.form.image = event.target.files[0];
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
