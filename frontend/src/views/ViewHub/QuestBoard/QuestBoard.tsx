/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { SVGPaper } from "../../../assets/svg/SVGPaper";
import { BaseButton } from "../../../components/BaseButton/BaseButton";

interface IQuestBoardProps {
    onBack: () => void;
}

export const QuestBoard: React.FC<IQuestBoardProps> = ({ onBack }) => {
    return <SVGPaper>
        <BaseButton onClick={onBack}>
            Go back
        </BaseButton>
    </SVGPaper>;
};
