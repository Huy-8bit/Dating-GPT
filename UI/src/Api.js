// app.js
import axios from 'axios';

export const getRoot = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/getchoice');
    console.log(response);
  } catch (error) {
    console.error(error);
  }
};

export const getPickUpLine = async (profiles, sender, history) => {
  console.log({
    "profile1": profiles.profile1,
    "profile2": profiles.profile2,
    "sender": sender,
    "history": history
  });

  try {
    const { data } = await axios.post('http://127.0.0.1:5000/getchoice', {
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

    console.log(data);
    return data;
  } catch (error) {
    console.error(error);
  }
};
