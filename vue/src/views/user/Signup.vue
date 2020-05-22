<template>
  <div>
    <form @submit.prevent="signup" action method="POST">
      <input v-model="form.firstName" type="text" name="firstName" required />
      <label for="firstName">firstName</label>

      <input v-model="form.lastName" type="text" name="lastName" required />
      <label for="lastName">lastName</label>

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
  name: "Signup",
  data: function() {
    return {
      form: {
        firstName: null,
        lastName: null,
        address: null,
        mail: null,
        password: null,
        repassword: null
      },
      info: null
    };
  },
  methods: {
    signup: function() {
      let bodyFormData = new FormData();

      bodyFormData.set("firstName", this.form.firstName);
      bodyFormData.set("lastName", this.form.lastName);
      bodyFormData.set("address", this.form.address);
      bodyFormData.set("mail", this.form.mail);
      bodyFormData.set("password", this.form.password);
      bodyFormData.set("repassword", this.form.repassword);

      axios
        .post("/api/user/signup", bodyFormData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(function(response) {
          console.log(response);
          this.info = response.data;
          console.log(this.info);
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss">
</style>