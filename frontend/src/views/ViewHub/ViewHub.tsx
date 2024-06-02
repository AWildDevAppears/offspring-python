/**
* Copyright (c) AWildDevAppears
*/

import React, { useCallback, useMemo, useState } from "react";
import { BaseButton } from "../../components/BaseButton/BaseButton";
import { Box } from "@mui/system";
import Grid from "@mui/system/Unstable_Grid";
import { DeckStorage } from "./DeckStorage/DeckStorage";
import { QuestBoard } from "./QuestBoard/QuestBoard";
import { EquipmentStorage } from "./EquipmentStorage/EquipmentStorage";
import { CharacterSelect } from "./CharacterSelect/CharacterSelect";
import { AlchemyStation } from "./AlchemyStation/AlchemyStation";
import { Shop } from "./Shop/Shop";

interface IViewHubProps {

}

type ViewHubState = "middle" | "alchemy" | "character" | "quest" | "deck" | "equip" | "shop";

export const ViewHub: React.FC<IViewHubProps> = () => {
    const [mode, setMode] = useState<ViewHubState>("middle");

    const switchMode = useCallback(() => {
        switch (mode) {
            case "middle":
                setMode("alchemy");
                return;
            case "alchemy":
                setMode("character");
                return;
            case "character":
                setMode("quest");
                return;
            case "quest":
                setMode("deck");
                return;
            case "deck":
                setMode("equip");
                return;
            case "equip":
                setMode("shop");
                return;
            case "shop":
                setMode("middle");
                return;
        }
    }, [mode]);

    const shouldShowLeft = useMemo(() => {
        switch (mode) {
            case "equip":
            case "character":
                return true;
            default:
                return false;
        }
    }, [mode]);

    const interactivePane = useMemo(() => {
        switch (mode) {
            case "deck":
                return <DeckStorage />
            case "quest":
                return <QuestBoard />
            case "equip":
                return <EquipmentStorage />
            case "character":
                return <CharacterSelect />
            case "alchemy":
                return <AlchemyStation />
            case "shop":
                return <Shop />
            default:
                return null;
        }
    }, [mode]);

    const shouldShowRight = useMemo(() => {
        switch (mode) {
            case "deck":
            case "shop":
            case "alchemy":
                return "true";
            default:
                return false;
        }
    }, [mode]);

    const shouldShowCenter = useMemo(() => {
        switch (mode) {
            case "quest":
                return true;
            default:
                return false;
        }
    }, [mode]);

    return <Box sx={{ height: "100vh", width: "100vw", position: "relative", }}>
        <Box sx={{ height: "100%", width: "100%", position: "absolute" }} />

        <BaseButton onClick={switchMode} sx={{ position: "absolute", top: "1rem", left: "1rem" }}>
            Switch mode {mode}
        </BaseButton>

        <Grid container>
            {shouldShowLeft && <Grid xs={6}>
                {interactivePane}
            </Grid>}

            {shouldShowCenter && <Grid xs={8} xsOffset={2}>
                {interactivePane}
            </Grid>}

            {shouldShowRight && <Grid xs={6} xsOffset={6}>
                {interactivePane}
            </Grid>}
        </Grid>
    </Box>;
}
