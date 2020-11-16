<template>
  <div class="Dashboard">
    <h2 class="grey--text">Dashboard</h2>
    <v-container class="my-5">
       <Plots />
      <v-layout row class="mb-3">
        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-btn small text color="grey" @click="sortBy('Title')" v-bind="attrs" v-on="on">
              <v-icon left small>mdi-folder</v-icon>
              <span class="caption text-lowercase">By event</span>
            </v-btn>
          </template>
        <span>Sort the list by event name</span>
        </v-tooltip>

        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-btn small text color="grey" @click="sortBy('Person')" v-bind="attrs" v-on="on">
              <v-icon left small>mdi-account-cowboy-hat</v-icon>
             <span class="caption text-lowercase">By name</span>
          </v-btn>
          </template>
        <span>Sort the list by person</span>
        </v-tooltip>
        
        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-btn small text color="grey" @click="sortBy('Date')" v-bind="attrs" v-on="on">
            <v-icon left small>mdi-alarm-check</v-icon>
            <span class="caption text-lowercase">By time</span>
        </v-btn>
          </template>
        <span>Sort the list by due time</span>
        </v-tooltip>
        
        
      </v-layout>
      <v-card v-for="(project, i) in projects"
          :key="i"> 
      <v-layout row wrap :class="`pa-3 project ${project.status}`">
        <v-flex xs12 md6>
          <div class="caption grey--text">Event</div>
          <div v-text="project.Title"></div>
        </v-flex>

        <v-flex xs6 sm4 md2>
          <div class="caption grey--text">Person</div>
          <div>{{project.Person}}</div>
        </v-flex>
        
        <v-flex xs6 sm4 md2>
          <div class="caption grey--text">Date</div>
          <div>{{project.Date}}</div>
        </v-flex>

        <v-flex xs2 sm4 md2>
          <div class="right">
            <v-chip  small :class="`${project.status} white--text caption my-2`">
                {{project.status}}
            </v-chip>
          </div>
        </v-flex>
      </v-layout>
      <v-divider></v-divider>
    </v-card>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Plots from '@/components/Plots'
export default {
  components:{ Plots },
  data(){
    return{
      //notification list
      projects:[
        { Title: 'Todo1', Person: 'AAA', Date: 'YYYY-MM-DD', status:'Ongoing'},
        { Title: 'Todo2', Person: 'BBB', Date: 'YYYY-MM-DD', status:'Complete'},
        { Title: 'Todo3', Person: 'CCC', Date: 'YYYY-MM-DD', status:'Overdue'},
    ],
    }

  },
  methods: {
    sortBy(prop){
      this.projects.sort((a,b) => a[prop] > b[prop] ? -1 : 1)
    }
  },
}
</script>

<style>
.v-chip.Complete{
  border-left:4px solid green;
}

.v-chip.Ongoing{
  border-left:4px solid orange;
}

.v-chip.Overdue{
  border-left:4px solid tomato;
}
</style>