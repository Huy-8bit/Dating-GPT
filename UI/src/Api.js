// app.js
import axios from 'axios';
export const getRoot = async () => {
  try {
    const response = await axios.post('https://0fd9d434-e233-4b18-8bc9-c1e8c94cd253.mock.pstmn.io');
    console.log("chekc respose:")
    console.log(response);
  } catch (error) {
    console.error(error);
  }
};

export const getchoice = async (profiles, sender, history) => {
  console.log({
    "profile1": profiles.profile1,
    "profile2": profiles.profile2,
    "sender": sender,
    "history": history
  });

  try {
    const { data } = await axios.post('https://0fd9d434-e233-4b18-8bc9-c1e8c94cd253.mock.pstmn.io', {
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
