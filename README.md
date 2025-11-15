# 🎭 VentriChat

**An AI-powered chat application that distorts your messages before others see them.**

VentriChat explores the fascinating concept of miscommunication through AI. When you send a message, it gets rewritten, misinterpreted, sanitized, exaggerated, or distorted by AI before appearing in the chatroom. It's a commentary on how automated systems reshape human communication, context changes perception, and how we behave differently when observed.

## 🌟 Core Concept

1. **Users type messages normally** - Just like any chat app
2. **Backend forwards to AI** - Messages are sent to an AI model
3. **AI transforms the message** - Based on the selected "speaker mode"
4. **Only AI version is broadcast** - The distorted text appears in chat
5. **Optional original view** - Users can toggle to see both versions

## 🎨 Features

- **Real-time multi-user chat** using WebSockets
- **8 AI distortion modes**:
  - 🌈 **Wholesome Overload** - Overly positive and saccharine
  - 📋 **Corporate Bureaucrat** - Formal memos and policy speak
  - 🎲 **Chaotic Neutral** - Random misinterpretations
  - 🖤 **Edgy Teenager** - Angsty and dramatic
  - 💼 **HR Department** - Sanitized corporate buzzwords
  - 👁️ **Paranoid Conspiracy** - Everything seems suspicious
  - 🏴‍☠️ **Pirate Translator** - Arr, matey!
  - 🎭 **Shakespearean** - Elizabethan English
- **Original vs Distorted view** - Toggle to see what was actually typed
- **Mock AI mode** - Runs completely self-contained without external APIs
- **Room-based chat** - Multiple rooms, each with their own conversations

## 🏗️ Tech Stack

- **Frontend**: Svelte + TypeScript + Vite
- **Backend**: Python FastAPI
- **Transport**: WebSockets for real-time messaging
- **AI**: Mock Ollama-compatible API (easily swappable with real models)

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- npm or yarn

### Installation

#### Modern Setup (Recommended - using uv and hatch)

1. **Clone the repository**
```bash
git clone <repository-url>
cd VentriChat
```

2. **Install uv** (if not already installed)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **Set up the backend**
```bash
cd backend
uv sync
cp .env.example .env
```

4. **Set up the frontend**
```bash
cd ../frontend
npm install
```

#### Traditional Setup (alternative)

1. **Clone and set up backend**
```bash
git clone <repository-url>
cd VentriChat/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

2. **Set up frontend**
```bash
cd ../frontend
npm install
```

### Running the Application

#### With Modern Tools (Recommended)

Terminal 1 - Backend:
```bash
cd backend
hatch run dev
```

Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

#### Traditional Method

Terminal 1 - Backend:
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py
```

Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

#### Quick Start Script

```bash
chmod +x start.sh
./start.sh
```

Then open your browser to `http://localhost:5173`

## 🎮 Usage

1. **Enter a username** and **room ID** on the landing page
2. **Select a distortion mode** from the dropdown
3. **Start chatting!** Your messages will be transformed by AI
4. **Toggle "Show original messages"** to see the difference
5. **Watch the chaos** as AI reshapes conversation

## 🔧 Configuration

### Backend (.env)

```env
HOST=0.0.0.0
PORT=8000
OLLAMA_BASE_URL=http://localhost:11434
USE_MOCK_AI=true  # Set to false to use real Ollama
```

### Development Mode

By default, VentriChat runs with **mock AI responses** (`USE_MOCK_AI=true`). This means:
- No external API calls
- Instant responses with templated transformations
- Completely self-contained for development

### Production Mode (Real AI)

To use actual AI models:

1. Install and run [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull llama2`
3. Set `USE_MOCK_AI=false` in backend/.env
4. Restart the backend

## 📁 Project Structure

```
VentriChat/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── routes/         # API endpoints
│   │   ├── ai_service.py   # AI distortion logic
│   │   ├── websocket_manager.py  # WebSocket handling
│   │   └── distortion_modes.py   # Mode configurations
│   ├── main.py             # FastAPI application
│   └── requirements.txt
├── frontend/               # Svelte + TypeScript frontend
│   ├── src/
│   │   ├── components/    # Svelte components
│   │   ├── services/      # API and WebSocket clients
│   │   ├── types.ts       # TypeScript definitions
│   │   └── App.svelte     # Main app component
│   ├── package.json
│   └── vite.config.ts
└── README.md
```

## 🎯 Why VentriChat?

This project is inspired by the idea that:

- **People behave differently when observed** - The AI is always watching
- **Context changes everything** - Without full conversation history, messages seem bizarre
- **Automated systems reshape intent** - Like how autocorrect or translation can fail hilariously
- **Unreliable narrators** - What if the communication layer itself can't be trusted?

It's similar to that old Outlook plugin that made the "Send" button run away if your email was too aggressive - but this is the chaotic AI version.

## 🛠️ Development

### Adding New Distortion Modes

Edit `backend/app/distortion_modes.py`:

```python
DISTORTION_MODES = {
    "your_mode": {
        "name": "Your Mode Name",
        "description": "What this mode does",
        "system_prompt": "Instructions for AI: {message}"
    }
}
```

Then add the transformation logic in `backend/app/ai_service.py`.

### API Endpoints

- `GET /` - Health check
- `GET /api/modes` - List available distortion modes
- `GET /api/rooms` - List active chat rooms
- `GET /api/rooms/{room_id}` - Get room info
- `WS /ws/{room_id}/{username}` - WebSocket connection

## 🤝 Contributing

This is an experimental/art project exploring AI-mediated communication. Feel free to:

- Add new distortion modes
- Improve the UI/UX
- Add features like message history, user avatars, etc.
- Experiment with different AI models
- Create plugins or extensions

## 📜 License

MIT License - Feel free to use, modify, and distribute.

## 🎨 Inspiration

- The unreliable narrator in literature
- Broken telephone / Chinese whispers
- "This email would have been better left unsent" plugins
- The gap between intent and interpretation
- How social media algorithms reshape discourse

---

**Built with chaos, powered by AI, inspired by miscommunication.**
