<template>
  <div class="home-container">
      <Hero />
    <section class="our-selection">
      <h2 class="section-title">Notre selection</h2>
      <div class="grid33-33-33">
        <div class="presentation-card-container">
          <div class="card-image">
            <img
              src="https://cdn-food.konbini.com/images/files/2017/06/capture-decran-2017-06-15-a-11.43.30.jpg?webp="
              alt
            />
          </div>
          <div class="card-title"></div>
          <div class="card-note"></div>
          <div class="card-category"></div>
        </div>
        <div class="presentation-card-container">
          <div class="card-image">
            <img
              src="https://cdn-food.konbini.com/images/files/2017/06/capture-decran-2017-06-15-a-11.43.30.jpg?webp="
              alt
            />
          </div>
          <div class="card-title"></div>
          <div class="card-note"></div>
          <div class="card-category"></div>
        </div>
        <div class="presentation-card-container">
          <div class="card-image">
            <img
              src="https://cdn-food.konbini.com/images/files/2017/06/capture-decran-2017-06-15-a-11.43.30.jpg?webp="
              alt
            />
          </div>
          <div class="card-title"></div>
          <div class="card-note"></div>
          <div class="card-category"></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Hero from "@/components/hero/hero.vue";

export default {
  name: "Home",
  components: {
    // HelloWorld,
    Hero
  }
};
</script>
