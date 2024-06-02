/**
* Copyright (c) AWildDevAppears
*/

import { Box } from "@mui/system"
import React, { PropsWithChildren } from "react"

interface ISVGPaperProps extends PropsWithChildren {

}

export const SVGPaper: React.FC<ISVGPaperProps> = ({ children }) => {
    return <Box sx={{ height: "100vh", position: "relative", }}>
        <Box component="svg" width="100%" height="100%" sx={{ zIndex: "-1", userSelect: "none", pointerEvents: "none"}}>
            <rect
                x="1rem"
                y="1rem"
                rx="1rem"
                height="calc(100% - 2rem)"
                width="calc(100% - 2rem)"
                strokeWidth="0.25rem"
                stroke="red"
                fill="none"
            >
            </rect>
        </Box>
        { children }
    </Box>;
}
