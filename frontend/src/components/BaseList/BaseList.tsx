/**
* Copyright (c) AWildDevAppears
*/

import { styled } from "@mui/system";
import React, { PropsWithChildren } from "react";

interface IBaseListProps extends PropsWithChildren {

}

const StyledList = styled("ul")({
    listStyle: "none",
    margin: "0",
    padding: "0",

});

export const BaseList: React.FC<IBaseListProps> = ({ children }) => {
    return <StyledList>
        { children }
    </StyledList>
};
