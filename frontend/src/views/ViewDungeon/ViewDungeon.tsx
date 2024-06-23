/**
* Copyright (c) AWildDevAppears
*/

import { Box } from "@mui/system";
import React, { useEffect, useState } from "react";
import { Canvas } from "@react-three/fiber";
import { Offspring } from "../../utilities/offspring";
import { ICard } from "../../models/Card";

interface IViewDungeonProps {

}

export const ViewDungeon: React.FC<IViewDungeonProps> = () => {
    const [deck, setDeck] = useState<ICard[]>([]);

    useEffect(() => {
        (async () => {
            await Offspring.dungeon.initDungeon();

            const newDeck = await Offspring.dungeon.getDeck();
            console.log(newDeck)
            setDeck(newDeck);
        })();
    }, []);

    return <div>
        <Box component="div" sx={{ height: "100vh", color: "#FFF" }}>
            {deck.map((card: ICard) => <div key={card.id}>
                {Object.keys(card).map(key => <div key={key}>{key}: {card[key]}</div>)}
            </div>)}
        </Box>
    </div>
};
