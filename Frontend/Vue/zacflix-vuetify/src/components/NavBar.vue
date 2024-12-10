<template>
  <VAppBar height="150" color="black">
    <div class="d-flex align-center justify-space-between ma-10 fill-height w-100">
      <div class="d-flex align-center">
        <VAppBarNavIcon class="mb-5" href="#">
          <img src="../assets/zacflix-logo.png" width="60" />
        </VAppBarNavIcon>
        <VAppBarNavTitle class="ml-8 text-red text-h4">
          <strong>ZacFlix</strong>
        </VAppBarNavTitle>
      </div>
      <div class="d-flex align-center">
        <VBtn href="#series" class="ml-15">
          Séries
        </VBtn>
        <VBtn href="#movies" class="ml-2">
          Filmes
        </VBtn>
        <VBtn href="#all" class="ml-2">
          Catálogo completo
        </VBtn>
      </div>
    </div>
  </VAppBar>
</template>

<script setup>
//
</script>


<style>
</style>