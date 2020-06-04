<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">Prénom</th>
        <th scope="col">Nom</th>
        <th scope="col">Adresse mail</th>
        <th scope="col">Adresse</th>
        <th></th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.firstName }}</td>
        <td>{{ user.lastName }}</td>
        <td>{{ user.mail}}</td>
        <td>{{ user.address | truncate(40)}}</td>
        <td class="modification-row">
          <button
            class="edit-button"
            v-on:click="
              scrollToTop(),
                $emit('openPopup', true),
                $emit('openOverlay', true),
                $emit('UserId', user.id)
            "
          >
            <i class="fas fa-edit edit"></i>
          </button>
          <!-- <button class="delete-button" v-on:click="deletePlate(plate.id)">
            <i class="fa fa-trash delete"></i>
          </button> -->
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
// import axios from "axios";
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
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    // deletePlate(id) {
    //   console.log("/api/restaurant/delete/plate/" + id);
    //   const response = axios
    //     .post("/api/restaurant/delete/plate/" + id, {
    //       headers: {
    //         "Content-Type": "application/x-www-form-urlencoded"
    //       }
    //     })
    //     .then(function(response) {
    //       return response;
    //     })
    //     .catch(function(error) {
    //       console.log(error);
    //     });

    //   this.info = response.data;
    //   location.reload();
    // }
  }
};
</script>