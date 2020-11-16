<template>
    <nav>
      
    <v-snackbar
      v-model="snackbar"
      color="success"
    >Event has been saved!

      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          OK
        </v-btn>
      </template>
    </v-snackbar>

        <v-toolbar app>
            <v-app-bar-nav-icon class="grey--text" @click="drawer=!drawer"></v-app-bar-nav-icon>
            <v-toolbar-titl class="text-uppercase grey--text">
                <span class="font-weight-light">GIGA</span>
                <span>COW</span>
            </v-toolbar-titl>
            <v-spacer></v-spacer>

            <v-menu offset-y
            :close-on-click="closeOnClick"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                text color="grey"
                v-bind="attrs"
                v-on="on"
              >
              <v-icon left>mdi-arrow-down-drop-circle-outline</v-icon>
              <span> Dropdown menu</span>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                v-for= "item in items"
                :key="item.text"
                route :to="item.route"
              >
                <v-list-item-title>{{ item.text }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
<!--dropdown menu-->
            <v-btn text color="grey">
                <span>Sign out</span>
                <v-icon right>mdi-exit-to-app</v-icon>
            </v-btn>
        </v-toolbar>

        <v-navigation-drawer app v-model="drawer" class="indigo">
          <v-layout column align-center>
            <v-flex class="mt-5">
              <v-avatar size="150">
                <img src="/user1.jpg" alt="">
              </v-avatar>
              <p></p>
            </v-flex>
            <v-flex>
              <Popup />
            </v-flex>
          </v-layout>
            <v-list dense>
      <v-subheader>MENU</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          route :to="item.route"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
import Popup from './Popup'

  export default {
    components: {Popup},
    data (){
      return{
          drawer:false,
          snackbar: true,
          selectedItem: 1,
          items: [
            { text: 'Dashboard', icon: 'mdi-clock', route:'/'},
            { text: 'Dashboard_1', icon: 'mdi-floder', route:'/D1'},
            { text: 'Event list', icon: 'mdi-account', route:'/eventlist' },
            { text: 'Team', icon: 'mdi-flag', route:'/team' },
      ],
      }
    }
  }
</script>
