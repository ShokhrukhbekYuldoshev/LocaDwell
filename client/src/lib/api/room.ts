'use client';

// src/api/room.ts
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { BASE_URL } from '../constants';

export const roomApi = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({ baseUrl: BASE_URL }),
    endpoints: (builder) => ({
        getRooms: builder.query<Array<Room>, void>({
            query: () => 'rooms',
        }),
        getRoomDetails: builder.query<Room, string>({
            query: (roomId) => `rooms/${roomId}`,
        }),
        createRoom: builder.mutation<Room, Partial<Room>>({
            query: (newRoom) => ({
                url: 'rooms/create',
                method: 'POST',
                body: newRoom,
            }),
        }),
        updateRoom: builder.mutation<
            void,
            { roomId: number; updates: Partial<Room> }
        >({
            query: ({ roomId, updates }) => ({
                url: `rooms/${roomId}/update`,
                method: 'PUT',
                body: updates,
            }),
        }),
        deleteRoom: builder.mutation<void, number>({
            query: (roomId) => ({
                url: `rooms/${roomId}/delete`,
                method: 'DELETE',
            }),
        }),
    }),
});

export const {
    useGetRoomsQuery,
    useGetRoomDetailsQuery,
    useCreateRoomMutation,
    useUpdateRoomMutation,
    useDeleteRoomMutation,
} = roomApi;
