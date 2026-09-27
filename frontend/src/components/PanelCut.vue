<script setup>
defineProps({ rows: { type: Array, default: () => [] } })
</script>
<template>
  <div class="panel-cut">
    <div v-for="row in rows.slice(0, 8)" :key="row.panel_index" class="panel"
      :style="{height: `${row.cut_height*40}px`}"
      :title="`第${row.panel_index}幅 累计 ${row.running_meters} m`"></div>
    <p v-if="rows.length">{{ rows.length }} 幅 × {{ rows[0].cut_height }} m = {{ rows[rows.length-1].running_meters }} m</p>
  </div>
</template>
