import { useState, useEffect } from 'react';
import { Heading, Highlight, chakra, shouldForwardProp } from "@chakra-ui/react";
import Header from "../components/Header";
import Conversation from "../components/Conversation";
import { getPickUpLine, getRoot } from '../Api.js';
import ProfileHelper from "../helper/ProfileHelper";
import { motion, isValidMotionProp } from "framer-motion"

const AnimationBox = chakra(motion.div, {
  shouldForwardProp: (prop) => isValidMotionProp(prop) || shouldForwardProp(prop),
});

const Chat = () => {
  const [profiles, setProfiles] = useState(null);
  const [history, setHistory] = useState([]);
  const [choices, setChoices] = useState([]);
  const [hideConversation, setHideConversation] = useState(true);
  const [fetchError, setFetchError] = useState(null);
  const [stopAiConversation, setStopAiConversation] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);

  // Initial call to backend to start it up
  useEffect(() => {
    getRoot();
  }, []);

  useEffect(() => {
    if (!hideConversation) {
      scrollToBottom();
    }
  }, [hideConversation, scrollToBottom]);

  useEffect(() => {
    if (history.length >= 4) {
      setStopAiConversation(true);
      return;
    }
    
    if (ProfileHelper.areFilledProfiles(profiles)) {
      console.log("Fetching choices");
      setHideConversation(false);
      fetchChoices().then((choices) => {
        setChoices(choices);
      });
    }
  }, [profiles, history]);

  const handleConversationStart = (profiles) => {
    if (!ProfileHelper.areFilledProfiles(profiles)) {
      setErrorMessage('Please add at least one information for each profile');
    } else {
      setErrorMessage(null);
      setHistory([]);
      setChoices([])
      setProfiles(profiles);
    }
  };

  function handleChoiceSelection(choice) {
    setHistory([...history, {sender: ProfileHelper.getNextProfileIdByHistory(history), msg: choice}]);
    setChoices([]);
  }

  function scrollToBottom() {
    window.scrollTo({
      top: window.scrollY + window.innerHeight,
      behavior: 'smooth',
    });
  }

  async function fetchChoices() {
    const profileId = ProfileHelper.getNextProfileIdByHistory(history);
    try {
      const {choices} = await getPickUpLine(profiles, profileId, history);
      setFetchError(null);
      return choices ?? []
    } catch (error) {
      console.error(`${error}`);
      setFetchError(error);
      return [];
    }
  }

  return (
    <>
      <AnimationBox as={motion.div} transition={{ease: 'easeOut', duration: 0.5}} initial={{ y: '-20', opacity: 0 }} animate={{ y: 0, opacity: 1 }}>
        <Heading as='h1' size='2xl' mb={10}>
          <Highlight
            query={'AI'}
            styles={{ px: '2', py: '1', rounded: 'full', bg: 'red.100' }}
          >
            DAITING.BETTER
          </Highlight>
        </Heading>
      </AnimationBox>
      <AnimationBox as={motion.div} transition={{ease: 'easeOut', duration: 0.5, delay: 0.3}} initial={{ y: -20, opacity: 0 }} animate={{ y: 0, opacity: 1 }}>
        <Header onConversationStart={handleConversationStart} errorMessage={errorMessage} />
      </AnimationBox>
      <AnimationBox as={motion.div} transition={{ease: 'easeOut', duration: 0.5, delay: 0.6}} initial={{ y: -20, opacity: 0 }} animate={{ y: 0, opacity: 1 }}>
        <Conversation choices={choices} history={history} onChoiceSelection={handleChoiceSelection} hidden={hideConversation} fetchError={fetchError} stopAiConversation={stopAiConversation} />
      </AnimationBox>
    </>
  );
};

export default Chat;