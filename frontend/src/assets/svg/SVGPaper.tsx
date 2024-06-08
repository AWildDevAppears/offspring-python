/**
* Copyright (c) AWildDevAppears
*/

import { Box } from "@mui/system"
import React, { PropsWithChildren } from "react"
import paper from "./SVGPaper.svg"
import { SVGBackground } from "./SVGBackground"

interface ISVGPaperProps extends PropsWithChildren {

}

export const SVGPaper: React.FC<ISVGPaperProps> = ({ children }) => {
    return <SVGBackground path={paper} sx={{  padding: "2rem", }}>
        { children }
    </SVGBackground>;
}
