# VentriChat Frontend

Svelte + TypeScript frontend with real-time WebSocket chat.

## Setup

```bash
npm install
```

## Development

```bash
npm run dev
```

Open `http://localhost:5173` in your browser.

## Build

```bash
npm run build
```

The built files will be in the `dist/` directory.

## Preview Production Build

```bash
npm run preview
```

## Type Checking

```bash
npm run check
```

## Project Structure

- `src/App.svelte` - Main application component
- `src/components/` - Reusable Svelte components
- `src/services/` - API and WebSocket client services
- `src/types.ts` - TypeScript type definitions
- `src/app.css` - Global styles
