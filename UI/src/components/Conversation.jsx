import { Stack, Heading, Flex, Spinner, Center, Input } from "@chakra-ui/react";
import Message from "../components/Message";
import MessageChoices from "../components/MessageChoices";
import ErrorAlert from "../components/ErrorAlert";
import MessageInput from "../components/MessageInput";

function Conversation({choices, history, onChoiceSelection, hidden, fetchError, stopAiConversation}) {
  const isUser = history.length % 2 === 0;

  return (
    <>
    { !hidden &&
      <Stack spacing={2} w='100%'>
        <Heading as='h2' size='lg'>Conversation</Heading>
        <Flex flexDirection='column' gap={2} w='100%'>
          {history.map((historyItem, index) => (
            <Message key={index} isUser={historyItem.sender === 'P1'}>
              {historyItem.msg}
            </Message>
          ))}
          { choices.length > 0 ? <MessageChoices
            choices={choices}
            onSelect={onChoiceSelection}
            isUser={isUser}
          /> : (fetchError ?
            <ErrorAlert message='Error when trying to fetch messages' /> :
            (stopAiConversation ?
              <MessageInput onSubmit={onChoiceSelection}/>
              : <Center m='30px'><Spinner/></Center>)
            ) }
        </Flex>
      </Stack>
    }
    </>
  );
}

export default Conversation;
