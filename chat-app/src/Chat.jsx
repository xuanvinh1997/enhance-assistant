import React, { useState, useRef } from 'react';
import axios from 'axios';

const url = process.env.CHAT_URL || 'http://localhost:8000';

const sendMessage = async (messages) => {
  return axios.post(`${url}/api/chat`, {
    messages
  });
}

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const inputRef = useRef(null);

  const handleSendMessage = () => {
    const messageText = inputRef.current.value;
    if (messageText.trim() !== '') {
      setMessages([...messages, { content: messageText, role: 'user' }]);
      inputRef.current.value = '';
    }
  };

  return (
    <div className="h-[80vh] flex flex-col w-full">
      <div className="flex flex-col p-4 overflow-y-auto bg-gray-100 rounded-t-lg h-full ">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`chat ${
              message.role === 'user' ? 'chat-end' : 'chat-start'
            }`}
          >
            <div
              className={`chat-bubble ${
                message.role === 'user'  ? 'chat-bubble-primary' : ''
              }`}
            >
              {message.content}
            </div>
          </div>
        ))}
      </div>
      <div className="flex items-center p-4 bg-white rounded-b-lg gap-4">
        <input
          ref={inputRef}
          type="text"
          placeholder="Type your message..."
          className="input input-bordered w-full"
        />
        <button
          onClick={handleSendMessage}
          className="btn btn-primary"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;