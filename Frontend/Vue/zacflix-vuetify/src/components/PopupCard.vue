<template>
    <v-card class="mx-auto fixed-card">
        <v-img :src="card.src" class="w-100 fixed-card-img"></v-img>

        <v-card-text>
            <h2 class="text-h6 text-primary">
                {{ card.title }}
            </h2>
            {{ card.desc }}
        </v-card-text>

        <v-card-title>
            <v-rating :model-value="card.stars" background-color="orange" class="me-2" color="orange" dense
                hover></v-rating>
            <span class="text-primary text-subtitle-2">Nota {{ card.stars }}</span>
        </v-card-title>
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
.fixed-card {
    width: 344px;
    height: 355px;
}

.fixed-card-img {
    height: 196px;
}
</style>