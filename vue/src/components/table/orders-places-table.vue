<template>
    <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Nom du client</th>
      <th scope="col">Mail du client</th>
      <th scope="col">Adresse du client</th>
      <th scope="col">Date de la commande</th>
      <th scope="col">Total</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="plate in plates" :key='plate.id'>
      <td><img src="" alt=""></td>
      <td>Cheese Burger</td>
      <td>Cheese burger composé de pain de laitue, fromage cheddar et de deux steack haché 100% Français</td>
      <td>@mdo</td>
      <td>@mdo</td>
    </tr>
  </tbody>
</table>
</template>