import { useState } from 'react'

function App() {
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([])

  const handleSend = async () => {
    if (!message.trim()) return

    const userMsg = { role: 'user', content: message }
    setMessages((prev) => [...prev, userMsg])
    setMessage('')

    // TODO: Call POST /api/v1/chat
    // Placeholder response
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: 'Thank you for your enquiry. Our team will assist you shortly. (Scaffold placeholder)',
        },
      ])
    }, 800)
  }

  return (
    <div style={{ maxWidth: 600, margin: '40px auto', fontFamily: 'system-ui, sans-serif' }}>
      <h1>Real Estate Lead Bot</h1>
      <p style={{ color: '#666' }}>Customer chat interface (scaffolded)</p>

      <div
        style={{
          border: '1px solid #ddd',
          borderRadius: 8,
          height: 400,
          overflowY: 'auto',
          padding: 16,
          marginBottom: 16,
          background: '#fafafa',
        }}
      >
        {messages.length === 0 && (
          <p style={{ color: '#999' }}>Start a conversation about a property...</p>
        )}
        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              marginBottom: 12,
              textAlign: m.role === 'user' ? 'right' : 'left',
            }}
          >
            <span
              style={{
                display: 'inline-block',
                padding: '8px 12px',
                borderRadius: 12,
                background: m.role === 'user' ? '#2563eb' : '#e5e7eb',
                color: m.role === 'user' ? 'white' : '#111',
                maxWidth: '80%',
              }}
            >
              {m.content}
            </span>
          </div>
        ))}
      </div>

      <div style={{ display: 'flex', gap: 8 }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type your message..."
          style={{ flex: 1, padding: '10px 14px', borderRadius: 8, border: '1px solid #ccc' }}
        />
        <button
          onClick={handleSend}
          style={{
            padding: '10px 20px',
            borderRadius: 8,
            border: 'none',
            background: '#2563eb',
            color: 'white',
            cursor: 'pointer',
          }}
        >
          Send
        </button>
      </div>
    </div>
  )
}

export default App
