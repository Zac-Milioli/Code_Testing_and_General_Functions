<template>
  <v-app theme="dark">
    <VAppBar color="black" height="100" title="Aplicativo do Zac"></VAppBar>
    <v-main>
      <VContainer>
        <div
          style="width: 100px; height: 100px;"
          class="border rounded";
          >
          Teste
        </div>
      </VContainer>
      <HelloWorld />
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script setup>
import { VSlideGroup } from 'vuetify/components';

</script>
