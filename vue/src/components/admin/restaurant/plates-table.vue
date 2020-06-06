<template>
  <div>
    <table class="table table-striped" v-if="plates != null">
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
          <td v-if="plate.content != null">
            {{ plate.content | truncate(50) }}
          </td>
          <td v-else></td>
          <td>{{ plate.type }}</td>
          <td>{{ plate.unitPrice }}€</td>
          <td class="modification-row">
            <button
              class="edit-button"
              v-on:click="
                scrollToTop(),
                  $emit('openPopup', true),
                  $emit('openOverlay', true),
                  $emit('plateId', plate.id)
              "
            >
              <i class="fas fa-edit edit"></i>
            </button>
            <button class="delete-button" v-on:click="deletePlate(plate.id)">
              <i class="fa fa-trash delete"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    plates: null,
  },
  filters: {
    truncate: function(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    },
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    deletePlate(id) {
      // console.log("/api/admin/restaurant/delete/plate/" + id);
      const response = axios
        .get("/api/admin/restaurant/" + this.$route.params.id + "/delete/plate/" + id)
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
      location.reload();
    },
  },
};
</script>
