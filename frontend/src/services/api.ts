/**
 * API Client for VentriChat REST endpoints
 */

import type { DistortionMode } from '../types'

const API_BASE = '/api'

export async function fetchDistortionModes(): Promise<DistortionMode[]> {
  const response = await fetch(`${API_BASE}/modes`)
  const data = await response.json()
  return data.modes
}

export async function fetchRoomInfo(roomId: string) {
  const response = await fetch(`${API_BASE}/rooms/${roomId}`)
  return await response.json()
}

export async function fetchActiveRooms() {
  const response = await fetch(`${API_BASE}/rooms`)
  const data = await response.json()
  return data.rooms
}
