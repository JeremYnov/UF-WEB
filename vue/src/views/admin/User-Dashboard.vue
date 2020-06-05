<template>
  <div class="sidebar-wrapper">
    <Sidebar />
    <div class="main_content">
      <ProfileHero :user="this.user" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProfileHero from "@/components/hero/profile-hero.vue";
import Sidebar from "@/components/layouts/sidebar.vue"

export default {
  components: {
    ProfileHero,
    Sidebar
  },
  data: function() {
    return {
      user: null
    };
  },
  methods: {
    async getmemberProfile() {
      const response = await axios
        .get("/api/admin/member/" + this.$route.params.id + "/profile")
        .then(function(response) {
          console.log(response);

          return response;
        })
        .catch(function(error) {
          console.log(error);
        });

      this.user = response.data.results;
    }
  },
  mounted: function() {
    this.getmemberProfile();
  }
};
</script>
