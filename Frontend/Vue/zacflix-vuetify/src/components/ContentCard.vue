<template>
    <div>
    <v-hover v-slot="{ isHovering, props }">
      <v-card
        class="mx-auto"
        max-width="344"
        v-bind="props"
      >
        <v-img src="https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABbdxecs38o67BVh4u1744XPBp6oA178-ESc2P6anlfeF21ydUOpy6DaxyQVuOhrgpxRQHNo0Fddasvr3rztuZZR63McpZVPB1kE.jpg?r=2ac"></v-img>

        <v-card-text>
          <h2 class="text-h6 text-primary">
            Nome do filme
          </h2>
          Descrição
        </v-card-text>

        <v-card-title>
          <v-rating
            :model-value="4"
            background-color="orange"
            class="me-2"
            color="orange"
            dense
            hover
          ></v-rating>
          <span class="text-primary text-subtitle-2">Avaliação</span>
        </v-card-title>

        <v-overlay
          :model-value="!!isHovering"
          class="align-center justify-center"
          scrim="#036358"
          contained
        >
          <v-btn variant="flat">Ver mais</v-btn>
        </v-overlay>
      </v-card>
    </v-hover>
  </div>
</template>

<script setup>
</script>
