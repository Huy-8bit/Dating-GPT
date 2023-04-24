
import { chakra } from "@chakra-ui/system";
import { useClickable } from "@chakra-ui/clickable";

const Clickable = (props) => {
    const clickable = useClickable(props);
    return <chakra.button display="inline-flex" {...clickable} disabled={props.isDisabled} />
}

export default Clickable;