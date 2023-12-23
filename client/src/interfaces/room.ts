interface Room {
    id: number;
    homeType: 'House' | 'Apartment';
    roomType: 'Entire Place' | 'Private Room' | 'Shared Room';
    totalOccupancy: number;
    totalBedrooms: number;
    totalBathrooms: number;
    summary: string;
    address: string;
    hasTV: boolean;
    hasKitchen: boolean;
    hasHeating: boolean;
    hasInternet: boolean;
    price: number;
    publishedAt: Date;
    ownerId: number;
    createdAt: Date;
    updatedAt: Date;
    latitude: number;
    longitude: number;
    media_files: string[];
}
