import { useState } from 'react';
import { HStack, Input, Button } from '@chakra-ui/react';

function MessageInput({onSubmit}) {
  const [inputValue, setInputValue] = useState('');

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
        handleSubmit();
    }
  };

  const handleSubmit = () => {
    onSubmit(inputValue);
    setInputValue('');
  };

  return (
    <HStack m='10px'>
      <Input
        placeholder='Your message'
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={handleKeyDown}
      />
      <Button onClick={handleSubmit}>Send</Button>
    </HStack>
  );
}

export default MessageInput;