/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'images.unsplash.com',
            },
            {
                protocol: 'https',
                hostname: 'picsum.photos',
            },
            // localhost
            {
                protocol: 'http',
                hostname: 'localhost',
            },
        ],
    },
};

module.exports = nextConfig;
