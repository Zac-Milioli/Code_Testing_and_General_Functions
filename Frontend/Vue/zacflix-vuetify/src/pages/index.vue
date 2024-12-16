<template>
    <header>
      <NavBar />
    </header>
    
    <body class="bg-black">
      <Carousel :items="carouselData"/>
      
      <div id="series">
        <div class="text-h4 ml-10 mt-10">
          Séries
        </div>
        <v-infinite-scroll direction="horizontal">
          <div v-for="item in cardSeries" @load="load">
            <ContentCard class="ma-5" :card="item"/>
          </div>
          <template v-slot:loading />
        </v-infinite-scroll>
      </div>
      
      <div id="movies">
        <div class="text-h4 ml-10 mt-10">
          Filmes
        </div>
        <v-infinite-scroll direction="horizontal">
          <div v-for="item in cardMovies">
            <ContentCard class="ma-5" :card="item" />
          </div>
          <template v-slot:loading />
        </v-infinite-scroll>
      </div>
      
      <div id="all">
        <div class="text-h4 ml-10 mt-10 mb-5">
        Catálogo Completo
      </div>
      <v-container>
        <v-row>
          <div v-for="item in cardSeries">
            <ContentCard :card="item" />
          </div>
          <div v-for="item in cardMovies">
            <ContentCard :card="item" />
          </div>
        </v-row>
      </v-container>
    </div>
  </body>
  
  <footer>
    <Footer />
  </footer>
</template>

<script setup>
const cardSeries = [
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABbdxecs38o67BVh4u1744XPBp6oA178-ESc2P6anlfeF21ydUOpy6DaxyQVuOhrgpxRQHNo0Fddasvr3rztuZZR63McpZVPB1kE.jpg?r=2ac',
    title: 'Beleza Verdadeira',
    desc: 'Dorama',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABWWrRAn-V_9v-3nzoOzbJDiTmWIhl0-yJbC5f4rTD2HxnQNrDDaH-4PnpbOCLZmuDjsQ8dW1wwERCGBUGKdCvXVI75C9H7_EXOJWFlxQ6VxQ5kHsATm72XhoU5-Mj5cqLZgt.jpg?r=233',
    title: 'Uma Advogada Extraordinária',
    desc: 'Dorama',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABd5_AdT8qjsvlwq3D2Tbu4WuxZdqKm_Xhj1o11jn0Fc-DnQ5getp9SueCyDjPNHRgLUmeEap81YXE24_HEboL1c_qOP8zqJc7RT78wBPnxOCgzhbNbVs0ij1553kmAXXfHIBYBhUKaA8bbqdjYyUKRiuR7uC-NfLRaME6BD9LqxBfrm7WuVOtECQPotuAH_9whOxYPWhNgDcpF-I_q4oOAzrl55QTX2G0DtPGSkv7HsJBkkS9zRbT6wsgDTy1VNqjS5r5Z1hZ_Y3FZDQbEKZsqq5OWtvhg1c_4OE05XYG-fCWN7yVPzmr64UqaE.jpg?r=c9c',
    title: 'Cobra Kai',
    desc: 'Ação e artes marciais',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABZtxJS1VGM9FU2Eg2rfSnjd9EI4W8D4rrxZlFO_L37Y_o9MqmmdIKjweU8I3egq4P_2Zjj_gteCrzVHdAJYBajvVX5eQdjTXmGDQAWTdHM2RFsm26nvOARZJSZXIE-VGGBkc.jpg?r=e13',
    title: 'Pousando no Amor',
    desc: 'Dorama',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABYtHI68_5JiWpU-nZsc38gM_N1ef9rRyjOWsgfhQ-haeXyhFFSYYboJ-f1WnhRux0z_rKZUa1C9bupMluM44jbSTHt8tRPDEsyd55X4HGCSXcWDCkKwAJVyVSlhKVHPBLoFt.jpg?r=20b',
    title: 'Bridgerton',
    desc: 'Romance de época',
    stars: 3
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABZUteytz_1MKSu0W_j3umM-wve7H_iV-SA4YZjdBD9hTlLYgdKaI7r5_D5THHlIJNg9ijWlCLjfzfEeS0jL6l6EqZD6_1HImwLxyRfJjK2hOtOSZjjF4sZJc-a7AlfRC_4jCpFeMnjQHvHHq3-pBTEwOzJcKvqescQECdNgH35O2ydJQiPg6g9w8v6LaFRT-S05iVAnuISM7GNxCENj8Wu1Ut_iEwu6Efzjws3x1f9EEHeOT8Jvw-t66gL0kQkDPO378B61FIr4qkVvA9NsEUT__IBPixdrUN58xEUKo5z-hAmlu1PoLIIJJFNDYzdclRuNGalBxri7jMLTmobXRarWILL5bNigoP8VG9jc8WLNcGIxMDaIPaHNoDqE-itt0NHrBmlgrNQeYDOmJMPD-qufdRDH0USiTjFVG_HYoEbbOgjhgsaI8JMbZS0PemxY2PxYmTedakAmh1jk1ManD7be41bR07ErQbvvw3wER3Edccw.jpg?r=d61',
    title: 'Dandadan',
    desc: 'Anime',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABSKlvK3bRW8pv_CVqKWNbIe2Bw77uJhIoKtKL6x63kRsyZIcHbEzq8wcWFEIKLqcy8O09TwiakQDFBpt29ZRN2Tyt-UdriOsSRAwtQHRpg4GFl51GYCQj7QN3W9KxTlE4G_v.jpg?r=875',
    title: 'Sorriso Real',
    desc: 'Dorama',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABbwDwQOIo8soVe7woP8_4Q8BkX_B_YZkJkXxHqLICYw-BNEM9gm9QHD9REZDfKo9IAgd_YamVR8_siuaNV5f586NUqvCfDzxzqRjtjHLz1VEV2i1-Th1XA7fmcp_i2kpScWh.jpg?r=371',
    title: 'Meu Demônio Favorito',
    desc: 'Dorama',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABcOiZj9ywUqeoL0jS65tjl4WIUkEHDuX586xD4nwLo31Ckcca7GVqpWRSdlA68_Yl8sDShkFV7XJqlLA3m6npwYdjKpOPZCgKHpE7Ztbhsckq-hJf6xK9H3PUVSdGRWCh6CH.jpg?r=3f9',
    title: 'Pretendente Surpresa',
    desc: 'Dorama',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABSitjBhxTkmKXKaLTESIa5iQ58nAyggjQUOYupjSwRe4gUR-_YAITsOHD6tTTZNuBfh0ssBesZYcvf9X7kTOjYj9LklBcD2gEr8rFmNxUtSBec4jGBl4Faf5hCl09TqioZr0.jpg?r=c8b',
    title: 'Vicenzo',
    desc: 'Dorama',
    stars: 2
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABde-cEKvUZqr0SiiMfVgkeeC9wtDzvVZ1R45cmn1HIycqtDLKJ2yxhrT4lM7XhB_ZlAg-iaNfglwDSMtCWP2wnCR-XeXYbSkyz3ALBnZhFA_hMWbMm9koX1AmVLdebRYcHKz8UQWEvTpNd8QpRyLzXMZHimQAClkFCkpDRZxyjKEOL1USP9Wy6U0O6rHBNCCk9lWC26icGshRaA91LDN6c6uFOavqJ7RsNCGt2o-_xt57RJKPZSs6nRufvUDGITg_kpiUQaAl3ITcpxw4y7uhAtKZTigDO9b4agEfvi3LsJc2oniT7_jHgSwMxbp1EejUGjNezdCnF6uGDXdndzE9P8F7PfUikwq83qVB3c2YDDxHfFSaDgWrUBSCL1e8fUest2pAbVJkWFaREM7EdqOm-hqNn4Bt-FNsYoUeV2VQ1mfhnE.jpg?r=880',
    title: 'SPY x FAMILY',
    desc: 'Anime',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABYEEpNTurltJ3caJtxnQSXI0OPiI41kO6xfjYs6E7X-VaGijigNSJegKAEG3d9Wk8Y88Oflr3I5Kpv_SXGZmpmvR0HnveGpsjmsnMVydNmcSCMyZmIMU2bDA7C-S6cYdTPkQVAIdkXGDBh8ivjNC4BHrcp4oxLeRCAH8G_fswbJKcMDaDsBT1hfcKg61y1FIDzhTLk8YlMYLa6pjk7cCJlSbp9tvX214hkW09AQsdb_Paa9ITXIlWfHb39iqhyTHHTuV2nHEkAiGQwH8dK_9FLJY6hlKxVs.jpg?r=094',
    title: 'Naruto Shippuden',
    desc: 'Anime',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABbt4w1Q0xwQo1sLi6XPGZL7bQImp6txKnHi6uB28Yflwd0G-MVis3AlL6uZ2v1yJDDP7_kjltix5SzTToBK9ShiQlII40qsRB74.jpg?r=535',
    title: 'Demon Slayer',
    desc: 'Anime',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABVTc8b2MDbOG79wxqwEyARxHpd2w3wlKbXCCdrziH49A3g74J5sCr4Dskm97KeauGN2TNqdF7FvoHYIxiv42I4mwUnWtYUHruhQ.jpg?r=739',
    title: 'Jujutsu Kaisen',
    desc: 'Anime',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABUps_ZR1iQfepCZnKrBczl9Fp3qgAQyK0kUN-FurkMJ3tFt90fsvx-K4-dUCkMTuNpX5vHdv0oRHNSG3tkX13n-liuIpuJ-tHu8.jpg?r=b92',
    title: 'My Hero Academia',
    desc: 'Anime',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABaCC0LmSovKE1ji0XhC4EGzgtyg2QsG-iDKZ-5X7afHqX-leCm-WLoE0FLE921rKEmqu9hXMfblFBZhSAcmgh-srjL6BA2RwWJs.jpg?r=888',
    title: 'Haikyuu!!',
    desc: 'Anime',
    stars: 3
  },
]

const cardMovies = [
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABaVxfoIy1wQB73i3kFcJRB2KFfXZ64prYgGoE7aUzc9RcUtaXilcQxr5nhXIV_HW6gdSHW9zOBRb8YRgj6mwsaZncmJG6HwuYJs.jpg?r=c71',
    title: 'Homem-Aranha: Longe de Casa',
    desc: 'Ação e Aventura',
    stars: 4
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABU_kI_8yE_yMz5vUfSoU3DUZ4gQyjbqq0rluXGk1ab0mEBDUNtcIeSOuDe8to1Q00v9tOC81dDwBUngxAgJKBX2oMVXVmTplPmAHbNP0usF51fOGXtTGcsciLxs1-kK1wDfL.jpg?r=d54',
    title: 'Donzela',
    desc: 'Ação e Aventura',
    stars: 2
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABaKozK53norgbS8RtJKpexUlakpYM_H3hdk9jVaqmWehbOUpD1FQ40crDy46yYB9bchxMUEceeEJxaSbMz-bTKq24VtPNQ332po.jpg?r=6af',
    title: 'Homem-Aranha',
    desc: 'Ação e Aventura',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABeXjftJU-S8u0cK6uVzQ4TkfwE16nlTSVoTvoK9wDPKQI_b2WQ4SZHJineK98Nt8gWDdapT8E4jTWOUP9sD5MCzLIfXZg1h9Y8k.jpg?r=f4c',
    title: 'O Lar das Crianças Peculiares',
    desc: 'Ação, Aventura e Drama',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABZGPBq_wJKZLqBqoCS4wAiEMHBx0dwahsUxixXuz13JTHForDhM3DOrifzhODhmi9yOUVqVi7ve1Ar0Fm17MWeN1OA1H4LTE4zE.jpg?r=2c9',
    title: 'Kung-fusão',
    desc: 'Ação e Artes Marciais',
    stars: 5
  },
  {
    src: 'https://occ-0-3824-185.1.nflxso.net/dnm/api/v6/Qs00mKCpRvrkl3HZAN5KwEL1kpE/AAAABb3H5HeRyxS_BJd6eZXJgYrNFD5gNhDo8zz2FvGvPBQxd83soWqx_qvhAJ2G51e6XSKG3h9PlL-queK9slvN1oX-wVKr6Avm9Tw.jpg?r=6eb',
    title: 'Depois da Terra',
    desc: 'Ação, Ficção Científica e Aventura',
    stars: 3
  }
]

const carouselData = [
    {
        src: 'https://assets.nflxext.com/ffe/siteui/vlv3/158a0e2a-cca4-40f5-86b8-11ea2a281b06/web_collection/BR-pt-20241202-TRIFECTA-fc4a2711-5d9f-4bd0-b2bd-c9e24ab06fdb_large.jpg',
        title: 'ZacFlix: Séries e Filmes',
        desc: 'Na verdade aqui não tem nada, é meio que um asset flip só pra aprender Vue e Vuetify'
    },
    {
        src: 'https://assets.nflxext.com/ffe/siteui/vlv3/522bb1bd-bd7a-4b41-9331-3350f25c97fc/web_collection/BR-pt-20241202-TRIFECTA-00b67504-679d-49d3-b1b7-f0fb69a5d4f8_large.jpg',
        title: 'Website feito para você',
        desc: 'Na verdade vai pro meu currículo'
    },
    {
        src: 'https://assets.nflxext.com/ffe/siteui/vlv3/fdcaf638-4ea0-4335-9cdb-a044f97cf39f/web_collection/BR-pt-20241202-TRIFECTA-dbf8d4d2-8f3c-44a2-a083-fdfda3d48a0f_large.jpg',
        title: 'Variedade para toda a família',
        desc: 'Eu só assisto anime e dorama, então praticamente só tem isso em séries'
    },
    {
        src: 'https://assets.nflxext.com/ffe/siteui/vlv3/0cc52fea-b37f-493d-b440-3c7aee3a9043/web_collection/BR-pt-20241202-TRIFECTA-77e39a44-90b9-4146-a8eb-17ebb13f0aad_large.jpg',
        title: 'Conteúdo original',
        desc: 'Peguei todas as imagens diretamente da Netflix, não tem nada original além do código'
    },
    {
        src: 'https://assets.nflxext.com/ffe/siteui/vlv3/9ce12859-9333-4eb1-b50c-d33d8e3d07cb/web_collection/BR-pt-20241202-TRIFECTA-0004a270-edae-4a1d-b8c1-6caf5b446cd6_large.jpg',
        title: 'Interface moderna e responsiva',
        desc: 'Vou concordar com esse, deu um trabalho'
    },
];
</script>
