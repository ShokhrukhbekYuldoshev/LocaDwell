'use client';

import { useRouter } from 'next/router';
import Image from 'next/image';
import { useGetRoomDetailsQuery } from '@/lib/api/room';
import LoadingSpinner from '@/components/loading';

export default function RoomDetailsPage() {
    const router = useRouter();

    const { id } = router.query;

    const {
        data: room,
        error,
        isLoading,
    } = useGetRoomDetailsQuery(id as string);

    if (isLoading) return <LoadingSpinner />;

    if (error) return <div>Error</div>;

    if (!room) return <div>Room not found</div>;

    return (
        <div className='min-h-screen bg-gray-100 flex items-center justify-center'>
            <div className='bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col my-2'>
                <div className='-mx-3 md:flex mb-6'>
                    <div className='md:w-1/2 px-3 mb-6 md:mb-0'>
                        <label
                            className='block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2'
                            htmlFor='grid-first-name'
                        >
                            Home Type
                        </label>
                        <input
                            className='appearance-none block w-full bg-grey-lighter text-grey-darker border border-red rounded py-3 px-4 mb-3'
                            id='grid-first-name'
                            type='text'
                            value={room.homeType}
                            disabled
                        />
                    </div>
                    <div className='md:w-1/2 px-3'>
                        <label
                            className='block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2'
                            htmlFor='grid-last-name'
                        >
                            Room Type
                        </label>
                        <input
                            className='appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4'
                            id='grid-last-name'
                            type='text'
                            value={room.roomType}
                            disabled
                        />
                    </div>
                </div>
                <div className='md:flex mb-6'>
                    <div className='md:w-full px-3'>
                        <label
                            className='block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2'
                            htmlFor='grid-password'
                        >
                            Summary
                        </label>
                        <textarea
                            className='appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3'
                            id='grid-password'
                            value={room.summary}
                            disabled
                        />
                    </div>
                </div>
                <div className='md:flex mb-6'>
                    <div className='md:w-full px-3'>
                        <label
                            className='block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2'
                            htmlFor='grid-password'
                        >
                            Address
                        </label>
                        <textarea
                            className='appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3'
                            id='grid-password'
                            value={room.address}
                            disabled
                        />
                    </div>
                </div>
                <div className='md:flex mb-6'>
                    <div className='md:w-full px-3'>
                        <label
                            className='block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2'
                            htmlFor='grid-password'
                        >
                            Price
                        </label>
                        <input
                            className='appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3'
                            id='grid-password'
                            type='text'
                            value={room.price}
                            disabled
                        />
                    </div>
                </div>
                <div className='md:flex mb-6'>
                    <div className='md:w-full px-3'>
                        <label
                            className='block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2'
                            htmlFor='grid-password'
                        >
                            Media Files
                        </label>
                        <div className='flex flex-wrap'>
                            {room.media_files.map((file, index) => (
                                <Image
                                    key={index}
                                    src={file}
                                    alt=''
                                    className='w-full sm:w-1/2 lg:w-1/3 px-2'
                                />
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
