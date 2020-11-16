<template>
  <v-app>
    <Navbar />
    <Tabs />
    <v-main>  <!--content-->
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
import Tabs from '@/components/Tabs'
export default {
  name: 'App',
  components:{ Navbar, Tabs },
  data () {
    return{
      //
    }
  }
};
</script>
