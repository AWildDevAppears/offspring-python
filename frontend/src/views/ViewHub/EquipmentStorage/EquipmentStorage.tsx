/**
* Copyright (c) AWildDevAppears
*/

import React from "react"
import { SVGPaper } from "../../../assets/svg/SVGPaper";
import { BaseButton } from "../../../components/BaseButton/BaseButton";

interface IEquipmentStorageProps {
    onBack: () => void;
}

export const EquipmentStorage: React.FC<IEquipmentStorageProps> = ({ onBack }) => {
    return <SVGPaper>
        <BaseButton onClick={onBack}>
            Go back
        </BaseButton>
    </SVGPaper>;
}
