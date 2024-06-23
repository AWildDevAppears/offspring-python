/**
* Copyright (c) AWildDevAppears
*/

import { ICard } from "../models/Card";

declare global {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    interface Window { pywebview: any; }
}

export interface IDeckResponse {
    deck: ICard[];
}

export interface IOffspringResponse<T = Record<string, unknown>> {
        failed: boolean;
        message?: string;
        error_ref?: string;
        data?: T
}

const responseNoConnection: IOffspringResponse = {
    failed: true,
    error_ref: "NO_CONN",
    message: "Cannot connect to Offspring"
}

export const Offspring = {
    dungeon: {
        initDungeon(): IOffspringResponse {
            if (!window.pywebview) return responseNoConnection;
            return window.pywebview.api.dungeon_state_init();
        },
        nextRound(): IOffspringResponse {
            if (!window.pywebview) return responseNoConnection;
            return window.pywebview.api.dungeon_next_round();
        },
        nextLocation(): IOffspringResponse {
            if (!window.pywebview) return responseNoConnection;
            return window.pywebview.api.dungeon_next_location();
        },
        getDeck(): IOffspringResponse<IDeckResponse> | IOffspringResponse {
            if (!window.pywebview) return responseNoConnection;
            return window.pywebview.api.dungeon_get_deck();
        }
    },
    inventory: {},
    store: {},
    // ... Rest

} as const;
