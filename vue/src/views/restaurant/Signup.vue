<template>
  <div>
    <div v-if="info != null">
      <div v-if="info.success">
        <p>Success {{ info.message }}</p>
      </div>
      <div v-else>
        <p>Error {{ info.message }}</p>
      </div>
    </div>

    <form @submit.prevent="signup" method="POST">
      <input v-model="form.name" type="text" name="name" required />
      <label for="name">name</label>

      <input @change="previewFiles" type="file" name="logo" required />
      <label for="logo">logo</label>

      <input v-model="form.address" type="text" name="address" required />
      <label for="address">address</label>

      <input v-model="form.mail" type="email" name="mail" required />
      <label for="mail">mail</label>

      <input v-model="form.password" type="password" name="password" required />
      <label for="password">password</label>

      <input v-model="form.repassword" type="password" name="repassword" required />
      <label for="repassword">repassword</label>

      <button type="submit">Envoyer</button>
    </form>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "RestaurantSignup",
  data: function() {
    return {
      form: {
        name: null,
        logo: null,
        address: null,
        mail: null,
        password: null,
        repassword: null
      },
      info: null
    };
  },
  methods: {
    signup: async function() {
      let bodyFormData = new FormData();

      bodyFormData.set("name", this.form.name);
      bodyFormData.set("logo", this.form.logo);
      bodyFormData.set("address", this.form.address);
      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("password", this.form.password);
      bodyFormData.set("repassword", this.form.repassword);

      const response = await axios
        .post("/api/restaurant/signup", bodyFormData, {
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded; multipart/form-data"
          }
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
    },
    previewFiles: function(event) {
      console.log(event.target.files[0]);
      this.form.logo = event.target.files[0];
    }
  }
};
</script>

<style lang="scss">
</style>