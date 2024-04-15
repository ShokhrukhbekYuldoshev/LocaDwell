'use client';

import React from 'react';
import { useGetRoomsQuery } from '@/lib/api/room';
import Image from 'next/image';
import { BASE_MEDIA_URL } from '@/lib/constants';
import LoadingSpinner from '@/components/loading';
import Link from 'next/link';

const RoomListPage = () => {
    const { data: rooms, error, isLoading } = useGetRoomsQuery();

    if (isLoading) return <LoadingSpinner />;

    if (error) return <div>Error</div>;

    return (
        <div className='container grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4'>
            {rooms &&
                rooms.map((room) => (
                    <Link href={`/rooms/${room.id}`} key={room.id}>
                        <div
                            key={room.id}
                            className='bg-white rounded-lg overflow-hidden shadow-lg'
                        >
                            <Image
                                className='h-48 w-full object-cover'
                                src={BASE_MEDIA_URL + room.media_files[0]}
                                alt={room.summary}
                                width={500}
                                height={500}
                            />
                            <div className='p-6'>
                                <div className='font-bold text-xl mb-2'>
                                    {room.summary}
                                </div>
                                <p className='text-gray-700 text-base'>
                                    {room.address}
                                </p>
                                <div className='mt-4'>
                                    <span className='text-sm font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-gray-200'>
                                        {room.price} $ / night
                                    </span>
                                </div>
                            </div>
                        </div>
                    </Link>
                ))}
        </div>
    );
};

export default RoomListPage;
