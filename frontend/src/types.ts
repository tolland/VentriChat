/**
 * Type definitions for VentriChat
 */

export interface Message {
  type: 'message' | 'user_joined' | 'user_left'
  username?: string
  original?: string
  distorted?: string
  mode?: string
  timestamp: string
  users_count?: number
}

export interface DistortionMode {
  id: string
  name: string
  description: string
}

export interface ChatState {
  connected: boolean
  username: string
  roomId: string
  messages: Message[]
  users: string[]
  currentMode: string
  showOriginal: boolean
}
