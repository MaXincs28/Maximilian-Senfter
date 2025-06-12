import { useState } from 'react'

export default function RegisterShop() {
  const [name, setName] = useState('')
  const [address, setAddress] = useState('')
  const [lat, setLat] = useState('')
  const [lng, setLng] = useState('')
  const [ownerId, setOwnerId] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    await fetch('http://localhost:8000/shops', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
      },
      body: JSON.stringify({
        name,
        address,
        ownerId: parseInt(ownerId, 10),
        coords: { lat: parseFloat(lat), lng: parseFloat(lng) }
      })
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Shop name" />
      <input value={address} onChange={(e) => setAddress(e.target.value)} placeholder="Address" />
      <input value={lat} onChange={(e) => setLat(e.target.value)} placeholder="Latitude" />
      <input value={lng} onChange={(e) => setLng(e.target.value)} placeholder="Longitude" />
      <input value={ownerId} onChange={(e) => setOwnerId(e.target.value)} placeholder="Owner ID" />
      <button type="submit">Create Shop</button>
    </form>
  )
}
