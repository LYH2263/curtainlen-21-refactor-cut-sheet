<script setup>
import { computed } from 'vue'
const props = defineProps({ cutSheet: { type: Array, default: () => [] } })
const rows = computed(() => (props.cutSheet || []).slice(0, 8))
const total = computed(() => {
  const sheet = props.cutSheet || []
  return sheet.length ? sheet[sheet.length - 1].running_meters : 0
})
</script>
<template>
  <div class="panel-cut">
    <div v-for="row in rows" :key="row.panel_index" class="panel"
      :style="{height: `${(row.cut_height||1)*40}px`}"
      :title="`第 ${row.panel_index} 幅：裁高 ${row.cut_height} m，累计 ${row.running_meters} m`"></div>
    <p>{{ (cutSheet||[]).length }} 幅，末幅累计 {{ total }} m</p>
  </div>
</template>
