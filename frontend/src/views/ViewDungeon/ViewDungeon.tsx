/**
* Copyright (c) AWildDevAppears
*/

import { Box, Container } from "@mui/system";
import Grid from "@mui/system/Unstable_Grid/Grid";
import React from "react";
import { SVGCard } from "../../assets/svg/SVGCard";

interface IViewDungeonProps {

}

export const ViewDungeon: React.FC<IViewDungeonProps> = () => {
    return <div>
        <Container>
            <Box component="div" sx={{
                display: "grid",
                gridTemplateRows: "3fr 1fr",
                gridTemplateColumns: "100%",
                gridTemplateAreas: `
                    "top"
                    "hud"
                `,
            }}>
                <Box height="45%" sx={{ gridArea: "hud" }}>
                    <Grid container>
                        <Grid xs={2}>
                            <SVGCard />
                        </Grid>
                    </Grid>
                </Box>
            </Box>
        </Container>
    </div>
};
