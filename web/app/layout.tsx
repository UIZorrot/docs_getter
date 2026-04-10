import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
    title: 'txzy/tool/getdoc',
    description: 'Grab documentation sites and download them as a ZIP archive.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
    return (
        <html lang="zh-CN" suppressHydrationWarning>
            <body>{children}</body>
        </html>
    );
}
