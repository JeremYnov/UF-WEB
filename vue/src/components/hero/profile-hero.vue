<template>
  <div
      class="hero"
      v-bind:style="{
        'background-image':
          'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),' +
          'url(https://cdn.pixabay.com/photo/2016/04/19/17/07/eat-1339061_1280.jpg)',
      }"
    >
      <div class="hero-content">
        <h1 class>
          {{ user.lastName }}
          <span class="last-name">{{ user.firstName }}</span>
        </h1>
        <p>{{ user.address }}</p>
        <p class="restaurant-address">{{ user.mail }}</p>
        <div class="restaurant-category">
          <p>Solde : {{ user.balance }}€</p>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    props:{
        user : null,
    }

}
</script>

<style>

</style>