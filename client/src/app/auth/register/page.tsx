'use client';

import { Button } from '@/components/ui/button';
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from '@/components/ui/card';
import {
    FormField,
    FormControl,
    FormLabel,
    FormMessage,
    FormItem,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';

import Link from 'next/link';
import { useForm, FormProvider } from 'react-hook-form';

export default function RegisterPage() {
    const form = useForm();

    return (
        <div className='grid h-screen place-items-center'>
            <Card className='w-[350px]'>
                <CardHeader>
                    <CardTitle>Register</CardTitle>
                    <CardDescription>Create a new account</CardDescription>
                </CardHeader>
                <CardContent>
                    <FormProvider {...form}>
                        <FormField
                            control={form.control}
                            name='email'
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Email</FormLabel>
                                    <FormControl>
                                        <Input
                                            placeholder='your-email@example.com'
                                            {...field}
                                        />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        {/* space */}
                        <div className='h-4' />
                        <FormField
                            control={form.control}
                            name='password'
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Password</FormLabel>
                                    <FormControl>
                                        <Input
                                            placeholder='********'
                                            {...field}
                                        />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </FormProvider>
                </CardContent>
                <CardFooter>
                    <Button className='w-full'>Register</Button>
                </CardFooter>
                <CardFooter>
                    <Link href='/auth/login'>Already have an account?</Link>
                </CardFooter>
            </Card>
        </div>
    );
}
