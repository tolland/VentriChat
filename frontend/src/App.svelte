<script lang="ts">
  import { onDestroy } from 'svelte'
  import ChatRoom from './components/ChatRoom.svelte'
  import type { DistortionMode } from './types'
  import { fetchDistortionModes } from './services/api'

  let username = ''
  let roomId = ''
  let joined = false
  let modes: DistortionMode[] = []
  let loading = true

  // Load available distortion modes
  fetchDistortionModes()
    .then(fetchedModes => {
      modes = fetchedModes
      loading = false
    })
    .catch(error => {
      console.error('Failed to load modes:', error)
      loading = false
    })

  function handleJoin() {
    if (username.trim() && roomId.trim()) {
      joined = true
    }
  }

  function handleLeave() {
    joined = false
    username = ''
    roomId = ''
  }
</script>

<main>
  <header>
    <h1>🎭 VentriChat</h1>
    <p class="tagline">Where AI distorts your every word</p>
  </header>

  {#if !joined}
    <div class="join-form">
      <h2>Join a Chat Room</h2>
      <p class="description">
        Messages you send will be transformed by AI before others see them.
        Choose a distortion mode and watch the chaos unfold!
      </p>

      <form on:submit|preventDefault={handleJoin}>
        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            type="text"
            bind:value={username}
            placeholder="Enter your username"
            required
          />
        </div>

        <div class="form-group">
          <label for="roomId">Room ID</label>
          <input
            id="roomId"
            type="text"
            bind:value={roomId}
            placeholder="Enter or create a room"
            required
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Loading...' : 'Join Room'}
        </button>
      </form>

      {#if modes.length > 0}
        <div class="modes-preview">
          <h3>Available Distortion Modes:</h3>
          <ul>
            {#each modes as mode}
              <li>
                <strong>{mode.name}</strong> - {mode.description}
              </li>
            {/each}
          </ul>
        </div>
      {/if}
    </div>
  {:else}
    <ChatRoom
      {username}
      {roomId}
      {modes}
      on:leave={handleLeave}
    />
  {/if}
</main>

<style>
  main {
    min-height: 100vh;
    padding: 2rem;
  }

  header {
    text-align: center;
    margin-bottom: 2rem;
  }

  h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(45deg, #646cff, #ff6b6b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .tagline {
    font-size: 1.1rem;
    opacity: 0.8;
    font-style: italic;
  }

  .join-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .join-form h2 {
    margin-bottom: 1rem;
  }

  .description {
    opacity: 0.8;
    margin-bottom: 2rem;
    line-height: 1.6;
  }

  .form-group {
    margin-bottom: 1.5rem;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  input {
    width: 100%;
  }

  button {
    width: 100%;
    padding: 0.8rem;
    font-size: 1.1rem;
  }

  .modes-preview {
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }

  .modes-preview h3 {
    margin-bottom: 1rem;
    font-size: 1.1rem;
  }

  .modes-preview ul {
    list-style: none;
    padding: 0;
  }

  .modes-preview li {
    padding: 0.5rem 0;
    opacity: 0.9;
    font-size: 0.95rem;
  }

  .modes-preview strong {
    color: #646cff;
  }
</style>
