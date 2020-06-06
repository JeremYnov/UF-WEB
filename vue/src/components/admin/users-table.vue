<template>
  <section class="members" v-if="users != null">
    <div
      class="alert alert-warning"
      role="alert"
      v-if="users.length == 0"
    >
      Aucun membre
    </div>
    <table class="table table-striped" v-if="users.length != 0">
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
          <td>{{ user.mail }}</td>
          <td>{{ user.address | truncate(40) }}</td>
          <td class="modification-row">
            <router-link
              v-bind:to="{
                name: 'AdminUserDashboard',
                params: { id: user.id },
              }"
            >
              <button class="edit-button">
                <i class="fas fa-edit edit"></i>
              </button>
            </router-link>
            <button class="delete-button" v-on:click="setMemberDelete(user.id)">
              <i class="fa fa-trash delete"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      users: null,
      info: null,
    };
  },
  filters: {
    truncate: function(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + "...";
      }
      return value;
    },
  },
  mounted() {
    this.getAllMember();
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    async getAllMember() {
      const response = await axios
        .get("/api/admin/list/member")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.users = response.data.results;
    },
    async setMemberDelete(id) {
      const response = await axios
        .get("/api/admin/member/" + id + "/delete")
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      console.log(response.data);

      this.info = response.data;

      if (response.data.success) {
        location.reload();
      }
    },
  },
};
</script>
