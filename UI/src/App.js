import './App.css';
import Chat from './pages/Chat';
import { ChakraProvider, Container } from '@chakra-ui/react'

function App() {
  return (
    <ChakraProvider>
      <Container maxW='6xl' p='0px' mt='45px' mb='45px'>
        <Chat />
      </Container>
    </ChakraProvider>
  );
}

export default App;
