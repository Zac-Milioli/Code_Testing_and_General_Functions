<script setup>
import NavBar from '../components/NavBar.vue';
import MoviesCarousel from '../components/MoviesCarousel.vue';
import Movies from '../components/Movies.vue';

</script>

<template>
  <header>
    <NavBar />
  </header>
  <body>
    <MoviesCarousel />
    <Movies />
  </body>
</template>
