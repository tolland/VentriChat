# VentriChat Frontend

Svelte + TypeScript frontend with real-time WebSocket chat.

## Prerequisites

- [pnpm](https://pnpm.io/) - Fast, disk space efficient package manager

## Setup

```bash
pnpm install
```

## Development

```bash
pnpm dev
```

Open `http://localhost:5173` in your browser.

## Build

```bash
pnpm build
```

The built files will be in the `dist/` directory.

## Preview Production Build

```bash
pnpm preview
```

## Type Checking

```bash
pnpm check
```

## Project Structure

- `src/App.svelte` - Main application component
- `src/components/` - Reusable Svelte components
- `src/services/` - API and WebSocket client services
- `src/types.ts` - TypeScript type definitions
- `src/app.css` - Global styles
