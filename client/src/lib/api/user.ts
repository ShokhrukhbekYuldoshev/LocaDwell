'use client';

// src/lib/api/user.ts
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { BASE_URL } from '../constants';

export const userApi = createApi({
    reducerPath: 'userApi',
    baseQuery: fetchBaseQuery({ baseUrl: BASE_URL }),
    endpoints: (builder) => ({
        registerUser: builder.mutation<User, Partial<User>>({
            query: (userData) => ({
                url: 'users/register',
                method: 'POST',
                body: userData,
            }),
        }),
        loginUser: builder.mutation<User, Partial<User>>({
            query: (userData) => ({
                url: 'users/login',
                method: 'POST',
                body: userData,
            }),
        }),
        logoutUser: builder.mutation<void, void>({
            query: () => ({
                url: 'users/logout',
                method: 'POST',
            }),
        }),
        refreshToken: builder.mutation<void, void>({
            query: () => ({
                url: 'users/token/refresh',
                method: 'POST',
            }),
        }),
        getUsers: builder.query<Array<User>, void>({
            query: () => 'users',
        }),
        getUserDetails: builder.query<User, number>({
            query: (userId) => `users/${userId}`,
        }),
        updateUser: builder.mutation<
            void,
            { userId: number; updates: Partial<User> }
        >({
            query: ({ userId, updates }) => ({
                url: `users/${userId}/update`,
                method: 'PUT',
                body: updates,
            }),
        }),
        deleteUser: builder.mutation<void, number>({
            query: (userId) => ({
                url: `users/${userId}/delete`,
                method: 'DELETE',
            }),
        }),
    }),
});

export const {
    useRegisterUserMutation,
    useLoginUserMutation,
    useLogoutUserMutation,
    useRefreshTokenMutation,
    useGetUsersQuery,
    useGetUserDetailsQuery,
    useUpdateUserMutation,
    useDeleteUserMutation,
} = userApi;
