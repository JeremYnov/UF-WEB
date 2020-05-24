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
      <input v-model="form.userName" type="text" name="userName" required />
      <label for="userName">userName</label>

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
  name: "AdminSignup",
  data: function() {
    return {
      form: {
        userName: null,
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

      bodyFormData.set("userName", this.form.userName);
      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("password", this.form.password);
      bodyFormData.set("repassword", this.form.repassword);

      const response = await axios
        .post("/api/admin/signup", bodyFormData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(function(response) {
          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.info = response.data;
    }
  }
};
</script>

<style lang="scss">
</style>