/**
* Copyright (c) AWildDevAppears
*/

import React from "react";
import { SVGBackground } from "./SVGBackground";

import card from "./SVGCard.svg";

interface ISVGCardProps {

}

export const SVGCard: React.FC<ISVGCardProps> = () => {
    return <SVGBackground path={card} />
};
