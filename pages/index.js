import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [agentStatus, setAgentStatus] = useState('READY');
  const [inputMessage, setInputMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [bootSequence, setBootSequence] = useState(true);
  const [bootMessages, setBootMessages] = useState([]);

  // Terminal boot sequence
  useEffect(() => {
    if (bootSequence) {
      const sequence = [
        'Initializing QUANTUM NEXUS LABS system...',
        'Loading ARIA Protocol v1.0.0...',
        'Establishing quantum backend connection...',
        'Neural patterns synchronized...',
        'System ready for input.'
      ];

      sequence.forEach((msg, index) => {
        setTimeout(() => {
          setBootMessages(prev => [...prev, msg]);
          if (index === sequence.length - 1) {
            setBootSequence(false);
          }
        }, index * 1000);
      });
    }
  }, []);

  const handleSendMessage = async () => {
    if (!inputMessage.trim()) return;
    
    setMessages(prev => [...prev, { 
      type: 'user', 
      content: inputMessage,
      timestamp: new Date().toLocaleTimeString()
    }]);
    
    setAgentStatus('PROCESSING');
    setTimeout(() => {
      setMessages(prev => [...prev, { 
        type: 'system', 
        content: `Processing request: ${inputMessage}`,
        timestamp: new Date().toLocaleTimeString()
      }]);
      setAgentStatus('READY');
    }, 1000);
    
    setInputMessage('');
  };

  return (
    <div className="min-h-screen bg-black text-white font-mono p-4">
      {/* Terminal Window */}
      <div className="border border-gray-600 rounded-lg max-w-4xl mx-auto">
        {/* Terminal Header */}
        <div className="border-b border-gray-600 p-2 flex justify-between items-center">
          <div className="flex space-x-2">
            <div className="w-3 h-3 rounded-full bg-red-500"></div>
            <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
            <div className="w-3 h-3 rounded-full bg-green-500"></div>
          </div>
          <div className="text-gray-400 text-sm">QUANTUM NEXUS LABS - TERMINAL</div>
          <div className="w-16"></div>
        </div>

        {/* Terminal Body */}
        <div className="p-4 h-[80vh] flex flex-col">
          {/* Status Bar */}
          <div className="mb-4 text-sm">
            <span className="text-gray-400">STATUS: </span>
            <span className="text-green-400">{agentStatus}</span>
            <span className="text-gray-400 ml-4">NEURAL: </span>
            <span className="text-blue-400">ACTIVE</span>
            <span className="text-gray-400 ml-4">QUANTUM: </span>
            <span className="text-purple-400">ONLINE</span>
          </div>

          {/* Boot Sequence */}
          {bootSequence && (
            <div className="space-y-2 mb-4">
              {bootMessages.map((msg, idx) => (
                <div key={idx} className="text-green-400">
                  > {msg}
                </div>
              ))}
            </div>
          )}

          {/* Messages */}
          <div className="flex-1 overflow-y-auto space-y-2 mb-4">
            {messages.map((msg, idx) => (
              <div key={idx} className="text-sm">
                <span className="text-gray-500">[{msg.timestamp}] </span>
                <span className={msg.type === 'user' ? 'text-white' : 'text-green-400'}>
                  {msg.type === 'user' ? '$ ' : '> '}{msg.content}
                </span>
              </div>
            ))}
          </div>

          {/* Input Area */}
          <div className="flex items-center text-sm">
            <span className="text-green-400 mr-2">$</span>
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              className="flex-1 bg-transparent focus:outline-none"
              placeholder="Enter command..."
              spellCheck="false"
            />
          </div>
        </div>
      </div>
    </div>
  );
}
