/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { Button, ButtonProps } from "@mui/base"
import { SxProps, Theme, styled } from "@mui/system"

interface IBaseButtonProps extends ButtonProps {
    sx?: SxProps<Theme>
}

const Styled = styled(Button)({
    padding: "1rem 2rem",
    border: "0",
    borderRadius: "2rem",
})

export const BaseButton: React.FC<IBaseButtonProps> = ({ children, sx, ...props }) => {
    return <Styled sx={{ backgroundColor: "primary.main", ...sx, }} {...props}>{ children }</Styled>
}
