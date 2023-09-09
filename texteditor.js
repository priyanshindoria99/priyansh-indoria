import React, { useState } from 'react';

const TextEditor = () => {
  const [text, setText] = useState('');
  const [editedText, setEditedText] = useState('');

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleUpperCase = () => {
    setEditedText(text.toUpperCase());
  };

  const handleLowerCase = () => {
    setEditedText(text.toLowerCase());
  };

  const handleBold = () => {
    setEditedText(`<strong>${text}</strong>`);
  };

  const handleItalic = () => {
    setEditedText(`<em>${text}</em>`);
  };

  const handleUnderline = () => {
    setEditedText(`<u>${text}</u>`);
  };

  return (
    <div>
      <textarea
        value={text}
        onChange={handleTextChange}
        placeholder="Enter your text here"
        rows={5}
        cols={40}
      />
      <div>
        <button onClick={handleUpperCase}>Uppercase</button>
        <button onClick={handleLowerCase}>Lowercase</button>
        <button onClick={handleBold}>Bold</button>
        <button onClick={handleItalic}>Italic</button>
        <button onClick={handleUnderline}>Underline</button>
      </div>
      <div>
        <div dangerouslySetInnerHTML={{ __html: editedText }} />
      </div>
    </div>
  );
};

export default TextEditor;
