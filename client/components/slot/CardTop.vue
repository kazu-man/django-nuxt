<template>
    <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
          <v-row dense>
              <v-col cols="6">
                <v-card-title class="text-h5">
                     <slot name="title"/>
                </v-card-title>

                <v-card-title
                class="text-h4"
                style="font-size:1.8rem;padding-left:10%"
                >
                    <slot name="total"/>
                </v-card-title>
              </v-col>

              <v-col cols="6">
                <div style="height:100%">
                    <slot name="content"/>
                </div>
              </v-col>              
          </v-row>

          </v-card>
    </v-col>
</template>