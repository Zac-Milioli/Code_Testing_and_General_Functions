<template>
    <v-carousel>
        <v-carousel-item
        v-for="(item, i) in items"
        :key="i"
        :src="item.src"
        cover
        >
        <div class="d-flex fill-height flex-column justify-left align-start ml-10">
            <div class="text-h2">
            TÍTULO TESTE
            </div>
            <div class="text-h4 mt-2">
            Descrição teste
            </div>
        </div>
        </v-carousel-item>
    </v-carousel>
</template>

<script setup>
const items = [
    {src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'},
    {src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'},
    {src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'},
    {src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'}
]
</script>