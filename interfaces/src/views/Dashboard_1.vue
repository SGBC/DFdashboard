<template>
  <v-container>
    <v-row >
      <v-col>
      <v-row v-for="i in 2" :key="i">
        <v-col v-for="i in 2" :key="i">
            <v-card>
                <v-flex> <Plots /></v-flex>
            </v-card>
        </v-col>
      </v-row>      
      </v-col>
      <v-col text
        cols="6"
        md="4"
      >
       <v-card>
           <div class="overline mb-4">
                Overview
            </div>
           <Overview/>
       </v-card>
        <v-card text> 
            <div class="overline mb-4">
                Event list
            </div>
          <Event />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Plots from '@/components/Plots'
import Event from '@/components/Event'
import Overview from '@/components/Overview'
export default {
    components:{ Plots, Event, Overview },
}
</script>