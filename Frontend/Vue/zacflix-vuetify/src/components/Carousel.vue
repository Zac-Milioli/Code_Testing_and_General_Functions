<template>
    <div onclick="alert('Clicou no carrossel')">
        <v-carousel hide-delimiters cycle="4">
            <v-carousel-item v-for="(item, i) in items" :key="i" :src="item.src" cover>
                <div class="d-flex fill-height flex-column justify-end align-start gradient-overlay">
                    <div class="text-h2 ml-12">
                        TÍTULO TESTE
                    </div>
                    <div class="text-h4 mb-16 ml-12 mt-5">
                        Descrição teste
                    </div>
                </div>
            </v-carousel-item>
        </v-carousel>
    </div>
</template>

<script setup>
const items = [
    { src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg' },
    { src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' },
    { src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg' },
    { src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg' }
]
</script>

<style>
.gradient-overlay {
    position: relative;
}

.gradient-overlay::before {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to top, black, transparent);
    z-index: 0;
}

.gradient-overlay>div {
    position: relative;
    z-index: 1;
}
</style>