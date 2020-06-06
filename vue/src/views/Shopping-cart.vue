<template>
  <section class="shopping-cart">
    <ShoppingCartHero />
    <div v-if="info != null">
      <div class="message-container" v-if="info.success">
        <div class="success">{{ info.message }}</div>
      </div>
      <div class="message-container" v-else>
        <div class="error">{{ info.message }}</div>
      </div>
    </div>
    <div class="container wrapper">
      <div class="part-container">
        <div class="left-part">
          <h2>Votre commande</h2>
          <div class="cart-plate-container">
            <div v-for="orderContent in orderContents" :key="orderContent.id" class="cart-plate">
              <div class="cart-plate-image">
                <img :src="orderContent.image" alt />
              </div>
              <div class="plate-summary-container grid80-20">
                <div class="cart-plate-informations">
                  <h4>{{ orderContent.name }}</h4>
                  <p>{{ orderContent.type }}</p>
                  <div class="select">
                    <label for="slct">Quantité :</label>
                    <select
                      v-model="orderContent.quantity"
                      @change="setTotalPrice"
                      name="slct"
                      id="slct"
                    >
                      <!-- <option selected disabled>Quantité</option> -->
                      <option selected>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                      <option>6</option>
                      <option>7</option>
                      <option>8</option>
                      <option>9</option>
                      <option>10</option>
                    </select>
                  </div>
                </div>

                <h4>{{ orderContent.price * orderContent.quantity }} €</h4>
              </div>
            </div>
          </div>
        </div>
        <div class="right-part">
          <h2>Récapitulatif</h2>
          <div class="order-summary-container">
            <div class="order-summary grid80-20">
              <p>Total de la commande</p>
              <p>{{ totalPrice }} €</p>
              <p>Frais de livraison</p>
              <p>2,50 €</p>
            </div>
            <div class="total grid80-20">
              <h4>Total</h4>
              <h4>{{ totalPrice + 2.5}} €</h4>
            </div>
            <div class="submit-btn-container">
              <button @click="setAddOrder" class="submit-btn">Payer</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import ShoppingCartHero from "@/components/hero/shopping-cart-hero.vue";

export default {
  components: {
    ShoppingCartHero
  },
  data: function() {
    return {
      idRestaurant: null,
      idUser: null,
      orderContents: null,
      totalPrice: null,
      info: null
    };
  },
  mounted: async function() {
    this.getShoppingCartOrder();
    this.setTotalPrice();
    this.getSessionUser();
  },
  methods: {
    async getSessionUser() {
      const response = await axios
        .get("/api/user/session")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.idUser = response.data.results;
    },
    async setAddOrder() {
      let bodyFormData = new FormData();
      const parsed = JSON.stringify({
        idRestaurant: this.idRestaurant,
        idUser: this.idUser,
        orderContent: this.orderContents
      });

      bodyFormData.set("order", parsed);

      const response = await axios
        .post("/api/order/add", bodyFormData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
    },
    getShoppingCartOrder() {
      const parse = JSON.parse(localStorage.getItem("order"));
      this.orderContents = parse.orderContent;
      this.idRestaurant = parse.idRestaurant;
    },
    setTotalPrice() {
      this.totalPrice = null;
      this.orderContents.forEach(element => {
        this.totalPrice += element.price * element.quantity;
      });
    }
  }
};
</script>
