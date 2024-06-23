/**
* Copyright (c) AWildDevAppears
*/

import React, { useCallback, useMemo, useState } from "react";
import { BaseButton } from "../../components/BaseButton/BaseButton";
import { Box, positions } from "@mui/system";
import Grid from "@mui/system/Unstable_Grid";
import { DeckStorage } from "./DeckStorage/DeckStorage";
import { QuestBoard } from "./QuestBoard/QuestBoard";
import { EquipmentStorage } from "./EquipmentStorage/EquipmentStorage";
import { CharacterSelect } from "./CharacterSelect/CharacterSelect";
import { AlchemyStation } from "./AlchemyStation/AlchemyStation";
import { Shop } from "./Shop/Shop";
import { Canvas } from "@react-three/fiber";

interface IViewHubProps {

}

type ViewHubState = "middle" | "alchemy" | "character" | "quest" | "deck" | "equip" | "shop";

export const ViewHub: React.FC<IViewHubProps> = () => {
    const [mode, setMode] = useState<ViewHubState>("middle");

    const shouldShowLeft = useMemo(() => {
        switch (mode) {
            case "equip":
            case "character":
                return true;
            default:
                return false;
        }
    }, [mode]);

    const navigator = useMemo(() => (
        <Box component="div">
            <BaseButton onClick={() => setMode("deck")}>
                Deck builder
            </BaseButton>
            <BaseButton onClick={() => setMode("equip")}>
                Equipment
            </BaseButton>
            <BaseButton onClick={() => setMode("alchemy")}>
                Alchemy
            </BaseButton>
            <BaseButton onClick={() => setMode("quest")}>
                Quest board
            </BaseButton>
            <BaseButton onClick={() => setMode("shop")}>
                Shop
            </BaseButton>
            <BaseButton onClick={() => setMode("character")}>
                Character view
            </BaseButton>
        </Box>
    ), [mode])

    const goBack = useCallback(() => setMode("middle"), []);

    const interactivePane = useMemo(() => {
        switch (mode) {
            case "deck":
                return <DeckStorage onBack={goBack} />
            case "quest":
                return <QuestBoard onBack={goBack} />
            case "equip":
                return <EquipmentStorage onBack={goBack} />
            case "character":
                return <CharacterSelect onBack={goBack} />
            case "alchemy":
                return <AlchemyStation onBack={goBack} />
            case "shop":
                return <Shop onBack={goBack} />
            default:
                return navigator;
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
            case "middle":
                return true;
            default:
                return false;
        }
    }, [mode]);

    return (<Box
        component="div"
        sx={{ height: "100vh", width: "100vw", position: "relative" }}
    >
        <Canvas>
            Hello I am a canvas
        </Canvas>

        <Box
            component="div"
            sx={{ position: "absolute", top: "0", width: "100vw", height: "100vh" }}
        >
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
        </Box>
    </Box>);
}
