<template>
  <div class="restaurant">
      <h1>{{id}}</h1>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      id: 0
    };
  },
  mounted: function() {
      this.id = this.$route.params.id
  }
};
</script>