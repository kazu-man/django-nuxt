<template>
  <v-card
    class="mx-auto"
    style="margin-top:10px;width:80%"
  >
    <v-spacer></v-spacer>

    <slot name="top_area"></slot>

    <v-container>
      <v-row dense>

        <slot name="card_header" />
        <slot name="card_body" />

      </v-row>
    </v-container>
  </v-card>
