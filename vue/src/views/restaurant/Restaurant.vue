<template>
  <div class="restaurant">
      <h1>{{id}}</h1>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      id: ""
    };
  },
  mounted: function() {
    this.id = window.location.href;
    this.id = this.id.split("restaurant/");
    // console.log(this.id)
    // this.id = this.id[this.id.length - 1];
    this.id = Number(this.id[1]);
    // console.log(this.id)
  }
};
</script>