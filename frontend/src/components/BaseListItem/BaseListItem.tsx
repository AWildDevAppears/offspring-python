/**
* Copyright (c) AWildDevAppears
*/

import { styled } from "@mui/system";
import React, { PropsWithChildren } from "react";

interface IBaseListItemProps extends PropsWithChildren {

}

const StyledListItem = styled("li")({
    margin: "0 0 0.5rem",
    padding: "1.5rem",
    borderRadius: "1rem",
    backgroundColor: "white",
    display: "grid",
    gridTemplateAreas: `
        "liicon lititle"
        "liicon lidescription"
        "liactions liactions"
    `,
    gridTemplateRows: "1fr 2fr 1fr",
    gridTemplateColumns: "1fr 3fr",
});

export const BaseListItem: React.FC<IBaseListItemProps> = ({ children }) => {
    return <StyledListItem>
        { children }
    </StyledListItem>
};
