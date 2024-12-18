<template>
    <v-carousel hide-delimiters cycle="4">
        <v-carousel-item v-for="(item, i) in items" :key="i">
            <v-parallax :src="item.src" height="500">
                <div class="d-flex fill-height flex-column justify-end align-start gradient-overlay">
                    <div class="text-h2 ml-12">
                        {{ item.title }}
                    </div>
                    <div class="text-h4 mb-16 ml-12 mt-5">
                        {{ item.desc }}
                    </div>
                </div>
            </v-parallax>
        </v-carousel-item>
    </v-carousel>
</template>

<script setup>
const props = defineProps({
    items: {
        type: Array,
        required: true,
        default: () => ([
            {
                src: 'https://th.bing.com/th/id/R.113e1056fd3d22db0495032cb9d819b0?rik=cI3TUWDI6LKivA&pid=ImgRaw&r=0&sres=1&sresct=1',
                title: 'Título',
                desc: 'Descrição'
            },
            {
                src: 'https://th.bing.com/th/id/R.113e1056fd3d22db0495032cb9d819b0?rik=cI3TUWDI6LKivA&pid=ImgRaw&r=0&sres=1&sresct=1',
                title: 'Título 2',
                desc: 'Descrição 2'
            }
        ])
    }
});
</script>

<style scoped>
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
