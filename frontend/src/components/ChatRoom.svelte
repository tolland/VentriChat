<script lang="ts">
  import { onMount, onDestroy, createEventDispatcher } from 'svelte'
  import { WebSocketClient } from '../services/websocket'
  import type { Message, DistortionMode } from '../types'
  import MessageList from './MessageList.svelte'
  import MessageInput from './MessageInput.svelte'
  import ModeSelector from './ModeSelector.svelte'

  export let username: string
  export let roomId: string
  export let modes: DistortionMode[]

  const dispatch = createEventDispatcher()

  let ws: WebSocketClient | null = null
  let messages: Message[] = []
  let connected = false
  let currentMode = 'chaotic'
  let showOriginal = true

  onMount(async () => {
    const wsUrl = window.location.protocol === 'https:'
      ? `wss://${window.location.host}`
      : `ws://${window.location.host}`

    ws = new WebSocketClient(wsUrl, roomId, username)

    ws.onMessage((message: Message) => {
      messages = [...messages, message]
    })

    try {
      await ws.connect()
      connected = true
    } catch (error) {
      console.error('Failed to connect:', error)
    }
  })

  onDestroy(() => {
    if (ws) {
      ws.disconnect()
    }
  })

  function handleSendMessage(event: CustomEvent<string>) {
    const text = event.detail
    if (ws && text.trim()) {
      ws.sendMessage(text, currentMode)
    }
  }

  function handleModeChange(event: CustomEvent<string>) {
    currentMode = event.detail
  }

  function handleLeave() {
    if (ws) {
      ws.disconnect()
    }
    dispatch('leave')
  }
</script>

<div class="chat-room">
  <div class="chat-header">
    <div class="room-info">
      <h2>Room: {roomId}</h2>
      <p>Logged in as <strong>{username}</strong></p>
      <span class="status" class:connected>
        {connected ? '● Connected' : '○ Disconnected'}
      </span>
    </div>
    <button class="leave-btn" on:click={handleLeave}>Leave Room</button>
  </div>

  <div class="chat-controls">
    <ModeSelector
      {modes}
      selectedMode={currentMode}
      on:change={handleModeChange}
    />

    <label class="toggle">
      <input type="checkbox" bind:checked={showOriginal} />
      <span>Show original messages</span>
    </label>
  </div>

  <div class="chat-content">
    <MessageList {messages} {showOriginal} {username} />
  </div>

  <div class="chat-input">
    <MessageInput on:send={handleSendMessage} disabled={!connected} />
  </div>
</div>

<style>
  .chat-room {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 4rem);
    max-width: 1200px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    overflow: hidden;
  }

  .chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    background: rgba(0, 0, 0, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .room-info h2 {
    margin: 0 0 0.25rem 0;
    font-size: 1.5rem;
  }

  .room-info p {
    margin: 0;
    opacity: 0.8;
    font-size: 0.9rem;
  }

  .status {
    display: inline-block;
    margin-left: 1rem;
    opacity: 0.6;
    font-size: 0.85rem;
  }

  .status.connected {
    opacity: 1;
    color: #4ade80;
  }

  .leave-btn {
    background: rgba(239, 68, 68, 0.2);
    border: 1px solid rgba(239, 68, 68, 0.5);
    color: #fca5a5;
  }

  .leave-btn:hover {
    background: rgba(239, 68, 68, 0.3);
    border-color: #ef4444;
  }

  .chat-controls {
    display: flex;
    gap: 2rem;
    align-items: center;
    padding: 1rem 1.5rem;
    background: rgba(0, 0, 0, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .toggle {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
    user-select: none;
  }

  .toggle input {
    cursor: pointer;
    width: auto;
  }

  .chat-content {
    flex: 1;
    overflow-y: auto;
    padding: 1.5rem;
  }

  .chat-input {
    padding: 1rem 1.5rem;
    background: rgba(0, 0, 0, 0.2);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }
</style>
