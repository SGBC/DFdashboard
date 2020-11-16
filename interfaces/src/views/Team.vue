<template>
  <div class="Team">
    <h1 class="subheading grey--text">Team</h1>
    <v-container class="my-5">
      <v-layout row warp>
        <v-flex xs12 sm6 md4 lg3  v-for="person in members" :key="person.name">
          <v-card class="text-center ma-3">
              <v-responsive class="pt-4">
                <v-avatar size="100" class="grey lighten-2">
                  <img :src="person.avatar">
                </v-avatar>
              </v-responsive>
              <v-card-text>
                <div class="subheading">{{person.name}}</div>
                <div class="grey--text">{{person.role}}</div>
              </v-card-text>
              <v-card-actions>
                <v-btn text color="grey"> 
                  <v-icon small left>mdi-badge-account-horizontal</v-icon>
                  <span>Message</span>
                </v-btn>
              </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  data(){
    return{
    members:[
      {name: 'AAA', role:'*****', avatar: '/user1.jpg'},
      {name: 'BBB', role:'*****', avatar: '/user2.jpg'},
      {name: 'CCC', role:'*****', avatar: '/user3.jpg'}
    ]
    }
    
  }
}
</script>
