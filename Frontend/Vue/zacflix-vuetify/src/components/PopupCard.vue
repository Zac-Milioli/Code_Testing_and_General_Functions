<template>
    <v-card width="80%" color="black" class="mx-auto d-flex flex-row">
        <div class="d-flex flex-column justify-center align-start p-4" style="flex: 1;">
            <v-card-text>
                <h2 class="text-h3 text-primary">
                    {{ card.title }}
                </h2>
                <div class="text-h5">
                    {{ card.desc }}
                </div>
            </v-card-text>
            <v-card-title>
                <v-rating :model-value="card.stars" background-color="orange" class="me-2" color="orange" dense
                    hover></v-rating>
            </v-card-title>
        </div>
        <div class="image-container" style="flex: 1;">
            <v-img :src="card.src" class="fixed-card-img"></v-img>
        </div>
    </v-card>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    card: {
        type: Object,
        required: true,
        default: () => ({
            src: '',
            title: '',
            desc: '',
            stars: 0
        })
    }
});
</script>

<style scoped>
.image-container {
    position: relative;
}

.fixed-card-img {
    width: 100%;
    height: auto;
    max-height: 100%;
}

.image-container::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to left, transparent 70%, black);
    z-index: 1;
}
</style>