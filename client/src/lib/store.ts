'use client';

import { configureStore } from '@reduxjs/toolkit';

import { userApi } from './api/user';
import { roomApi } from './api/room';

export const store: ReturnType<typeof configureStore> = configureStore({
    reducer: {
        [userApi.reducerPath]: userApi.reducer,
        [roomApi.reducerPath]: roomApi.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(userApi.middleware, roomApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
