import '../styles.css'

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <header className="header">Locus</header>
      <main>
        <Component {...pageProps} />
      </main>
    </>
  )
}
