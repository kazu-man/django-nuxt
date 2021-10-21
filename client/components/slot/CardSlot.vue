<template>
    <v-card
    color="#385F73"
    dark
    >
    <v-card-text style="padding-bottom:5px">
        <v-row>
            <v-col cols="3" style="padding:0 12px 0 12px;height:100%">
                <v-card-text style="padding:15px 10px 5px 10px;height:40%">

                    <slot name="date"></slot>

                </v-card-text>
                <v-card-title  style="padding: 0px 10px;"
                >
                    <slot name="total"></slot>

                </v-card-title>
            </v-col>

            <v-col cols="7" style="padding:0 0 0 12px;height:100%">
                    <slot name="content"></slot>
            </v-col>  

            <v-col cols="2" style="padding:0 0 0 12px;height:100%">

                <slot name="right_area"></slot>

            </v-col>       
        </v-row>
    </v-card-text>
    </v-card>
</template>
