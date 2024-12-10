<template>

  <header>
    <NavBar />
  </header>

  <body class="bg-black">
    <div>
      <Carousel />
    </div>
    
    <div id="series">
      <div class="text-h4 ml-10 mt-10">
        Catálogo de séries
      </div>
      <div class="d-flex">
        <ContentCard />
        <ContentCard />
        <ContentCard />
        <ContentCard />
        <ContentCard />
        <ContentCard />
      </div>
    </div>
      
  </body>
</template>

<script setup>
import ContentCard from '@/components/ContentCard.vue';

  //
</script>
