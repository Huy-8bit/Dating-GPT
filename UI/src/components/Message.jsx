import { Text } from "@chakra-ui/react";
import Clickable from "../components/Clickable";

const Message = ({children, isUser, onClick}) => {
  return (
    <Clickable onClick={onClick} alignSelf={isUser ? 'flex-start' : 'flex-end'} _disabled={{ pointerEvents: "none" }} isDisabled={onClick ? false : true} ml='10px' mr='10px'>
      <Text align={isUser ? 'left' : 'right'} maxW='400px' borderRadius='lg' p='10px' backgroundColor={isUser ? 'red.100' : 'blue.100'}>{children}</Text>
    </Clickable>
  );
};

export default Message;