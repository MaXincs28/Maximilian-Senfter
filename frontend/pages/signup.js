import { useState } from 'react'
import { API_URL } from '../config'

export default function Signup() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [shopName, setShopName] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      })
      if (res.ok) {
        const loginRes = await fetch(`${API_URL}/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        })
        const data = await loginRes.json()
        if (data.access_token && shopName) {
          await fetch(`${API_URL}/shops`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${data.access_token}`
            },
            body: JSON.stringify({ name: shopName })
          })
        }
        setUsername('')
        setPassword('')
        setShopName('')
      } else {
        console.error('Signup failed')
      }
    } catch (err) {
      console.error('Network error:', err)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <input value={shopName} onChange={(e) => setShopName(e.target.value)} placeholder="Shop Name (optional)" />
      <button type="submit">Sign Up</button>
    </form>
  )
}
