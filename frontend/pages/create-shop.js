import { useState } from 'react'
import { API_URL } from '../config'

export default function CreateShop() {
  const [name, setName] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const token = localStorage.getItem('token')
    try {
      await fetch(`${API_URL}/shops`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ name })
      })
      setName('')
    } catch (err) {
      console.error('Network error:', err)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Shop Name" />
      <button type="submit">Create Shop</button>
    </form>
  )
}
