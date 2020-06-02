<template>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Image</th>
      <th scope="col">Nom du plat</th>
      <th scope="col">Description</th>
      <th scope="col">Type</th>
      <th scope="col">Prix unitaire</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <!-- <tr v-for="plate in plates" :key='plate.id'> -->
      <td><img src="https://timbuktoo.name/wp-content/uploads/2016/08/Placeholder-300-300.png" alt=""></td>
      <td>Cheese Burger</td>
      <td>Cheese burger composé de pain de laitue, fromage cheddar et de deux steack haché 100% Français</td>
      <td>Burger</td>
      <td>1.99e</td>
      <td class="modification-row"><button class="edit-button"><i class="fas fa-edit edit"></i></button><button class="delete-button"><i class="fa fa-trash delete"></i></button></td>
    <!-- </tr> -->
  </tbody>
</table>
</template>