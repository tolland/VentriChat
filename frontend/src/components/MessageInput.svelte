<script lang="ts">
  import { createEventDispatcher } from 'svelte'

  export let disabled = false

  const dispatch = createEventDispatcher<{ send: string }>()

  let messageText = ''

  function handleSubmit() {
    if (messageText.trim() && !disabled) {
      dispatch('send', messageText)
      messageText = ''
    }
  }

  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault()
      handleSubmit()
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <div class="input-container">
    <input
      type="text"
      bind:value={messageText}
      on:keydown={handleKeydown}
      placeholder={disabled ? 'Connecting...' : 'Type your message...'}
      {disabled}
    />
    <button type="submit" {disabled}>
      Send
    </button>
  </div>
</form>

<style>
  form {
    width: 100%;
  }

  .input-container {
    display: flex;
    gap: 0.75rem;
    width: 100%;
  }

  input {
    flex: 1;
    padding: 0.75rem 1rem;
    font-size: 1rem;
  }

  button {
    padding: 0.75rem 2rem;
    background: #646cff;
    color: white;
    border: 1px solid #646cff;
    font-weight: 600;
  }

  button:hover:not(:disabled) {
    background: #535bf2;
  }

  button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
</style>
