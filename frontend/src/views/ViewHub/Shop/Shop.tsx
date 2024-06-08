/**
* Copyright (c) AWildDevAppears
*/

import React from "react"
import { SVGPaper } from "../../../assets/svg/SVGPaper"
import { BaseButton } from "../../../components/BaseButton/BaseButton";

interface IShopProps {
    onBack: () => void;
}

export const Shop: React.FC<IShopProps> = ({ onBack }) => {
    return <SVGPaper>
        <BaseButton onClick={onBack}>
            Go back
        </BaseButton>
    </SVGPaper>
}
