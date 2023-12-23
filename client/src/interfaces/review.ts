interface Review {
    id: number;
    reservationId: number;
    rating: number;
    comment?: string | null;
    reservation: number;
    createdAt: Date;
    updatedAt: Date;
    userId: number;
    roomId: number;
}
