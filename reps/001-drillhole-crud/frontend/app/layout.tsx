import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Drillhole CRUD",
  description: "Rep 001 consumer",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
