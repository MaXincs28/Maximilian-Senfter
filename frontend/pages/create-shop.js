import { useState } from 'react'

export default function CreateShop() {
  const [name, setName] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const token = localStorage.getItem('token')
    await fetch('http://localhost:8000/shops', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ name })
    })
    setName('')
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Shop Name" />
      <button type="submit">Create Shop</button>
    </form>
  )
}
