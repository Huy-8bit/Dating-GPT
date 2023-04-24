import { Heading, SimpleGrid, VStack } from "@chakra-ui/react";
import InterestBadges from './Profile-components/InterestBadges.jsx';
import ProfileInput from './Profile-components/ProfileInput.jsx';

const profileInformation = [
  {
    name: "Name",
    type: "text",
    required: true,
  },
  {
    name: "About me",
    type: "text",
  },
  {
    name: "Gender",
    type: "choice",
    choices: ['male', 'female', 'diverse'],
  },
  {
    name: "Looking for",
    type: "choice",
    choices: ["relationship", "dating", "something casual", "new friends", "not sure yet"],
  },
  {
    name: "Language",
    type: "choice",
    choices: ["English", "Spanish", "Mandarin", "Hindi", "Arabic", "Portuguese", "Bengali", "Japanese", "German"],
  },
  {
    name: "Zodiac sign",
    type: "choice",
    choices: ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
  },
  {
    name: "Education",
    type: "choice",
    choices: ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate Degree", "Vocational School", "Trade School", "Homeschool", "Other"],
  },
  {
    name: "Living in",
    type: "text",
  },
  {
    name: "Job",
    type: "text",
  },
  {
    name: "Drinking",
    type: "choice",
    choices: ["Yes, I drink alcohol", "No, I do not drink alcohol", "I drink occasionally", "I drink socially", "I prefer not to say"],
  },
  {
    name: "Smoking",
    type: "choice",
    choices: ["Non-smoker", "Occasional smoker", "Regular smoker"],
  },
  {
    name: "Children",
    type: "choice",
    choices: ["I have children", "Yes, I want children", "No, I don't want children", "Maybe, I'm not sure yet","Preferences open to discussion"],
  },
  {
    name: "Favourite Pet",
    type: "choice",
    choices: ["Cats", "Dogs", "Reptiles", "Fish", "Rabbits", "Small Mammals", "Birds", "Amphibians", "Insects"],
  },
  {
    name: "Favourite Song",
    type: "text",
  },
  {
    name: "Favourite Artist",
    type: "text",
  },
];
const interests = ['art', 'writing', 'photography', 'clubbing', 'videogames', 'watching movies', 'reading', 'singing', 'dancing', 'go out with friends', 'gardening', 'cooking', 'fitness', 'gym', 'soccer', 'feminism', 'theater', 'meditation', 'coffee'];

const Profile = ({heading, onChange}) => {
  return (
      <VStack mb={10}>
        <Heading as='h2' size='lg'>{heading}</Heading>
        <SimpleGrid columns={{sm: 2, md: 3, lg: 4}} spacing={2}>
          {profileInformation.map((info, index) => (
            <ProfileInput key={index} info={info} onChange={onChange} />
          ))}
        </SimpleGrid>
        <InterestBadges interests={interests} onChange={onChange} />
      </VStack>
  );
};

export default Profile;