import Link from "next/link";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 w-full backdrop-blur-md bg-white/80 border-b border-gray-100">
      <div className="container mx-auto px-4 h-20 flex items-center justify-between">
        <Link href="/" className="flex items-center space-x-2">
          <span className="font-serif text-2xl font-bold text-primary">N.K.T.</span>
        </Link>
        <nav className="hidden md:flex items-center space-x-8">
          <Link href="/" className="text-text-dark hover:text-primary transition-colors">Home</Link>
          <Link href="/jim-corbett" className="text-text-dark hover:text-primary transition-colors">Safaris</Link>
          <Link href="/chardham-yatra" className="text-text-dark hover:text-primary transition-colors">Pilgrimage</Link>
        </nav>
        <Link 
          href="/booking" 
          className="bg-primary text-white px-6 py-2 rounded-lg font-medium hover:bg-primary-hover transition-all hover:scale-105 active:scale-95 shadow-md hover:shadow-lg"
        >
          Book Now
        </Link>
      </div>
    </header>
  );
}
