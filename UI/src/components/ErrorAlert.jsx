import { Alert, AlertIcon, AlertTitle, AlertDescription, Center } from '@chakra-ui/react'

const ErrorAlert = ({message, omitTitle = false}) => {
  return (
    <Center>
    <Alert status='error' borderRadius={7}>
        <AlertIcon />
        { !omitTitle &&
          <AlertTitle>Error!</AlertTitle>
        }
        <AlertDescription>{message}</AlertDescription>
    </Alert></Center>
  );
};

export default ErrorAlert;