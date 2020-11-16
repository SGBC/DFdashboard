<template>
  <div class="Event_list">
    <v-container>
      <v-expansion-panels>
        <v-expansion-panel
          v-for="project in projects" :key="project.Title"
        >
          <v-expansion-panel-header>{{project.Title}}</v-expansion-panel-header>
          <v-expansion-panel-content>
            <div class="font-weight-bold">due by {{project.Date}}</div>
            <div>information</div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  data(){
    return{
      projects:[
        { Title: 'Todo1', Person: 'AAA', Date: 'YYYY-MM-DD', status:'Ongoing'},
        { Title: 'Todo2', Person: 'BBB', Date: 'YYYY-MM-DD', status:'Complete'},
        { Title: 'Todo3', Person: 'CCC', Date: 'YYYY-MM-DD', status:'Overdue'},
    ]
    }
  },
  //filter function
  //computed:{
    //myprojects(){
      //return this.projects.filter(project => {
        //return project.Person === 'AAA'
      //})
    //}
  //}
}
</script>
