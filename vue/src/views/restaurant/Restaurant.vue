<template>
  <div class="restaurant">
    <RestaurantHero :restaurantInfos="this.restaurant" />

    <section class="menu">
      <div class="overlay" v-bind:class="{ 'is-open': closeThePopup }" v-on:click="closePopup()"></div>
      <div class="grid33-33-33 container">
        <div class="plates" v-for="plate in plates" :key="plate.id">
          <div
            class="plate-container"
            v-on:click="
              togglePlateInformations(),scrollToTop(),
                getPlate(
                  plate.id,
                  plate.name,
                  plate.type,
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
              <p
                class="plate-content"
                v-if="plate.content != null"
              >{{ plate.content | truncate(90) }}</p>
              <p>{{ plate.unitPrice }}€</p>
            </div>
          </div>
        </div>
      </div>
    </section>
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
        <p class="plate-content">{{ onlyOnePlate.description }}</p>
        <button
          class="add-to-cart-button"
          v-on:click="togglePlateInformations(), addShoppingCart(onlyOnePlate)"
        >Ajouter au panier ({{ onlyOnePlate.unitPrice }}€)</button>
      </div>
    </div>
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

              <div class="submit-btn-container">
                <button type="submit" class="submit-btn">
                  Valider
                </button>
              </div>
            </form>
    </div>-->

    <!-- <div
            class="add-plate-popup"
            v-if="editInformationsPopupActive"
            v-bind:class="{ 'is-active': editInformationsPopupActive }"
          >
            TEST
    </div>-->
  </div>
</template>

<script>
import axios from "axios";
import RestaurantHero from "@/components/hero/restaurant-hero.vue";
export default {
  components: {
    RestaurantHero
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
      // form: {
      //   name: null,
      //   type: null,
      //   description: null,
      //   unitPrice: null,
      //   image: null
      // },
      order: null
    };
  },

  mounted: async function() {
    await this.getRestaurantPlate();

    this.order = {
      idRestaurant: this.restaurant.id,
      // idUser: JSON.parse(localStorage.getItem("session")).user.id,
      orderContent: []
    };
  },
  methods: {
    addShoppingCart(plate) {
      let similar = false;

      if (this.order.orderContent.length != 0) {
        this.order.orderContent.forEach(element => {
          if (element.id == plate.id) {
            similar = true;
          } else {
            similar = false;
          }
        });
      }

      if (!similar) {
        this.order.orderContent.push({
          id: plate.id,
          price: plate.unitPrice,
          name: plate.name,
          type: plate.type,
          image: plate.image,
          quantity: 1
        });
      }

      this.saveShoppingCart(this.order);
    },
    saveShoppingCart(params) {
      const parsed = JSON.stringify(params);
      localStorage.setItem("order", parsed);
    },
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
          name: response.data.results.logo.name
        },
        address: response.data.results.address,
        mail: response.data.results.mail,
        creation: response.data.results.creation,
        selection: response.data.results.selection
      };

      this.plates = response.data.results.plates;
    },
    getPlate(id, name, type, content, image, unitPrice) {
      this.onlyOnePlate = {
        id: id,
        name: name,
        type: type,
        description: content,
        image: image,
        unitPrice: unitPrice
      };
    }
  },
  filters: {
    truncate: function(value, limit) {
      // console.log(value)
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    }
  }
};
</script>
