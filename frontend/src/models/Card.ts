/**
* Copyright (c) AWildDevAppears
*/

export enum CardTarget {
    SELF = "self",
    ENEMY = "enemy",
    ENEMY_ALL = "enemy_all",
    ALL = "all",
    ARENA = "arena",
    SPELL = "spell",
}

export interface ICard {
    id: string;
    description: string;
    damage: number;
    target: CardTarget;
    modifiers: str[];
}
