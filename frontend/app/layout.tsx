import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Timeline",
  description: "Timeline: Visualize and manage your events easily.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className="antialiased"
      >
        {children}
      </body>
    </html>
  );
}
