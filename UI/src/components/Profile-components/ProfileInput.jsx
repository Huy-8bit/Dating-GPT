import { FormControl, Select, Input, Box } from "@chakra-ui/react";


function ProfileInput({info, onChange}) {
  return (
    <FormControl key={info.name} id={info.name} isRequired={info.required}>
      <Box ml='10px' mr='10px'>
        {info.type === "choice" ? (
          <Select name={info.name} placeholder={info.name} onChange={onChange}>
            {info.choices.map((choice) => (
              <option key={choice} value={choice}>
                {choice}
              </option>
            ))}
          </Select>
        ) : (
          <Input name={info.name} placeholder={info.name} onChange={onChange} />
        )}
      </Box>
    </FormControl>
  );
}
export default ProfileInput;