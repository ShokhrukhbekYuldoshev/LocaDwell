// not MimeType because it is used by next.js or whatever
enum MediaMimeType {
    JPEG = 'image/jpeg',
    PNG = 'image/png',
    GIF = 'image/gif',
    WEBP = 'image/webp',
    MP4 = 'video/mp4',
    WEBM = 'video/webm',
}

interface Media {
    id: number;
    modelType: number; // 1 = Room, 2 = Reservation etc... I'm not sure if this is correct
    modelId: number;
    fileName?: string | null;
    mimeType?: MediaMimeType | null;
    mediaFile?: string | null;
}
