import { useState } from 'react'

export default function ManageProducts() {
  const [shopId, setShopId] = useState('')
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [price, setPrice] = useState('')
  const [image, setImage] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    const formData = new FormData()
    formData.append('name', name)
    formData.append('description', description)
    formData.append('price', price)
    if (image) {
      formData.append('image', image)
    }
    await fetch(`http://localhost:8000/shops/${shopId}/products`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
      },
      body: formData
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={shopId} onChange={(e) => setShopId(e.target.value)} placeholder="Shop ID" />
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <input value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" />
      <input value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" />
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <button type="submit">Add Product</button>
    </form>
  )
}
