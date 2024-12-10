<template>

  <header>
    <NavBar />
  </header>

  <body class="bg-black">
    <div>
      <Carousel :items="carouselData"/>
    </div>
    
    <div id="series">
      <div class="text-h4 ml-10 mt-10">
        Séries
      </div>
      <div class="d-flex">
        <ContentCard class="ma-5" :card="cardDataTest"/>
        <ContentCard class="ma-5" />
        <ContentCard class="ma-5" />
        <ContentCard class="ma-5" />
      </div>
    </div>

    <div id="movies">
      <div class="text-h4 ml-10 mt-10">
        Filmes
      </div>
      <div class="d-flex">
        <ContentCard class="ma-5" :card="cardDataTest"/>
        <ContentCard class="ma-5" />
        <ContentCard class="ma-5" />
        <ContentCard class="ma-5" />
      </div>
    </div>
    
    <div id="all">
      <div class="text-h4 ml-10 mt-10 mb-5">
        Acervo Completo
      </div>
      <v-container>
        <v-column>
          <v-row>
              <ContentCard :card="cardDataTest" />
              <ContentCard />
              <ContentCard />
              <ContentCard />
              <ContentCard />
              <ContentCard />
              <ContentCard />
              <ContentCard />
              <ContentCard />
          </v-row>
        </v-column>
      </v-container>
    </div>
      
  </body>
</template>

<script setup>
import ContentCard from '@/components/ContentCard.vue';

const cardDataTest = {
  src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABbdxecs38o67BVh4u1744XPBp6oA178-ESc2P6anlfeF21ydUOpy6DaxyQVuOhrgpxRQHNo0Fddasvr3rztuZZR63McpZVPB1kE.jpg?r=2ac',
  title: 'True Beauty',
  desc: 'Dorama',
  stars: 4
};

const carouselData = [
    {
        src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
        title: 'Esquilo',
        desc: 'Foto de um esquilinho'
    },
    {
        src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        title: 'Imagem bonita de uma vista glacial',
        desc: 'O título já serviu de descrição'
    },
    {
        src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        title: 'Passarinho',
        desc: 'Na verdade é uma coruja, mas no link da imagem diz "bird.jpg"'
    },
    {
        src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        title: 'Planeta',
        desc: 'Adivinha qual'
    }
]
</script>
