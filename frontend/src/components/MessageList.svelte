<script lang="ts">
  import { afterUpdate } from 'svelte'
  import type { Message } from '../types'

  export let messages: Message[]
  export let showOriginal: boolean
  export let username: string

  let scrollContainer: HTMLDivElement

  afterUpdate(() => {
    if (scrollContainer) {
      scrollContainer.scrollTop = scrollContainer.scrollHeight
    }
  })

  function formatTime(timestamp: string): string {
    const date = new Date(timestamp)
    return date.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit'
    })
  }
</script>

<div class="message-list" bind:this={scrollContainer}>
  {#if messages.length === 0}
    <div class="empty-state">
      <p>No messages yet. Start the conversation!</p>
      <p class="hint">Your messages will be distorted by AI before others see them.</p>
    </div>
  {:else}
    {#each messages as message}
      {#if message.type === 'message'}
        <div class="message" class:own={message.username === username}>
          <div class="message-header">
            <span class="username">{message.username}</span>
            <span class="time">{formatTime(message.timestamp)}</span>
            {#if message.mode}
              <span class="mode-badge">{message.mode}</span>
            {/if}
          </div>

          <div class="message-content">
            <div class="distorted-text">
              {message.distorted || message.original}
            </div>

            {#if showOriginal && message.original && message.distorted}
              <div class="original-text">
                <span class="label">Original:</span>
                {message.original}
              </div>
            {/if}
          </div>
        </div>
      {:else if message.type === 'user_joined'}
        <div class="system-message">
          <span>{message.username} joined the room</span>
        </div>
      {:else if message.type === 'user_left'}
        <div class="system-message">
          <span>{message.username} left the room</span>
        </div>
      {/if}
    {/each}
  {/if}
</div>

<style>
  .message-list {
    height: 100%;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    opacity: 0.6;
    text-align: center;
  }

  .empty-state p {
    margin: 0.5rem 0;
  }

  .hint {
    font-size: 0.9rem;
    font-style: italic;
  }

  .message {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    border-left: 3px solid #646cff;
  }

  .message.own {
    border-left-color: #4ade80;
    background: rgba(74, 222, 128, 0.1);
  }

  .message-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.9rem;
  }

  .username {
    font-weight: 600;
    color: #646cff;
  }

  .message.own .username {
    color: #4ade80;
  }

  .time {
    opacity: 0.6;
    font-size: 0.85rem;
  }

  .mode-badge {
    padding: 0.2rem 0.5rem;
    background: rgba(100, 108, 255, 0.2);
    border-radius: 4px;
    font-size: 0.75rem;
    text-transform: lowercase;
  }

  .message-content {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .distorted-text {
    font-size: 1rem;
    line-height: 1.5;
  }

  .original-text {
    padding: 0.75rem;
    background: rgba(0, 0, 0, 0.3);
    border-radius: 6px;
    font-size: 0.9rem;
    opacity: 0.8;
    border-left: 2px solid rgba(255, 255, 255, 0.2);
  }

  .label {
    font-weight: 600;
    opacity: 0.7;
    font-size: 0.8rem;
    text-transform: uppercase;
    display: block;
    margin-bottom: 0.25rem;
  }

  .system-message {
    text-align: center;
    padding: 0.5rem;
    opacity: 0.6;
    font-size: 0.9rem;
    font-style: italic;
  }
</style>
