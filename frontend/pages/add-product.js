import { useState } from 'react'
import { API_URL } from '../config'

export default function AddProduct() {
  const [name, setName] = useState('')
  const [price, setPrice] = useState('')
  const [shopId, setShopId] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const token = localStorage.getItem('token')
    try {
      await fetch(`${API_URL}/products`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ name, price: parseFloat(price), shop_id: parseInt(shopId) })
      })
      setName('')
      setPrice('')
      setShopId('')
    } catch (err) {
      console.error('Network error:', err)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Product Name" />
      <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" />
      <input type="number" value={shopId} onChange={(e) => setShopId(e.target.value)} placeholder="Shop ID" />
      <button type="submit">Add Product</button>
    </form>
  )
}
