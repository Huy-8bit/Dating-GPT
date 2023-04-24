import axios from 'axios';

export const getRoot = async () => {
  await axios.get('https://dating-better.onrender.com/');
};

export const getPickUpLine = async (profiles, sender, history) => {
  console.log({
    "profile1": profiles.profile1,
    "profile2": profiles.profile2,
    "sender": sender,
    "history": history
  });
  

  const {data} = await axios.post('https://dating-better.onrender.com/GetPickupLine', {
    "profile1": profiles.profile1,
    "profile2": profiles.profile2,
    "sender": sender,
    "msg_attr": [
        "creative",
        "witty",
        "teasing",
        "funny",
    ],
    "history": history
  });

  return data;
};