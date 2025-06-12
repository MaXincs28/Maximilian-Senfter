import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Shop Demo</h1>
      <nav>
        <ul>
          <li><Link href="/signup">Sign Up</Link></li>
          <li><Link href="/login">Login</Link></li>
          <li><Link href="/register-shop">Register Shop</Link></li>
          <li><Link href="/manage-products">Manage Products</Link></li>
        </ul>
      </nav>
    </div>
  )
}
