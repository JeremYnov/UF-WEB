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
      <tr v-for="plate in plates" :key="plate.id">
        <td>
          <img v-bind:src="plate.picture.url" alt />
        </td>
        <td>{{ plate.name }}</td>
        <td v-if="plate.content != null">{{ plate.content | truncate(50) }}</td>
        <td v-else></td>
        <td>{{ plate.type }}</td>
        <td>{{ plate.unitPrice }}</td>
        <td class="modification-row">
          <button class="edit-button">
            <i class="fas fa-edit edit"></i>
          </button>
          <button class="delete-button">
            <i class="fa fa-trash delete"></i>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    plates: null
  },
  filters: {
    truncate: function(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    }
  }
};
</script>