<template>
  <c4-page>
    <v-layout column>
      <v-flex v-for="(notification, key) in notifications" :key="key">
        <notification v-if="notification.inComponents.includes('stockChart')"
                      :show="notification.state"
                      :type="notification.type"
                      :message="notification.message"
                      :dismissible="notification.dismissible"
                      :timeout="notification.timeout"
                      :mutation="key">
          <component :is="notification.slot"></component>
        </notification>
      </v-flex>
      <v-flex>
        <v-layout row wrap xs12>
          <v-flex v-for="(states, group) in groupsJobsByStates" :key="group" class="ma-2 flex-equal-size">
            <board xs12 md4 lg4 xl4 :name="group" :flags="flags" :states="states" class="pa-3"></board>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex ma-2 hidden-sm-and-down>
        <stock-chart></stock-chart>
      </v-flex>
    </v-layout>
  </c4-page>
</template>

<script>
import { mapState } from 'vuex'

import { groupsJobsByStates, jobFlags } from '../settings'

import Board from '@/components/Board'
import stockChart from '@/components/StockChart'
import Notification from '@/components/Notification'
import SocketReconnectError from '@/components/notifications/SocketReconnectError'

export default {
  name: 'home',
  components: {
    SocketReconnectError,
    Notification,
    Board,
    stockChart
  },
  methods: {},
  computed: {
    ...mapState({
      'notifications': (state) => state.error
    })
  },
  data () {
    return {
      groupsJobsByStates: groupsJobsByStates, // {waiting: [pending, ..., failed], running: [running], stopped: [error, ..., killed]
      flags: jobFlags, // Z R N K
      dark: false
    }
  }
}
</script>

<style scoped lang="scss">
.flex-equal-size {
  flex: 1 1 0;
}
</style>
