/**
* Copyright (c) AWildDevAppears
*/

import { Box } from "@mui/system";
import React, { PropsWithChildren } from "react";

interface IBaseListItemTitleProps extends PropsWithChildren {

}

export const BaseListItemTitle: React.FC<IBaseListItemTitleProps> = ({ children }) => {
    return <Box component="div" sx={{ gridArea: "lititle" }}>
        { children }
    </Box>
};
