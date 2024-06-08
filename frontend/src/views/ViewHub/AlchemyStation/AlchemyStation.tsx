/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { SVGPaper } from "../../../assets/svg/SVGPaper";
import { BaseButton } from "../../../components/BaseButton/BaseButton";

interface IAlchemyStationProps {
    onBack: () => void;
}

export const AlchemyStation: React.FC<IAlchemyStationProps> = ({ onBack }) => {
    return <SVGPaper>
        <BaseButton onClick={onBack}>
            Go back
        </BaseButton>
    </SVGPaper>
}
