/**
* Copyright (c) AWildDevAppears
*/

import { Plane } from "@react-three/drei";
import React from "react";

interface IR3CardProps {
    pos: [number, number, number];
}

export const R3Card: React.FC<IR3CardProps> = ({ pos }) => {
    return <Plane args={pos}>
        <meshStandardMaterial color="red" />
    </Plane>
};
