import { useState } from 'react'
import './App.css'
import Routes from './routes/Routes'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Routes />
    </>
  )
}

export default App
