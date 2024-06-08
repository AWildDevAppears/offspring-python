/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { SVGPaper } from "../../../assets/svg/SVGPaper";
import { BaseButton } from "../../../components/BaseButton/BaseButton";

interface IDeckStorageProps {
    onBack: () => void;
}

export const DeckStorage: React.FC<IDeckStorageProps> = ({ onBack }) => {
    return <SVGPaper>
        <BaseButton onClick={onBack}>
            Go back
        </BaseButton>
    </SVGPaper>
};
