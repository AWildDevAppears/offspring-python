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
    return <Box sx={{ height: "100vh", position: "relative",}}>
        <Box component="div" width="100%" height="100%" sx={
            {
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
