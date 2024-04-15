import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import MainNav from '@/components/main-nav';
import { StoreProvider } from '@/lib/store-provider';
const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
    title: 'LocaDwell',
    description:
        'Full stack web application that allows users to book rooms in hotels and leave reviews about their experience. The application is built using the Django REST Framework and Next.js.',
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang='en'>
            <body className={inter.className}>
                <StoreProvider>
                    <MainNav />
                    {children}
                </StoreProvider>
            </body>
        </html>
    );
}
