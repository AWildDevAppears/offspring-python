/**
* Copyright (c) AWildDevAppears
*/

import { createBrowserRouter } from "react-router-dom";
import { ViewDebug } from "./ViewDebug/ViewDebug";
import { ViewHub } from "./ViewHub/ViewHub";
import { ViewDungeon } from "./ViewDungeon/ViewDungeon";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <ViewHub />,
    },
    {
        path: "/debug",
        element: <ViewDebug />,
    },
    {
        path: "/quests/:id",
        element: <ViewDungeon />,
    },
]);
