/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { SVGPaper } from "../../../assets/svg/SVGPaper";
import { BaseButton } from "../../../components/BaseButton/BaseButton";

interface ICharacterSelectProps {
    onBack: () => void;
}

export const CharacterSelect: React.FC<ICharacterSelectProps> = ({ onBack }) => {
    return <SVGPaper>
        <BaseButton onClick={onBack}>
            Go back
        </BaseButton>
    </SVGPaper>
};
