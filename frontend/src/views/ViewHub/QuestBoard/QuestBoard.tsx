/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { SVGPaper } from "../../../assets/svg/SVGPaper";
import { BaseButton } from "../../../components/BaseButton/BaseButton";
import { Box } from "@mui/system";
import { BaseList } from "../../../components/BaseList/BaseList";
import { BaseListItem } from "../../../components/BaseListItem/BaseListItem";
import { BaseListItemTitle } from "../../../components/BaseListItem/BaseListItemTitle/BaseListItemTitle";

interface IQuestBoardProps {
    onBack: () => void;
}

export const QuestBoard: React.FC<IQuestBoardProps> = ({ onBack }) => {
    const id = 1;

    return <SVGPaper>
        <Box component="div" sx={{ display: "flex", flexDirection: "column", height: "calc(100vh - 3rem)" }}>
            <Box component="div" sx={{ flex: "1" }}>
                <BaseList>
                    <BaseListItem to={`quests/${id}`}>
                        <BaseListItemTitle>Hello I am a quest</BaseListItemTitle>
                    </BaseListItem>
                </BaseList>
            </Box>
            <Box component="div">
                <BaseButton onClick={onBack}>
                    Go back
                </BaseButton>
            </Box>
        </Box>
    </SVGPaper>;
};
