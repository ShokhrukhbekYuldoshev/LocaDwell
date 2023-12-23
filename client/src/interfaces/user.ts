interface User {
    id: number;
    username?: string | null;
    email: string;
    emailVerifiedAt?: Date | null;
    password: string;
    rememberToken?: string | null;
    createdAt: Date;
    updatedAt: Date;
    phoneNumber?: string | null;
    description?: string | null;
    profileImage?: string | null; // Assuming image is stored as URL
    groups?: Group[];
    userPermissions?: Permission[];
}

interface Group {
    id: number;
    name: string;
    customUsers: User[];
}

interface Permission {
    id: number;
    name: string;
    customUsers: User[];
}
