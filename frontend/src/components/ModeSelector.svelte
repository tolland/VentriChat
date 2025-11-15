<script lang="ts">
  import { createEventDispatcher } from 'svelte'
  import type { DistortionMode } from '../types'

  export let modes: DistortionMode[]
  export let selectedMode: string

  const dispatch = createEventDispatcher<{ change: string }>()

  function handleChange(event: Event) {
    const target = event.target as HTMLSelectElement
    dispatch('change', target.value)
  }
</script>

<div class="mode-selector">
  <label for="mode">Distortion Mode:</label>
  <select id="mode" value={selectedMode} on:change={handleChange}>
    {#each modes as mode}
      <option value={mode.id}>
        {mode.name}
      </option>
    {/each}
  </select>

  {#if modes.length > 0}
    {@const currentMode = modes.find(m => m.id === selectedMode)}
    {#if currentMode}
      <span class="description">{currentMode.description}</span>
    {/if}
  {/if}
</div>

<style>
  .mode-selector {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex: 1;
  }

  label {
    font-weight: 600;
    white-space: nowrap;
  }

  select {
    min-width: 200px;
    padding: 0.5rem 0.75rem;
  }

  .description {
    opacity: 0.7;
    font-size: 0.85rem;
    font-style: italic;
  }

  @media (max-width: 768px) {
    .mode-selector {
      flex-direction: column;
      align-items: flex-start;
    }

    .description {
      display: none;
    }
  }
</style>
