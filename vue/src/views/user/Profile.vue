<template>
  <div></div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      user: null
    };
  },
  mounted: function() {
    this.getProfile();
  },
  methods: {
    async getProfile() {
      const response = await axios
        .get("/api/user/profile")
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.user = response.data.results;
    }
  }
};
</script>