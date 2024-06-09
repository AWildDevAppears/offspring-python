/**
* Copyright (c) AWildDevAppears
*/

import { Container } from "@mui/system"
import { SVGCard } from "../../assets/svg/SVGCard"

interface IViewDebugProps {

}

export const ViewDebug: React.FC<IViewDebugProps> = () => {
    return <Container>
        <h1>Debug</h1>
        <SVGCard />
    </Container>
}
