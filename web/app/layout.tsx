import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
    title: "Doc Getter Demo",
    description: "Submit crawl jobs and download mirrored Markdown docs.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
    return (
        <html lang="zh-CN">
            <body>{children}</body>
        </html>
    );
}
