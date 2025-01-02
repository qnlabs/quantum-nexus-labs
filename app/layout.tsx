import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Quantum Nexus Labs',
  description: 'Advanced Quantum Computing & AI Research',
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
