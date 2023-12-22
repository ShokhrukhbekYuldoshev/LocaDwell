import {
    Card,
    CardContent,
    CardTitle,
    CardDescription,
} from '@/components/ui/card';
import Link from 'next/link';
import Image from 'next/image';
import { StarIcon } from 'lucide-react';

export default function RoomListPage() {
    const rooms: Room[] = [
        {
            id: 1,
            homeType: 'House',
            roomType: 'Entire Place',
            totalOccupancy: 4,
            totalBedrooms: 2,
            totalBathrooms: 1,
            summary: 'This is a beautiful house with a garden.',
            address: '123 Main St',
            hasTV: true,
            hasKitchen: true,
            hasHeating: true,
            hasInternet: true,
            price: 100,
            publishedAt: new Date(),
            ownerId: 1,
            createdAt: new Date(),
            updatedAt: new Date(),
            latitude: 40.7128,
            longitude: -74.006,
            media_files: [
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
            ],
        },
        {
            id: 1,
            homeType: 'House',
            roomType: 'Entire Place',
            totalOccupancy: 4,
            totalBedrooms: 2,
            totalBathrooms: 1,
            summary: 'This is a beautiful house with a garden.',
            address: '123 Main St',
            hasTV: true,
            hasKitchen: true,
            hasHeating: true,
            hasInternet: true,
            price: 100,
            publishedAt: new Date(),
            ownerId: 1,
            createdAt: new Date(),
            updatedAt: new Date(),
            latitude: 40.7128,
            longitude: -74.006,
            media_files: [
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
            ],
        },
        {
            id: 1,
            homeType: 'House',
            roomType: 'Entire Place',
            totalOccupancy: 4,
            totalBedrooms: 2,
            totalBathrooms: 1,
            summary: 'This is a beautiful house with a garden.',
            address: '123 Main St',
            hasTV: true,
            hasKitchen: true,
            hasHeating: true,
            hasInternet: true,
            price: 100,
            publishedAt: new Date(),
            ownerId: 1,
            createdAt: new Date(),
            updatedAt: new Date(),
            latitude: 40.7128,
            longitude: -74.006,
            media_files: [
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
            ],
        },
        {
            id: 1,
            homeType: 'House',
            roomType: 'Entire Place',
            totalOccupancy: 4,
            totalBedrooms: 2,
            totalBathrooms: 1,
            summary: 'This is a beautiful house with a garden.',
            address: '123 Main St',
            hasTV: true,
            hasKitchen: true,
            hasHeating: true,
            hasInternet: true,
            price: 100,
            publishedAt: new Date(),
            ownerId: 1,
            createdAt: new Date(),
            updatedAt: new Date(),
            latitude: 40.7128,
            longitude: -74.006,
            media_files: [
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
            ],
        },
        {
            id: 1,
            homeType: 'House',
            roomType: 'Entire Place',
            totalOccupancy: 4,
            totalBedrooms: 2,
            totalBathrooms: 1,
            summary: 'This is a beautiful house with a garden.',
            address: '123 Main St',
            hasTV: true,
            hasKitchen: true,
            hasHeating: true,
            hasInternet: true,
            price: 100,
            publishedAt: new Date(),
            ownerId: 1,
            createdAt: new Date(),
            updatedAt: new Date(),
            latitude: 40.7128,
            longitude: -74.006,
            media_files: [
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
            ],
        },
        {
            id: 1,
            homeType: 'House',
            roomType: 'Entire Place',
            totalOccupancy: 4,
            totalBedrooms: 2,
            totalBathrooms: 1,
            summary: 'This is a beautiful house with a garden.',
            address: '123 Main St',
            hasTV: true,
            hasKitchen: true,
            hasHeating: true,
            hasInternet: true,
            price: 100,
            publishedAt: new Date(),
            ownerId: 1,
            createdAt: new Date(),
            updatedAt: new Date(),
            latitude: 40.7128,
            longitude: -74.006,
            media_files: [
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
                'https://images.unsplash.com/photo-1505533321630-975218a5f66f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D',
            ],
        },
    ];

    return (
        <div className='container mx-auto p-4'>
            <h1 className='text-3xl font-bold mb-4'>Rooms</h1>
            <div className='grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8'>
                {rooms.map((room) => (
                    <Link href={`/rooms/${room.id}`} key={room.id}>
                        <Card key={room.id}>
                            <CardTitle>
                                <Image
                                    src={room.media_files[0]}
                                    alt={room.address}
                                    width={500}
                                    height={0}
                                    className='w-full h-full object-cover rounded-md'
                                />
                            </CardTitle>
                            <div className='h-4' />
                            <CardContent>
                                <CardTitle>{room.address}</CardTitle>
                                <div className='h-2' />
                                <CardDescription>
                                    {room.summary}
                                </CardDescription>
                                <div className='flex items-center justify-between mt-4'>
                                    <div className='flex items-center gap-1'>
                                        <StarIcon className='w-5 h-5 text-yellow-500' />
                                        <span>{room.price}</span>
                                    </div>
                                    <span className='text-lg font-bold'>
                                        ${room.price}
                                    </span>
                                </div>
                            </CardContent>
                        </Card>
                    </Link>
                ))}
            </div>
        </div>
    );
}
