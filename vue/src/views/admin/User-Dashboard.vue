<template>
  <section class="profile-dashboard">
   <ProfileHero :user="this.user"/>
  </section>
</template>

<script>
import axios from "axios";
import ProfileHero from "@/components/hero/profile-hero.vue";

export default {
  components: {
    ProfileHero,
  },
  data: function() {
    return {
      user: null,
    };
  },
  methods: {
    async getUserProfile() {
      const response = await axios
        .get("/api/user/dashboard/profile/" + this.$route.params.id)
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.user = response.data.results;
    },
  },
  mounted: function() {
    this.getUserProfile();
  },
};
</script>
