/**
* Copyright (c) AWildDevAppears
*/

import { Box, SxProps, Theme } from "@mui/system";
import React, { PropsWithChildren } from "react"

interface ISVGBackgroundProps extends PropsWithChildren {
    path: string;
    sx?: SxProps<Theme>;
}

export const SVGBackground = React.FC<ISVGBackgroundProps> = ({ path, sx, children }) => {
    return <Box sx={{ height: "100%", width: "100%", position: "relative",}}>
        <Box component="div" height="100%" sx={
            {
                maxWidth: "100%",
                backgroundImage: `url("${path}")`,
                backgroundSize: "cover",
                backgroundRepeat: "no-repeat",
                ...sx,
            }
        }>
            { children }
        </Box>
    </Box>;
}
