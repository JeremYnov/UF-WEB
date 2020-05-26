<script>
import router from "../../router";
const axios = require("axios");

export default {
  name: "UserLogout",
  mounted: () => {
    axios.get("/api/user/logout").catch(function(error) {
      console.log(error);
    });

    localStorage.removeItem("session");
    router.push("/");
    location.reload();
  }
};
</script>
