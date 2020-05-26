<script>
import router from "../../router";
const axios = require("axios");

export default {
  name: "UserLogout",
  data: () => {
    return {};
  },
  mounted: async () => {
    const response = await axios
      .get("/api/user/logout")
      .then(function(response) {
        return response;
      })
      .catch(function(error) {
        console.log(error);
      });

    localStorage.setItem("session", response.data.session);
    router.push("/");
    location.reload();
  }
};
</script>
