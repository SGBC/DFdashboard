<template>
    <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Add new event
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          NEW EVENT
        </v-card-title>

        <v-card-text>
          <v-form class="px-3">
            <v-text-field label="Title" v-model="title"></v-text-field>
            <v-textarea label="Information" v-model="content"></v-textarea>
            <v-menu
          v-model="menu1"
          :close-on-content-click="false"
          max-width="290"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              :value="date"
              clearable
              label="Date"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            @change="menu1 = false"
          ></v-date-picker>
        </v-menu>
                
            <v-btn text class="success mx-0 mt-3" @click="submit">Save</v-btn>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
export default {
    data(){
        return{
            dialog: false,
            title:'',
            content:'',
            due:null,
        }
    },
    methods:{
        submit(){
          console.log(this.title, this.content)
        }
    }
}
</script>