<template>
  <section class="shopping-cart">
    <ShoppingCartHero />
    <div class="container wrapper">
      <div class="part-container">
        <div class="left-part">
          <h2>Votre commande</h2>
          <div class="cart-plate-container">
            <div class="cart-plate">
              <div class="cart-plate-image">
                <img
                  src="https://cdn.pixabay.com/photo/2018/05/03/05/19/skewer-3370443_1280.jpg"
                  alt=""
                />
              </div>
              <div class="plate-summary-container grid80-20">
                <div class="cart-plate-informations">
                  <h4>Plate name</h4>
                  <p>Type</p>
                  <div class="select">
                    <label for="slct">Quantité : </label>
                    <select name="slct" id="slct">
                      <!-- <option selected disabled>Quantité</option> -->
                      <option selected value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                      <option value="6">6</option>
                      <option value="7">7</option>
                      <option value="8">8</option>
                      <option value="9">9</option>
                      <option value="10">10</option>
                    </select>
                  </div>
                </div>

                <h4>UNITPRICE x QUANTITY€</h4>
              </div>
            </div>
          </div>
        </div>
        <div class="right-part">
          <h2>Récapitulatif</h2>
          <div class="order-summary-container">
            <div class="order-summary grid80-20">
              <p>Total de la commande</p>
              <p>800€</p>
              <p>Frais de livraison</p>
              <p>2,50€</p>
            </div>
            <div class="total grid80-20">
              <h4>Total</h4>
              <h4>802,50€</h4>
            </div>
            <div class="submit-btn-container">
              <button  class="submit-btn">Payer</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import ShoppingCartHero from "@/components/hero/shopping-cart-hero.vue";
export default {
  components: {
    ShoppingCartHero,
  },
};
</script>
