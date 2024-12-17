<template>
  <div class="ma-2">
    <v-hover v-slot="{ isHovering, props }">
      <v-card class="mx-auto fixed-card" v-bind="props" @click="handleClick">
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

        <v-overlay :model-value="!!isHovering" class="align-center justify-center" scrim="#036358" contained>
          <v-btn variant="flat">Ver mais</v-btn>
        </v-overlay>
      </v-card>
    </v-hover>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  card: {
    type: Object,
    required: true,
    default: () => ({
      src: 'https://th.bing.com/th/id/R.113e1056fd3d22db0495032cb9d819b0?rik=cI3TUWDI6LKivA&pid=ImgRaw&r=0&sres=1&sresct=1',
      title: 'Título',
      desc: 'Descrição',
      stars: 0
    })
  }
});

const emit = defineEmits(['show-overlay']);

const handleClick = () => {
  emit('show-overlay', props.card);
};
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